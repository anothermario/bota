"""
backtest.py
===========
Offline event-driven backtester that mirrors the Pine Script "Adaptive KAMA
Trend-Follower" logic 1:1, so you can validate / finetune it on real data
*before* trusting it on TradingView. The 0.04% per-fill fee is included.

Input CSV must have columns (case-insensitive): time/date, open, high, low, close.
You can export this straight from TradingView (Export chart data) or Binance.

Usage:
    python backtest.py --csv BTCUSDT_4h.csv
    python backtest.py --demo                 # runs on synthetic data (smoke test only)
    python backtest.py --csv data.csv --params params.json
"""
import argparse
import json
import math
import sys

import numpy as np
import pandas as pd

FEE = 0.0004  # 0.04% per fill, same as the Pine commission

DEFAULT_PARAMS = {
    "er_len": 20,
    "kama_fast": 2,
    "kama_slow": 30,
    "er_thresh": 0.30,
    "use_adx": True,
    "adx_len": 14,
    "adx_thresh": 20.0,
    "don_len": 20,
    "atr_len": 14,
    "atr_mult": 3.0,
    "chand_len": 22,
    "risk_pct": 1.0,
    "allow_short": True,
    "initial_capital": 10000.0,
}


# ── Indicator helpers (vectorised; no lookahead) ──────────────────────────────
def kama(close, er_len, fast, slow):
    chg = (close - close.shift(er_len)).abs()
    noise = close.diff().abs().rolling(er_len).sum()
    er = (chg / noise).replace([np.inf, -np.inf], 0).fillna(0)
    fast_sc = 2.0 / (fast + 1)
    slow_sc = 2.0 / (slow + 1)
    sc = (er * (fast_sc - slow_sc) + slow_sc) ** 2
    out = np.full(len(close), np.nan)
    c = close.to_numpy()
    s = sc.to_numpy()
    for i in range(len(c)):
        if i == 0 or math.isnan(out[i - 1]):
            out[i] = c[i]
        else:
            out[i] = out[i - 1] + s[i] * (c[i] - out[i - 1])
    return pd.Series(out, index=close.index), er


def atr(df, length):
    h, l, c = df["high"], df["low"], df["close"]
    tr = pd.concat([h - l, (h - c.shift()).abs(), (l - c.shift()).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1 / length, adjust=False).mean()


def adx(df, length):
    h, l, c = df["high"], df["low"], df["close"]
    up = h.diff()
    dn = -l.diff()
    plus_dm = np.where((up > dn) & (up > 0), up, 0.0)
    minus_dm = np.where((dn > up) & (dn > 0), dn, 0.0)
    tr = pd.concat([h - l, (h - c.shift()).abs(), (l - c.shift()).abs()], axis=1).max(axis=1)
    atr_ = tr.ewm(alpha=1 / length, adjust=False).mean()
    plus_di = 100 * pd.Series(plus_dm, index=df.index).ewm(alpha=1 / length, adjust=False).mean() / atr_
    minus_di = 100 * pd.Series(minus_dm, index=df.index).ewm(alpha=1 / length, adjust=False).mean() / atr_
    dx = 100 * (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)
    return dx.ewm(alpha=1 / length, adjust=False).mean().fillna(0)


# ── Backtest engine ───────────────────────────────────────────────────────────
def run_backtest(df, params):
    p = {**DEFAULT_PARAMS, **params}
    df = df.copy()
    kama_s, er = kama(df["close"], p["er_len"], p["kama_fast"], p["kama_slow"])
    df["kama"] = kama_s
    df["er"] = er
    df["atr"] = atr(df, p["atr_len"])
    df["adx"] = adx(df, p["adx_len"]) if p["use_adx"] else 100.0

    df["up_break"] = df["high"].rolling(p["don_len"]).max().shift(1)
    df["dn_break"] = df["low"].rolling(p["don_len"]).min().shift(1)
    df["trend_up"] = (df["close"] > df["kama"]) & (df["kama"] > df["kama"].shift(1))
    df["trend_dn"] = (df["close"] < df["kama"]) & (df["kama"] < df["kama"].shift(1))
    df["strong"] = (df["er"] >= p["er_thresh"]) & (df["adx"] >= (p["adx_thresh"] if p["use_adx"] else -1))

    df["long_sig"] = df["trend_up"] & df["strong"] & (df["close"] > df["up_break"])
    df["short_sig"] = p["allow_short"] & df["trend_dn"] & df["strong"] & (df["close"] < df["dn_break"])

    hi_chand = df["high"].rolling(p["chand_len"]).max()
    lo_chand = df["low"].rolling(p["chand_len"]).min()

    # timestamps (optional): used by the dashboard. None if the CSV has no time col.
    times = df["time"].tolist() if "time" in df.columns else [None] * len(df)

    def ts(x):
        # normalise a pandas/np timestamp to an ISO string the report can use
        if x is None:
            return None
        try:
            return pd.Timestamp(x).strftime("%Y-%m-%d %H:%M")
        except Exception:  # noqa: BLE001
            return str(x)

    equity = p["initial_capital"]
    pos = 0  # +1 long, -1 short, 0 flat
    qty = 0.0
    entry_price = 0.0
    entry_time = None
    trail = np.nan
    trades = []
    equity_curve = []

    cols = df.to_dict("records")
    for i in range(len(cols)):
        bar = cols[i]
        o, h, l, c = bar["open"], bar["high"], bar["low"], bar["close"]
        a = bar["atr"]
        if any(map(lambda x: x is None or (isinstance(x, float) and math.isnan(x)),
                   [bar["kama"], a, bar["up_break"], bar["dn_break"]])):
            equity_curve.append(equity)
            continue

        # --- manage open position: update trail, check stop on this bar ---
        if pos == 1:
            base = hi_chand.iloc[i] - a * p["atr_mult"]
            trail = base if math.isnan(trail) else max(trail, base)
            if l <= trail:  # stop hit
                exit_p = min(o, trail)  # conservative fill
                pnl = (exit_p - entry_price) * qty
                fee = (entry_price + exit_p) * qty * FEE
                equity += pnl - fee
                trades.append(dict(side="L", entry=entry_price, exit=exit_p, pnl=pnl - fee,
                                   entry_time=entry_time, exit_time=ts(times[i])))
                pos, qty, trail, entry_time = 0, 0.0, np.nan, None
        elif pos == -1:
            base = lo_chand.iloc[i] + a * p["atr_mult"]
            trail = base if math.isnan(trail) else min(trail, base)
            if h >= trail:
                exit_p = max(o, trail)
                pnl = (entry_price - exit_p) * qty
                fee = (entry_price + exit_p) * qty * FEE
                equity += pnl - fee
                trades.append(dict(side="S", entry=entry_price, exit=exit_p, pnl=pnl - fee,
                                   entry_time=entry_time, exit_time=ts(times[i])))
                pos, qty, trail, entry_time = 0, 0.0, np.nan, None

        # --- new signals (fill at NEXT bar open, like Pine) ---
        nxt = cols[i + 1]["open"] if i + 1 < len(cols) else None
        nxt_t = ts(times[i + 1]) if i + 1 < len(cols) else None
        if nxt is not None:
            stop_dist = a * p["atr_mult"]
            if stop_dist > 0:
                raw_qty = (equity * p["risk_pct"] / 100.0) / stop_dist
                max_qty = equity / nxt
                size = min(raw_qty, max_qty)
                if bar["long_sig"] and pos <= 0:
                    if pos == -1:  # reverse
                        pnl = (entry_price - nxt) * qty
                        fee = (entry_price + nxt) * qty * FEE
                        equity += pnl - fee
                        trades.append(dict(side="S", entry=entry_price, exit=nxt, pnl=pnl - fee,
                                           entry_time=entry_time, exit_time=nxt_t))
                    pos, qty, entry_price, trail, entry_time = 1, size, nxt, np.nan, nxt_t
                    equity -= nxt * size * FEE
                elif bar["short_sig"] and pos >= 0:
                    if pos == 1:
                        pnl = (nxt - entry_price) * qty
                        fee = (entry_price + nxt) * qty * FEE
                        equity += pnl - fee
                        trades.append(dict(side="L", entry=entry_price, exit=nxt, pnl=pnl - fee,
                                           entry_time=entry_time, exit_time=nxt_t))
                    pos, qty, entry_price, trail, entry_time = -1, size, nxt, np.nan, nxt_t
                    equity -= nxt * size * FEE
        equity_curve.append(equity)

    return _metrics(trades, equity_curve, p["initial_capital"])


def _metrics(trades, curve, capital):
    eq = pd.Series(curve)
    wins = [t for t in trades if t["pnl"] > 0]
    gross_p = sum(t["pnl"] for t in wins)
    gross_l = abs(sum(t["pnl"] for t in trades if t["pnl"] <= 0))
    net = eq.iloc[-1] - capital if len(eq) else 0.0
    peak = eq.cummax()
    dd = (eq - peak)
    rets = eq.pct_change().dropna()
    sharpe = (rets.mean() / rets.std() * math.sqrt(len(rets))) if len(rets) > 2 and rets.std() else 0.0
    return {
        "net_profit": round(net, 2),
        "net_profit_pct": round(net / capital * 100, 2),
        "total_trades": len(trades),
        "win_rate_pct": round(len(wins) / len(trades) * 100, 2) if trades else 0.0,
        "profit_factor": round(gross_p / gross_l, 3) if gross_l else float("inf"),
        "max_drawdown": round(dd.min(), 2) if len(dd) else 0.0,
        "sharpe_like": round(sharpe, 3),
        "final_equity": round(eq.iloc[-1], 2) if len(eq) else capital,
        "equity_curve": [round(x, 2) for x in curve],
        "trades": trades,
    }


# ── IO ────────────────────────────────────────────────────────────────────────
def load_csv(path):
    df = pd.read_csv(path)
    df.columns = [c.strip().lower() for c in df.columns]
    rename = {}
    for c in df.columns:
        if c in ("time", "date", "datetime", "timestamp"):
            rename[c] = "time"
    df = df.rename(columns=rename)
    needed = ["open", "high", "low", "close"]
    missing = [c for c in needed if c not in df.columns]
    if missing:
        raise ValueError(f"CSV missing columns: {missing}. Found: {list(df.columns)}")
    return df[[c for c in (["time"] + needed) if c in df.columns]].dropna().reset_index(drop=True)


def make_synthetic(n=3000, seed=7, with_time=False):
    """Trending-with-noise random walk. SMOKE TEST ONLY — not a performance claim."""
    rng = np.random.default_rng(seed)
    drift = np.concatenate([np.full(n // 3, 0.0006), np.full(n // 3, -0.0004), np.full(n - 2 * (n // 3), 0.0005)])
    rets = drift + rng.normal(0, 0.012, n)
    close = 30000 * np.exp(np.cumsum(rets))
    high = close * (1 + np.abs(rng.normal(0, 0.004, n)))
    low = close * (1 - np.abs(rng.normal(0, 0.004, n)))
    open_ = np.concatenate([[close[0]], close[:-1]])
    out = pd.DataFrame({"open": open_, "high": high, "low": low, "close": close})
    if with_time:
        end = pd.Timestamp.utcnow().floor("h")
        out["time"] = pd.date_range(end=end, periods=n, freq="4h")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv")
    ap.add_argument("--params")
    ap.add_argument("--demo", action="store_true")
    args = ap.parse_args()

    params = {}
    if args.params:
        with open(args.params) as f:
            params = json.load(f)

    if args.demo:
        df = make_synthetic(with_time=True)
        print("[smoke test on SYNTHETIC data — proves the engine runs, NOT a profit claim]\n")
    elif args.csv:
        df = load_csv(args.csv)
    else:
        print("Provide --csv <file> or --demo", file=sys.stderr)
        sys.exit(1)

    res = run_backtest(df, params)
    trades = res.pop("trades")
    res.pop("equity_curve", None)
    print(json.dumps(res, indent=2))
    print(f"\nLast {min(5, len(trades))} trades:")
    for t in trades[-5:]:
        print(f"  {t['side']}  entry={t['entry']:.2f}  exit={t['exit']:.2f}  pnl={t['pnl']:.2f}  {t.get('exit_time')}")


if __name__ == "__main__":
    main()

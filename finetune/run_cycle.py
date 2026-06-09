"""
run_cycle.py
============
One full finetune cycle for ONE OR MORE symbols, designed to be run on a schedule
(e.g. every 4 hours by GitHub Actions). For each symbol it:

  1. Gets fresh data (Binance public API, a --csv, or a --csv-dir).
  2. Backtests the CURRENT live params on all of it  -> "tracking" snapshot.
  3. Runs a walk-forward grid search (train -> out-of-sample test).
  4. Promotes the new params ONLY if they stay profitable out-of-sample.
  5. Appends a row to results/<SYMBOL>/history.csv and rewrites
     results/<SYMBOL>/REPORT.md (+ an equity-curve PNG if matplotlib is available).

After all symbols run, it writes a combined results/REPORT.md index.

It never deletes anything and never trades -- it only proposes/records.

Per-symbol params live in finetune/params/<SYMBOL>.json. If a symbol has no file
yet, the legacy finetune/params.json (or DEFAULT_PARAMS) is used as the seed.

Usage:
    python run_cycle.py --symbols BTCUSDT,ETHUSDT,ETCUSDT --interval 15m --limit 5000
    python run_cycle.py --symbol BTCUSDT --csv data/BTCUSDT_15m.csv       # single, local file
    python run_cycle.py --symbols BTCUSDT,ETHUSDT --csv-dir data          # local files per symbol
"""
import argparse
import csv
import datetime as dt
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from backtest import run_backtest, load_csv, DEFAULT_PARAMS  # noqa: E402
from optimize import grid_search, GRID, MIN_TRADES           # noqa: E402

RESULTS = os.path.join(ROOT, "results")
DATA = os.path.join(ROOT, "data")
PARAMS_DIR = os.path.join(HERE, "params")
LEGACY_PARAMS = os.path.join(HERE, "params.json")


# -- params helpers (per symbol, with legacy fallback) ------------------------
def params_path(symbol):
    return os.path.join(PARAMS_DIR, f"{symbol.upper()}.json")


def load_params(symbol):
    p = params_path(symbol)
    if os.path.exists(p):
        with open(p) as f:
            return json.load(f)
    if os.path.exists(LEGACY_PARAMS):
        with open(LEGACY_PARAMS) as f:
            return json.load(f)
    return {k: v for k, v in DEFAULT_PARAMS.items() if k != "initial_capital"}


def save_params(symbol, params):
    os.makedirs(PARAMS_DIR, exist_ok=True)
    with open(params_path(symbol), "w") as f:
        json.dump(params, f, indent=2)


# -- data --------------------------------------------------------------------
def get_data(symbol, args):
    if args.csv_dir:
        path = os.path.join(args.csv_dir, f"{symbol.upper()}_{args.interval}.csv")
        return load_csv(path)
    if args.csv:
        return load_csv(args.csv)
    from fetch_data import fetch_with_fallback
    df = fetch_with_fallback(symbol, args.interval, args.limit)
    os.makedirs(DATA, exist_ok=True)
    df.to_csv(os.path.join(DATA, f"{symbol.upper()}_{args.interval}.csv"), index=False)
    return df


def reconstruct_equity(trades, capital):
    eq, e = [capital], capital
    for t in trades:
        e += t["pnl"]
        eq.append(e)
    return eq


def write_curve(eq, path):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        plt.figure(figsize=(8, 3))
        plt.plot(eq, linewidth=1.5)
        plt.title("Equity (current params, full sample)")
        plt.xlabel("closed trade #")
        plt.ylabel("equity")
        plt.tight_layout()
        plt.savefig(path, dpi=110)
        plt.close()
        return True
    except Exception as e:  # noqa: BLE001
        print(f"[report] skipped equity curve: {e}")
        return False


def append_history(path, row):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    new = not os.path.exists(path)
    with open(path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(row.keys()))
        if new:
            w.writeheader()
        w.writerow(row)


def read_recent(path, n=10):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        rows = list(csv.DictReader(f))
    return rows[-n:]


def write_symbol_report(out_dir, symbol, interval, live, test_m, accepted, params, curve_ok):
    recent = read_recent(os.path.join(out_dir, "history.csv"), 10)
    lines = []
    lines.append(f"# Finetune report -- {symbol} {interval}")
    lines.append("")
    lines.append(f"_Last run (UTC): {dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M}_")
    lines.append("")
    lines.append("## Current params (live)")
    lines.append("")
    lines.append("```json")
    lines.append(json.dumps(params, indent=2))
    lines.append("```")
    lines.append("")
    lines.append("## Latest cycle")
    lines.append("")
    lines.append(f"- Current-params net profit (full sample): **{live['net_profit_pct']}%**, "
                 f"PF {live['profit_factor']}, {live['total_trades']} trades, "
                 f"max DD {live['max_drawdown']}")
    lines.append(f"- Optimizer out-of-sample: net **{test_m['net_profit_pct']}%**, "
                 f"PF {test_m['profit_factor']}, {test_m['total_trades']} trades")
    lines.append(f"- Decision: **{'PROMOTED new params' if accepted else 'kept current params'}**")
    lines.append("")
    if curve_ok:
        lines.append("![equity curve](equity_curve.png)")
        lines.append("")
    lines.append("## Recent runs")
    lines.append("")
    lines.append("| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |")
    lines.append("|---|---|---|---|---|---|---|")
    for r in recent:
        lines.append(f"| {r['timestamp']} | {r['data_bars']} | {r['live_net_pct']} | "
                     f"{r['live_pf']} | {r['oos_net_pct']} | {r['oos_pf']} | {r['accepted']} |")
    lines.append("")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "REPORT.md"), "w") as f:
        f.write("\n".join(lines))


def write_index_report(interval, summary):
    lines = []
    lines.append(f"# Finetune index -- {interval}")
    lines.append("")
    lines.append(f"_Last run (UTC): {dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M}_")
    lines.append("")
    lines.append("| symbol | bars | live net% | live PF | OOS net% | OOS PF | trades | accepted | report |")
    lines.append("|---|---|---|---|---|---|---|---|---|")
    for s in summary:
        lines.append(f"| {s['symbol']} | {s['bars']} | {s['live_net_pct']} | {s['live_pf']} | "
                     f"{s['oos_net_pct']} | {s['oos_pf']} | {s['oos_trades']} | {s['accepted']} | "
                     f"[{s['symbol']}]({s['symbol']}/REPORT.md) |")
    lines.append("")
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "REPORT.md"), "w") as f:
        f.write("\n".join(lines))


def run_one(symbol, args):
    df = get_data(symbol, args)
    if len(df) < 200:
        print(f"[{symbol}] Not enough data ({len(df)} bars). Increase --limit.", file=sys.stderr)
        return None

    out_dir = os.path.join(RESULTS, symbol.upper())
    os.makedirs(out_dir, exist_ok=True)
    current = load_params(symbol)
    capital = DEFAULT_PARAMS["initial_capital"]

    live = run_backtest(df, current)

    split = int(len(df) * args.train_frac)
    train = df.iloc[:split].reset_index(drop=True)
    test = df.iloc[split:].reset_index(drop=True)
    best_params, _ = grid_search(train, current)
    test_m = run_backtest(test, best_params)

    accepted = bool(test_m["net_profit"] > 0 and test_m["profit_factor"] > 1.0
                    and test_m["total_trades"] >= args.min_trades)

    if accepted:
        promoted = {k: v for k, v in best_params.items() if k != "initial_capital"}
        save_params(symbol, promoted)
        params_for_report = promoted
    else:
        params_for_report = {k: v for k, v in current.items() if k != "initial_capital"}

    curve_ok = write_curve(reconstruct_equity(live["trades"], capital),
                           os.path.join(out_dir, "equity_curve.png"))

    append_history(os.path.join(out_dir, "history.csv"), {
        "timestamp": f"{dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M}",
        "symbol": symbol, "interval": args.interval, "data_bars": len(df),
        "live_net_pct": live["net_profit_pct"], "live_pf": live["profit_factor"],
        "live_trades": live["total_trades"], "live_max_dd": live["max_drawdown"],
        "oos_net_pct": test_m["net_profit_pct"], "oos_pf": test_m["profit_factor"],
        "oos_trades": test_m["total_trades"], "accepted": accepted,
        "params": json.dumps({k: best_params[k] for k in GRID}),
    })
    write_symbol_report(out_dir, symbol, args.interval, live, test_m, accepted,
                        params_for_report, curve_ok)

    return {
        "symbol": symbol, "bars": len(df),
        "live_net_pct": live["net_profit_pct"], "live_pf": live["profit_factor"],
        "oos_net_pct": test_m["net_profit_pct"], "oos_pf": test_m["profit_factor"],
        "oos_trades": test_m["total_trades"], "accepted": accepted,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbols", default=None, help="comma-separated, e.g. BTCUSDT,ETHUSDT,ETCUSDT")
    ap.add_argument("--symbol", default=None, help="single symbol (alias for --symbols)")
    ap.add_argument("--interval", default="15m")
    ap.add_argument("--limit", type=int, default=5000)
    ap.add_argument("--csv", help="single local CSV (only valid with one symbol)")
    ap.add_argument("--csv-dir", dest="csv_dir", help="dir of <SYMBOL>_<interval>.csv files")
    ap.add_argument("--train-frac", type=float, default=0.7)
    ap.add_argument("--min-trades", type=int, default=MIN_TRADES)
    args = ap.parse_args()

    if args.symbols:
        symbols = [s.strip().upper() for s in args.symbols.split(",") if s.strip()]
    elif args.symbol:
        symbols = [args.symbol.strip().upper()]
    else:
        symbols = ["BTCUSDT", "ETHUSDT", "ETCUSDT"]

    if args.csv and len(symbols) > 1:
        print("--csv takes a single file; use --csv-dir for multiple symbols.", file=sys.stderr)
        sys.exit(2)

    os.makedirs(RESULTS, exist_ok=True)
    summary = []
    for sym in symbols:
        print(f"\n=== {sym} {args.interval} ===")
        try:
            row = run_one(sym, args)
        except Exception as e:  # noqa: BLE001
            print(f"[{sym}] cycle failed: {e}", file=sys.stderr)
            row = None
        if row:
            summary.append(row)
            print(json.dumps(row, indent=2))

    if summary:
        write_index_report(args.interval, summary)
    print(f"\n[done] {len(summary)}/{len(symbols)} symbols completed.")


if __name__ == "__main__":
    main()

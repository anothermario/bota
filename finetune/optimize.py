"""
optimize.py
===========
Walk-forward parameter finetuner for the KAMA Trend-Follower. This is the engine
the "strategy-finetune" skill runs on a 4-hour cadence.

It splits your data into an in-sample (train) window and an out-of-sample (test)
window, grid-searches parameters on train, then validates the winner on test.
A parameter set is only accepted if it ALSO performs out-of-sample -- this is the
single most important guard against curve-fitting.

Note on timeframe: the grid lengths are in BARS, not clock time. On 15m bars a
length of 20 is 5 hours; on 4h bars it was 80 hours. If you move timeframes,
revisit the grid (see TIMEFRAME_NOTE) rather than assuming the same numbers mean
the same thing.

Usage:
    python optimize.py --csv BTCUSDT_15m.csv --out params.json
    python optimize.py --demo --out params.json
"""
import argparse
import itertools
import json
import sys

import numpy as np

from backtest import run_backtest, load_csv, make_synthetic, DEFAULT_PARAMS

TIMEFRAME_NOTE = "grid lengths are in bars; rescale when changing timeframe"

# Keep the grid small so a 4-hour cadence stays fast. Widen only if you have time.
GRID = {
    "er_thresh": [0.25, 0.30, 0.35],
    "atr_mult": [2.5, 3.0, 3.5],
    "don_len": [15, 20, 30],
    "chand_len": [18, 22, 26],
}

MIN_TRADES = 15


def score(metrics):
    """Rank by risk-adjusted return; penalise tiny samples and ugly drawdowns."""
    if metrics["total_trades"] < MIN_TRADES:
        return -1e9
    dd = abs(metrics["max_drawdown"]) or 1.0
    return metrics["net_profit"] / dd + metrics["sharpe_like"] * 100


def grid_search(df, base):
    keys = list(GRID.keys())
    best, best_score = None, -1e18
    for combo in itertools.product(*[GRID[k] for k in keys]):
        params = {**base, **dict(zip(keys, combo))}
        m = run_backtest(df, params)
        s = score(m)
        if s > best_score:
            best_score, best = s, (params, m)
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv")
    ap.add_argument("--demo", action="store_true")
    ap.add_argument("--out", default="params.json")
    ap.add_argument("--train-frac", type=float, default=0.7)
    args = ap.parse_args()

    if args.demo:
        df = make_synthetic()
    elif args.csv:
        df = load_csv(args.csv)
    else:
        print("Provide --csv <file> or --demo", file=sys.stderr)
        sys.exit(1)

    split = int(len(df) * args.train_frac)
    train, test = df.iloc[:split].reset_index(drop=True), df.iloc[split:].reset_index(drop=True)

    params, train_m = grid_search(train, DEFAULT_PARAMS)
    test_m = run_backtest(test, params)

    accept = test_m["net_profit"] > 0 and test_m["profit_factor"] > 1.0 and test_m["total_trades"] >= MIN_TRADES
    report = {
        "best_params": {k: params[k] for k in GRID},
        "train": {k: train_m[k] for k in ("net_profit_pct", "profit_factor", "total_trades", "max_drawdown")},
        "test_out_of_sample": {k: test_m[k] for k in ("net_profit_pct", "profit_factor", "total_trades", "max_drawdown")},
        "accepted": bool(accept),
    }
    print(json.dumps(report, indent=2))

    if accept:
        full = {**DEFAULT_PARAMS, **params}
        full.pop("initial_capital", None)
        with open(args.out, "w") as f:
            json.dump(full, f, indent=2)
        print(f"\nAccepted. Wrote new params -> {args.out}")
        print("Copy these into the Pine strategy's Settings (or your alert/webhook config).")
    else:
        print("\nRejected: did not stay profitable out-of-sample. Keeping current params.")


if __name__ == "__main__":
    main()

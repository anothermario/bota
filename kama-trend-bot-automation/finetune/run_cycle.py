"""
run_cycle.py
============
One full finetune cycle, designed to be run on a schedule (e.g. every 4 hours by
GitHub Actions). It:

  1. Gets fresh data (Binance public API, or a --csv you pass).
  2. Backtests the CURRENT live params on all of it  -> "tracking" snapshot.
  3. Runs a walk-forward grid search (train -> out-of-sample test).
  4. Promotes the new params ONLY if they stay profitable out-of-sample.
  5. Appends a row to results/history.csv and rewrites results/REPORT.md
     (+ an equity-curve PNG if matplotlib is available).

It never deletes anything and never trades — it only proposes/records.

Usage:
    python run_cycle.py --symbol BTCUSDT --interval 4h --limit 1500
    python run_cycle.py --csv data/BTCUSDT_4h.csv      # use a local file instead
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
from optimize import grid_search, GRID                       # noqa: E402

RESULTS = os.path.join(ROOT, "results")
DATA = os.path.join(ROOT, "data")
PARAMS_PATH = os.path.join(HERE, "params.json")
HISTORY = os.path.join(RESULTS, "history.csv")
REPORT = os.path.join(RESULTS, "REPORT.md")
CURVE = os.path.join(RESULTS, "equity_curve.png")


def get_data(args):
    if args.csv:
        return load_csv(args.csv)
    from fetch_data import fetch_with_fallback
    df = fetch_with_fallback(args.symbol, args.interval, args.limit)
    os.makedirs(DATA, exist_ok=True)
    df.to_csv(os.path.join(DATA, f"{args.symbol}_{args.interval}.csv"), index=False)
    return df


def reconstruct_equity(trades, capital):
    eq, e = [capital], capital
    for t in trades:
        e += t["pnl"]
        eq.append(e)
    return eq


def write_curve(eq):
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
        plt.savefig(CURVE, dpi=110)
        plt.close()
        return True
    except Exception as e:  # noqa: BLE001
        print(f"[report] skipped equity curve: {e}")
        return False


def append_history(row):
    os.makedirs(RESULTS, exist_ok=True)
    new = not os.path.exists(HISTORY)
    with open(HISTORY, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(row.keys()))
        if new:
            w.writeheader()
        w.writerow(row)


def read_recent(n=10):
    if not os.path.exists(HISTORY):
        return []
    with open(HISTORY) as f:
        rows = list(csv.DictReader(f))
    return rows[-n:]


def write_report(symbol, interval, live, test_m, accepted, params, curve_ok):
    recent = read_recent(10)
    lines = []
    lines.append(f"# Finetune report — {symbol} {interval}")
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
    os.makedirs(RESULTS, exist_ok=True)
    with open(REPORT, "w") as f:
        f.write("\n".join(lines))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbol", default="BTCUSDT")
    ap.add_argument("--interval", default="4h")
    ap.add_argument("--limit", type=int, default=1500)
    ap.add_argument("--csv")
    ap.add_argument("--train-frac", type=float, default=0.7)
    ap.add_argument("--min-trades", type=int, default=15)
    args = ap.parse_args()

    df = get_data(args)
    os.makedirs(RESULTS, exist_ok=True)
    if len(df) < 200:
        print(f"Not enough data ({len(df)} bars). Increase --limit.", file=sys.stderr)
        sys.exit(1)

    with open(PARAMS_PATH) as f:
        current = json.load(f)

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
        with open(PARAMS_PATH, "w") as f:
            json.dump(promoted, f, indent=2)
        params_for_report = promoted
    else:
        params_for_report = {k: v for k, v in current.items() if k != "initial_capital"}

    curve_ok = write_curve(reconstruct_equity(live["trades"], capital))

    append_history({
        "timestamp": f"{dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M}",
        "symbol": args.symbol, "interval": args.interval, "data_bars": len(df),
        "live_net_pct": live["net_profit_pct"], "live_pf": live["profit_factor"],
        "live_trades": live["total_trades"], "live_max_dd": live["max_drawdown"],
        "oos_net_pct": test_m["net_profit_pct"], "oos_pf": test_m["profit_factor"],
        "oos_trades": test_m["total_trades"], "accepted": accepted,
        "params": json.dumps({k: best_params[k] for k in GRID}),
    })
    write_report(args.symbol, args.interval, live, test_m, accepted, params_for_report, curve_ok)

    print(json.dumps({
        "accepted": accepted,
        "live_net_pct": live["net_profit_pct"],
        "oos_net_pct": test_m["net_profit_pct"],
        "oos_pf": test_m["profit_factor"],
    }, indent=2))


if __name__ == "__main__":
    main()

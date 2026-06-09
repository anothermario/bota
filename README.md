# Adaptive KAMA Trend-Follower — crypto trend-following kit

A trend-following trading system built around a single Pine Script v6 TradingView
strategy, plus an offline, **multi-symbol** finetuning loop that runs on a
**4-hour cadence** against **15m** data.

## What's in the box
```
kama-trend-bot/
├── kama_trend_follower.pine        # the TradingView strategy (paste into Pine editor)
├── finetune/
│   ├── backtest.py                 # offline backtester, mirrors Pine logic, 0.04% fee
│   ├── optimize.py                 # walk-forward parameter finetuner
│   ├── fetch_data.py               # pulls Binance public klines into a CSV
│   ├── run_cycle.py                # one scheduled cycle over one or more symbols
│   ├── params.json                 # legacy/template param set (seed for new symbols)
│   └── params/                     # per-symbol live params: <SYMBOL>.json
└── results/
    ├── REPORT.md                   # combined index across symbols
    └── <SYMBOL>/                   # per-symbol REPORT.md, history.csv, equity_curve.png
```

## Timeframe vs cadence (read this first)
- **Timeframe = 15m**: the bars the strategy trades on.
- **Cadence = every 4 hours**: how often the finetune loop re-checks/optimizes.

These are independent. The 4-hour cadence did **not** change; only the data
timeframe moved from 4h to 15m.

> ⚠️ The strategy's lengths (`er_len`, `kama_slow`, `don_len`, `chand_len`, …) are
> in **bars, not clock time**. On 15m, the old 4h-tuned numbers cover ~1/16th of
> the calendar window they used to — so the strategy is now much faster, trades
> far more often, and is **much more fee-sensitive** (0.04%/fill compounds with
> trade count). Let the walk-forward optimizer re-fit them per symbol; don't
> assume the 4h defaults are still appropriate.

## 1. Run the strategy on TradingView
1. Open TradingView → a crypto chart on the **15m** timeframe (e.g. BINANCE:BTCUSDT).
2. Open the **Pine Editor**, paste `kama_trend_follower.pine`, click **Add to chart**.
3. The Strategy Tester + on-chart dashboard show performance; commission is set to
   **0.04% per fill** inside `strategy(...)`.
4. The Pine inputs map name-for-name to the keys in `finetune/params/<SYMBOL>.json`.

## 2. Going live (optional)
Pine cannot place Binance orders. Add alerts on the "Long Signal"/"Short Signal"
conditions and point the webhook at your own execution service. The script emits
signals; you own execution. **This is not financial advice.**

## 3. Finetune locally (multi-symbol)
```bash
cd finetune
# fetch + optimize + report for several coins at once
python run_cycle.py --symbols BTCUSDT,ETHUSDT,ETCUSDT --interval 15m --limit 5000

# or a single symbol from a local CSV
python run_cycle.py --symbol BTCUSDT --csv data/BTCUSDT_15m.csv
```
Accepted params land in `finetune/params/<SYMBOL>.json`; copy them into the Pine
strategy's Settings → Inputs (per symbol). Rejected candidates are discarded and
the current params stay put.

Quick smoke test without your own data:
```bash
python backtest.py --demo
python optimize.py --demo --out /tmp/p.json
```

## Automated workflow (GitHub Actions)
- `.github/workflows/finetune.yml` — runs every 4 hours (and on-demand) for the
  symbol list, then commits `results/`, `data/`, and `finetune/params/` back.
- One-time: **Settings → Actions → General → Workflow permissions → Read and
  write**, then enable workflows. Trigger a first run from the **Actions** tab
  (you can override symbols/interval/limit there).

## Honest expectations
- The design is meant to be robust (regime filter, adaptive baseline, ATR risk
  sizing, trailing exits) and the backtester includes fees — but **no strategy is
  guaranteed to be profitable**, and past results don't guarantee future ones.
- A 15m trend-follower lives or dies on fee/slippage realism. The backtester only
  models the 0.04% maker/taker-style fee; it does **not** model slippage, funding,
  or partial fills, which matter more at higher trade frequency. Treat the numbers
  as optimistic.
- Validate on *your* market/timeframe before risking money. Start in paper trading.
- This is not financial advice.

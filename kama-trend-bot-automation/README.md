# Adaptive KAMA Trend-Follower — crypto trend-following kit

A complete trend-following trading system built around a single Pine Script v6
TradingView strategy, plus an offline finetuning loop.

## What's in the box
```
kama-trend-bot/
├── kama_trend_follower.pine        # the TradingView strategy (paste into Pine editor)
├── finetune/
│   ├── backtest.py                 # offline backtester, mirrors Pine logic, 0.04% fee
│   ├── optimize.py                 # walk-forward parameter finetuner
│   └── params.json                 # current parameter set (maps to Pine inputs)
└── skills/
    └── strategy-finetune/
        └── SKILL.md                # the 4-hour readaptation workflow
```

## 1. Run the strategy on TradingView
1. Open TradingView → any crypto chart (e.g. BINANCE:BTCUSDT, 4h).
2. Open the **Pine Editor**, paste the contents of `kama_trend_follower.pine`,
   click **Add to chart**.
3. The **Strategy Tester** panel shows full performance; the on-chart **dashboard**
   (top-right) shows live net profit, win rate, profit factor, drawdown, position
   and regime; the **trade-history table** (bottom-right) shows your last N trades
   colour-coded green/red.
4. Commission is already set to **0.04% per trade** inside `strategy(...)`.

## 2. Going live (optional)
Pine itself cannot place Binance orders. To trade live: right-click the
strategy → **Add alert** on the "Long Signal" / "Short Signal" conditions →
point the alert webhook at an execution service (e.g. your own bot, or a
TradingView→Binance bridge). The script only emits signals; you own the
execution layer.

## 3. Finetune every 4 hours
```bash
cd finetune
python optimize.py --csv your_data.csv --out params.json
```
Then copy the values from `params.json` into the strategy's Settings → Inputs.
See `skills/strategy-finetune/SKILL.md` for the full scheduled loop and the
anti-overfitting guardrails. Schedule it with cron (`0 */4 * * *`).

Quick smoke test without your own data:
```bash
python backtest.py --demo
python optimize.py --demo --out /tmp/p.json
```

## Honest expectations
- I designed this to be robust (regime filter, adaptive baseline, ATR risk
  sizing, trailing exits) and the backtester includes fees — but **no strategy is
  guaranteed to be profitable**, and past results don't guarantee future ones.
- Validate on *your* market/timeframe before risking money. Start in paper trading.
- This is not financial advice.
```

---

## Automated workflow (GitHub Actions)

The repo runs itself on a schedule. Files involved:
- `.github/workflows/finetune.yml` — runs every 4 hours (and on-demand).
- `finetune/fetch_data.py` — pulls Binance public klines into a CSV.
- `finetune/run_cycle.py` — backtests current params, walk-forward optimizes,
  promotes params only if they survive out-of-sample, and writes `results/`.
- `results/REPORT.md`, `results/history.csv`, `results/equity_curve.png` —
  the tracked, version-controlled record of every cycle.

### One-time setup
1. Add the files above to the repo (keep the paths).
2. On GitHub: **Settings → Actions → General → Workflow permissions →
   "Read and write permissions"** (lets the workflow commit results back).
3. **Actions** tab → enable workflows if prompted.
4. Trigger a first run: **Actions → "Finetune & Backtest" → Run workflow**
   (pick symbol/interval), or just wait for the next 4-hour slot.

### What you get each cycle
A new commit on the repo containing the latest `results/REPORT.md` (rendered
nicely on GitHub), an appended row in `results/history.csv`, and a refreshed
equity-curve image. Param changes only land when they pass the out-of-sample
guardrail; otherwise the current params stay put.

### Run it locally (same thing, no Actions)
```bash
cd finetune
python run_cycle.py --symbol BTCUSDT --interval 4h --limit 1500
```

### Notes
- Scheduled GitHub workflows can be delayed a few minutes under load, and GitHub
  pauses schedules on repos with no commits for 60 days — the auto-commits keep it alive.
- `data-api.binance.vision` is used first because the main Binance host is
  geo-blocked on some cloud IPs.

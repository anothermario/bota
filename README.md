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

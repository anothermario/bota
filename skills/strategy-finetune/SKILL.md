---
name: strategy-finetune
description: >-
  Re-optimize and finetune the KAMA Trend-Follower crypto strategy on a recurring
  (every-4-hours) cadence using walk-forward validation, across one or more
  symbols on a 15m timeframe. Use this skill whenever the user wants to readapt,
  retune, re-optimize, refit, or refresh a trading strategy's parameters against
  fresh market data; whenever they mention a scheduled/cron/4-hour optimization
  loop for a TradingView or Pine Script strategy; or whenever they ask to validate
  that a strategy still works on recent OHLCV data. Always use this skill before
  changing live trading parameters -- never hand-tune live params without an
  out-of-sample check.
---

# Strategy Finetune (4-hour readaptation loop, 15m data, multi-symbol)

Keeps the **Adaptive KAMA Trend-Follower** honest as the market drifts. It re-fits
parameters on recent data using **walk-forward validation** and only promotes a
change if it survives out-of-sample. Timeframe (15m) and cadence (every 4h) are
independent: the *loop* runs 4-hourly; the *bars* are 15m.

> Reality check: a Pine strategy can't rewrite itself. "Adapting" means (1) the
> KAMA engine adapts bar-by-bar inside Pine, and (2) this loop re-fits the tunable
> params offline and you push winners into Settings. This skill is loop (2).

> 15m caveat: param lengths are in **bars**, not time. The 4h-era defaults cover
> ~1/16th of the calendar window on 15m, so the strategy trades far more often and
> is much more fee-sensitive. Let the optimizer re-fit; don't trust old defaults.

## Files this skill drives
- `finetune/backtest.py` — engine that mirrors Pine 1:1 (0.04%/fill; entry+exit
  charged once each).
- `finetune/optimize.py` — walk-forward grid search; OOS gate (net>0, PF>1, >=15 trades).
- `finetune/fetch_data.py` — Binance public klines → CSV (15m default).
- `finetune/run_cycle.py` — runs the whole cycle over a symbol list.
- `finetune/params/<SYMBOL>.json` — the current live params, **per symbol**.

## When it runs
Every 4 hours (cron `0 */4 * * *`), via GitHub Actions or any scheduler.

## The cycle — do these steps in order
1. **Get fresh data** for each symbol/timeframe (15m). Use enough history that the
   out-of-sample slice still holds several hundred bars (5000 x 15m ~= 52 days).
2. **Run the cycle:**
   ```bash
   python run_cycle.py --symbols BTCUSDT,ETHUSDT,ETCUSDT --interval 15m --limit 5000
   ```
   It grid-searches train (70%) and validates on test (30%), per symbol.
3. **Guardrails (enforced; confirm them):** reject if OOS net ≤ 0, OOS PF ≤ 1.0,
   or OOS trades < 15. Prefer the smallest change that clears the bar; big
   in-sample wins that fade out-of-sample are overfitting.
4. **Promote only if accepted.** Winners are written to `params/<SYMBOL>.json` and
   logged in `results/<SYMBOL>/history.csv`. Otherwise current params stay.
5. **Push to the live strategy.** Copy `params/<SYMBOL>.json` into the Pine
   Settings → Inputs for that symbol's chart (and/or your webhook config).
6. **Log and stop.** Never trade a rejected candidate. Three straight rejections =
   regime change; flag for human review rather than loosening guardrails.

## Anti-overfitting rules (non-negotiable)
- Out-of-sample is the judge, never in-sample.
- Keep the grid small; a giant grid finds noise. On 15m, watch fee drag.
- Don't re-run until you get the answer you want.
- Past backtest profit ≠ future profit. This loop reduces self-deception; it does
  not remove market risk.

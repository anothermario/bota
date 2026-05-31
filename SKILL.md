---
name: strategy-finetune
description: >-
  Re-optimize and finetune the KAMA Trend-Follower crypto strategy on a recurring
  (e.g. every-4-hours) cadence using walk-forward validation. Use this skill
  whenever the user wants to readapt, retune, re-optimize, refit, or refresh a
  trading strategy's parameters against fresh market data; whenever they mention
  a scheduled/cron/4-hour optimization loop for a TradingView or Pine Script
  strategy; or whenever they ask to validate that a strategy still works on
  recent OHLCV data. Always use this skill before changing live trading
  parameters — never hand-tune live params without an out-of-sample check.
---

# Strategy Finetune (4-hour readaptation loop)

This skill keeps the **Adaptive KAMA Trend-Follower** honest as the market drifts.
It re-fits the strategy's parameters on recent data using **walk-forward
validation** and only promotes a change if it survives out-of-sample.

> Reality check: A Pine Script strategy on TradingView cannot rewrite itself.
> "Self-adapting every 4 hours" is implemented two ways: (1) the strategy's KAMA
> engine adapts bar-by-bar on its own inside Pine, and (2) this skill re-fits the
> *tunable* parameters offline on a schedule and you push the winners into the
> strategy's Settings (or your alert/webhook config). This skill is that second loop.

## Files this skill drives
- `finetune/backtest.py` — engine that mirrors the Pine logic 1:1 (0.04% fee included).
- `finetune/optimize.py` — walk-forward grid search; writes accepted params to `params.json`.
- `finetune/params.json` — the current live parameter set.

## When it runs
On a 4-hour cadence (or whatever the user sets). Schedule it with cron, a
systemd timer, Task Scheduler, or a cloud scheduler. Example cron line:

```
0 */4 * * *  cd /path/to/kama-trend-bot/finetune && /usr/bin/python3 run_cycle.sh >> finetune.log 2>&1
```

## The cycle — do these steps in order

1. **Get fresh data.** Pull the most recent OHLCV for the traded symbol/timeframe
   (export from TradingView, or pull from Binance's public klines endpoint into a
   CSV with columns: time, open, high, low, close). Use enough history that the
   out-of-sample slice still holds several hundred bars.

2. **Run the walk-forward optimizer:**
   ```bash
   python optimize.py --csv <fresh_data>.csv --out params.candidate.json --train-frac 0.7
   ```
   It grid-searches on the first 70% (train) and validates on the last 30% (test).

3. **Apply the guardrails (the optimizer enforces these; confirm them):**
   - Reject if out-of-sample net profit ≤ 0.
   - Reject if out-of-sample profit factor ≤ 1.0.
   - Reject if total trades < 15 (sample too small to trust).
   - Prefer the smallest parameter change that clears the bar — do not chase the
     highest in-sample number. Big in-sample wins that fade out-of-sample are
     overfitting and must be discarded.

4. **Promote only if accepted.** If `optimize.py` wrote a new file, diff it against
   the live `params.json`. If the change is accepted AND meaningfully better
   out-of-sample, replace `params.json` and record the decision in `finetune.log`
   (timestamp, old params, new params, OOS metrics). Otherwise keep current params.

5. **Push to the live strategy.** Open the values from `params.json` into the Pine
   strategy's **Settings → Inputs** on TradingView (and/or your webhook bot's
   config). The Pine inputs map name-for-name to the keys in `params.json`.

6. **Log and stop.** Never trade on a rejected candidate. If three consecutive
   cycles reject, that is a signal the regime changed — flag it for human review
   rather than loosening the guardrails.

## Anti-overfitting rules (non-negotiable)
- Out-of-sample is the judge, never in-sample.
- Keep the search grid small; a giant grid finds noise.
- Don't re-run until you get the answer you want.
- Past backtest profit does not guarantee future profit. This loop reduces the
  odds of self-deception; it does not eliminate market risk.

## Helper script to bundle the cycle
Create `finetune/run_cycle.sh` (the user supplies the data step for their broker):

```bash
#!/usr/bin/env bash
set -euo pipefail
DATA="latest.csv"          # produced by your data-fetch step
python optimize.py --csv "$DATA" --out params.candidate.json --train-frac 0.7
# promotion logic: optimize.py only writes the file when accepted
if [ -f params.candidate.json ]; then
  cp params.json "params.$(date +%Y%m%d_%H%M%S).bak"
  mv params.candidate.json params.json
  echo "$(date -u) promoted new params"
fi
```

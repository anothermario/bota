# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-26 00:15_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.35,
  "use_adx": true,
  "adx_len": 14,
  "adx_thresh": 20.0,
  "don_len": 30,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 26,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-3.93%**, PF 0.8, 50 trades, max DD -1029.0
- Optimizer out-of-sample: net **6.29%**, PF 2.571, 16 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-24 12:10 | 5000 | -3.26 | 0.832 | 7.3 | 3.449 | True |
| 2026-08-24 16:12 | 5000 | -3.26 | 0.832 | 7.3 | 3.449 | True |
| 2026-08-24 20:08 | 5000 | -2.32 | 0.875 | 7.3 | 3.449 | True |
| 2026-08-25 00:14 | 5000 | -2.34 | 0.874 | 7.3 | 3.449 | True |
| 2026-08-25 04:15 | 5000 | -2.35 | 0.874 | 7.28 | 3.449 | True |
| 2026-08-25 08:16 | 5000 | -2.99 | 0.845 | 6.55 | 2.759 | True |
| 2026-08-25 12:11 | 5000 | -2.99 | 0.845 | 6.55 | 2.759 | True |
| 2026-08-25 16:14 | 5000 | -2.37 | 0.878 | 6.7 | 2.864 | True |
| 2026-08-25 20:07 | 5000 | -3.02 | 0.843 | 6.7 | 2.864 | True |
| 2026-08-26 00:15 | 5000 | -3.93 | 0.8 | 6.29 | 2.571 | True |

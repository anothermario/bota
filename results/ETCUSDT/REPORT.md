# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-10 02:56_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.25,
  "use_adx": true,
  "adx_len": 14,
  "adx_thresh": 20.0,
  "don_len": 15,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 18,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-12.38%**, PF 0.535, 71 trades, max DD -1238.49
- Optimizer out-of-sample: net **-5.74%**, PF 0.262, 16 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-08 14:03 | 5000 | -13.03 | 0.521 | -5.87 | 0.335 | False |
| 2026-07-08 17:28 | 5000 | -12.99 | 0.521 | -6.57 | 0.309 | False |
| 2026-07-08 21:07 | 5000 | -12.8 | 0.526 | -5.81 | 0.336 | False |
| 2026-07-09 02:54 | 5000 | -12.8 | 0.526 | -5.79 | 0.339 | False |
| 2026-07-09 07:41 | 5000 | -12.47 | 0.533 | -5.71 | 0.308 | False |
| 2026-07-09 10:53 | 5000 | -12.47 | 0.533 | -5.93 | 0.3 | False |
| 2026-07-09 14:56 | 5000 | -12.47 | 0.533 | -5.98 | 0.297 | False |
| 2026-07-09 17:55 | 5000 | -13.06 | 0.52 | -5.66 | 0.311 | False |
| 2026-07-09 21:22 | 5000 | -12.37 | 0.535 | -5.32 | 0.327 | False |
| 2026-07-10 02:56 | 5000 | -12.38 | 0.535 | -5.74 | 0.262 | False |

# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-26 20:10_

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
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-13.86%**, PF 0.51, 98 trades, max DD -1564.4
- Optimizer out-of-sample: net **-3.33%**, PF 0.594, 29 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-25 08:16 | 5000 | -13.4 | 0.517 | -3.56 | 0.575 | False |
| 2026-09-25 12:17 | 5000 | -13.55 | 0.516 | -4.54 | 0.515 | False |
| 2026-09-25 16:13 | 5000 | -13.55 | 0.516 | -4.54 | 0.515 | False |
| 2026-09-25 20:10 | 5000 | -13.55 | 0.516 | -4.46 | 0.519 | False |
| 2026-09-26 00:30 | 5000 | -14.14 | 0.504 | -3.67 | 0.57 | False |
| 2026-09-26 04:12 | 5000 | -14.57 | 0.495 | -3.67 | 0.57 | False |
| 2026-09-26 08:15 | 5000 | -13.95 | 0.508 | -3.67 | 0.57 | False |
| 2026-09-26 12:15 | 5000 | -12.9 | 0.537 | -3.66 | 0.571 | False |
| 2026-09-26 16:11 | 5000 | -13.87 | 0.51 | -3.34 | 0.593 | False |
| 2026-09-26 20:10 | 5000 | -13.86 | 0.51 | -3.33 | 0.594 | False |

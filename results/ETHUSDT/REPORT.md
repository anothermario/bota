# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-26 08:15_

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

- Current-params net profit (full sample): **-13.95%**, PF 0.508, 99 trades, max DD -1572.9
- Optimizer out-of-sample: net **-3.67%**, PF 0.57, 30 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-24 20:12 | 5000 | -14.12 | 0.502 | -3.72 | 0.564 | False |
| 2026-09-25 00:31 | 5000 | -13.4 | 0.517 | -3.72 | 0.564 | False |
| 2026-09-25 04:14 | 5000 | -13.4 | 0.517 | -4.31 | 0.525 | False |
| 2026-09-25 08:16 | 5000 | -13.4 | 0.517 | -3.56 | 0.575 | False |
| 2026-09-25 12:17 | 5000 | -13.55 | 0.516 | -4.54 | 0.515 | False |
| 2026-09-25 16:13 | 5000 | -13.55 | 0.516 | -4.54 | 0.515 | False |
| 2026-09-25 20:10 | 5000 | -13.55 | 0.516 | -4.46 | 0.519 | False |
| 2026-09-26 00:30 | 5000 | -14.14 | 0.504 | -3.67 | 0.57 | False |
| 2026-09-26 04:12 | 5000 | -14.57 | 0.495 | -3.67 | 0.57 | False |
| 2026-09-26 08:15 | 5000 | -13.95 | 0.508 | -3.67 | 0.57 | False |

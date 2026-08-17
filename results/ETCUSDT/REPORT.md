# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-17 20:07_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.3,
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

- Current-params net profit (full sample): **-14.51%**, PF 0.368, 57 trades, max DD -1451.36
- Optimizer out-of-sample: net **-4.0%**, PF 0.249, 14 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-16 08:08 | 5000 | -16.11 | 0.322 | -3.48 | 0.29 | False |
| 2026-08-16 12:07 | 5000 | -15.12 | 0.339 | -1.68 | 0.618 | False |
| 2026-08-16 16:05 | 5000 | -15.03 | 0.341 | -2.07 | 0.561 | False |
| 2026-08-16 20:05 | 5000 | -15.05 | 0.341 | -2.55 | 0.467 | False |
| 2026-08-17 00:14 | 5000 | -14.76 | 0.364 | -3.28 | 0.398 | False |
| 2026-08-17 04:17 | 5000 | -15.25 | 0.356 | -5.47 | 0.193 | False |
| 2026-08-17 08:15 | 5000 | -15.26 | 0.356 | -5.47 | 0.193 | False |
| 2026-08-17 12:08 | 5000 | -14.45 | 0.371 | -4.0 | 0.249 | False |
| 2026-08-17 16:06 | 5000 | -14.98 | 0.359 | -4.0 | 0.249 | False |
| 2026-08-17 20:07 | 5000 | -14.51 | 0.368 | -4.0 | 0.249 | False |

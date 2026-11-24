# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-11-24 00:18_

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

- Current-params net profit (full sample): **-13.0%**, PF 0.49, 66 trades, max DD -1317.22
- Optimizer out-of-sample: net **-6.43%**, PF 0.441, 29 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-22 12:09 | 5000 | -13.13 | 0.491 | -6.48 | 0.388 | False |
| 2026-11-22 16:07 | 5000 | -13.24 | 0.488 | -6.55 | 0.385 | False |
| 2026-11-22 20:07 | 5000 | -13.24 | 0.488 | -6.55 | 0.385 | False |
| 2026-11-23 00:21 | 5000 | -13.77 | 0.477 | -6.58 | 0.385 | False |
| 2026-11-23 04:09 | 5000 | -13.43 | 0.485 | -7.11 | 0.365 | False |
| 2026-11-23 08:11 | 5000 | -13.43 | 0.485 | -7.11 | 0.365 | False |
| 2026-11-23 12:12 | 5000 | -13.74 | 0.472 | -6.82 | 0.376 | False |
| 2026-11-23 16:07 | 5000 | -13.0 | 0.49 | -6.39 | 0.415 | False |
| 2026-11-23 20:07 | 5000 | -13.0 | 0.49 | -6.97 | 0.394 | False |
| 2026-11-24 00:18 | 5000 | -13.0 | 0.49 | -6.43 | 0.441 | False |

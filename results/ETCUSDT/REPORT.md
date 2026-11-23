# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-11-23 04:09_

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

- Current-params net profit (full sample): **-13.43%**, PF 0.485, 67 trades, max DD -1374.35
- Optimizer out-of-sample: net **-7.11%**, PF 0.365, 27 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-21 16:07 | 5000 | -12.8 | 0.492 | -6.25 | 0.385 | False |
| 2026-11-21 20:07 | 5000 | -12.8 | 0.492 | -6.27 | 0.384 | False |
| 2026-11-22 00:21 | 5000 | -12.27 | 0.507 | -5.68 | 0.431 | False |
| 2026-11-22 04:08 | 5000 | -12.3 | 0.507 | -5.51 | 0.449 | False |
| 2026-11-22 08:09 | 5000 | -13.11 | 0.491 | -6.74 | 0.377 | False |
| 2026-11-22 12:09 | 5000 | -13.13 | 0.491 | -6.48 | 0.388 | False |
| 2026-11-22 16:07 | 5000 | -13.24 | 0.488 | -6.55 | 0.385 | False |
| 2026-11-22 20:07 | 5000 | -13.24 | 0.488 | -6.55 | 0.385 | False |
| 2026-11-23 00:21 | 5000 | -13.77 | 0.477 | -6.58 | 0.385 | False |
| 2026-11-23 04:09 | 5000 | -13.43 | 0.485 | -7.11 | 0.365 | False |

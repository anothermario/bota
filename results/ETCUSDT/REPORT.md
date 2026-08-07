# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-07 20:15_

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

- Current-params net profit (full sample): **-16.43%**, PF 0.419, 68 trades, max DD -1657.7
- Optimizer out-of-sample: net **-1.34%**, PF 0.815, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-06 05:05 | 5000 | -13.93 | 0.493 | -3.06 | 0.668 | False |
| 2026-08-06 08:59 | 5000 | -14.86 | 0.453 | -2.54 | 0.69 | False |
| 2026-08-06 12:41 | 5000 | -15.71 | 0.429 | -2.54 | 0.692 | False |
| 2026-08-06 21:58 | 5000 | -16.27 | 0.42 | -2.86 | 0.667 | False |
| 2026-08-07 01:16 | 5000 | -16.19 | 0.423 | -2.67 | 0.685 | False |
| 2026-08-07 04:41 | 5000 | -16.42 | 0.419 | -1.86 | 0.759 | False |
| 2026-08-07 08:26 | 5000 | -15.62 | 0.434 | -1.68 | 0.777 | False |
| 2026-08-07 12:19 | 5000 | -15.02 | 0.445 | -1.3 | 0.819 | False |
| 2026-08-07 16:19 | 5000 | -15.76 | 0.431 | -1.28 | 0.822 | False |
| 2026-08-07 20:15 | 5000 | -16.43 | 0.419 | -1.34 | 0.815 | False |

# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-11 16:12_

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

- Current-params net profit (full sample): **-16.78%**, PF 0.4, 99 trades, max DD -1687.76
- Optimizer out-of-sample: net **-5.61%**, PF 0.433, 27 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-10 04:13 | 5000 | -14.51 | 0.442 | -4.18 | 0.458 | False |
| 2026-09-10 08:15 | 5000 | -14.95 | 0.434 | -4.02 | 0.471 | False |
| 2026-09-10 12:16 | 5000 | -14.95 | 0.436 | -4.71 | 0.429 | False |
| 2026-09-10 16:11 | 5000 | -15.03 | 0.434 | -4.92 | 0.419 | False |
| 2026-09-10 20:10 | 5000 | -15.07 | 0.433 | -3.89 | 0.487 | False |
| 2026-09-11 00:31 | 5000 | -16.42 | 0.39 | -4.37 | 0.458 | False |
| 2026-09-11 04:14 | 5000 | -16.51 | 0.388 | -4.37 | 0.458 | False |
| 2026-09-11 08:15 | 5000 | -17.0 | 0.382 | -4.91 | 0.428 | False |
| 2026-09-11 12:17 | 5000 | -16.96 | 0.384 | -5.23 | 0.347 | False |
| 2026-09-11 16:12 | 5000 | -16.78 | 0.4 | -5.61 | 0.433 | False |

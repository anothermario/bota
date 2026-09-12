# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-12 12:14_

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

- Current-params net profit (full sample): **-17.1%**, PF 0.396, 99 trades, max DD -1710.09
- Optimizer out-of-sample: net **-5.7%**, PF 0.43, 27 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-11 00:31 | 5000 | -16.42 | 0.39 | -4.37 | 0.458 | False |
| 2026-09-11 04:14 | 5000 | -16.51 | 0.388 | -4.37 | 0.458 | False |
| 2026-09-11 08:15 | 5000 | -17.0 | 0.382 | -4.91 | 0.428 | False |
| 2026-09-11 12:17 | 5000 | -16.96 | 0.384 | -5.23 | 0.347 | False |
| 2026-09-11 16:12 | 5000 | -16.78 | 0.4 | -5.61 | 0.433 | False |
| 2026-09-11 20:11 | 5000 | -16.71 | 0.402 | -5.57 | 0.434 | False |
| 2026-09-12 00:29 | 5000 | -16.81 | 0.4 | -5.59 | 0.434 | False |
| 2026-09-12 04:12 | 5000 | -16.54 | 0.405 | -6.47 | 0.396 | False |
| 2026-09-12 08:13 | 5000 | -16.65 | 0.403 | -6.32 | 0.403 | False |
| 2026-09-12 12:14 | 5000 | -17.1 | 0.396 | -5.7 | 0.43 | False |

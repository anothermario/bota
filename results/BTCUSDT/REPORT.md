# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-29 20:54_

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
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-15.79%**, PF 0.395, 72 trades, max DD -1677.28
- Optimizer out-of-sample: net **-6.95%**, PF 0.241, 25 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-28 10:33 | 5000 | -15.76 | 0.41 | -6.59 | 0.343 | False |
| 2026-07-28 14:03 | 5000 | -15.76 | 0.41 | -6.59 | 0.343 | False |
| 2026-07-28 17:25 | 5000 | -15.37 | 0.427 | -6.14 | 0.359 | False |
| 2026-07-28 21:06 | 5000 | -15.74 | 0.411 | -7.05 | 0.327 | False |
| 2026-07-29 02:31 | 5000 | -16.74 | 0.377 | -4.97 | 0.412 | False |
| 2026-07-29 06:29 | 5000 | -16.33 | 0.384 | -4.97 | 0.412 | False |
| 2026-07-29 10:37 | 5000 | -16.36 | 0.385 | -5.01 | 0.412 | False |
| 2026-07-29 14:07 | 5000 | -15.79 | 0.395 | -5.35 | 0.394 | False |
| 2026-07-29 17:13 | 5000 | -15.79 | 0.395 | -5.79 | 0.376 | False |
| 2026-07-29 20:54 | 5000 | -15.79 | 0.395 | -6.95 | 0.241 | False |

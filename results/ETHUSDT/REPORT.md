# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-06-11 20:52_

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
  "don_len": 20,
  "atr_len": 14,
  "atr_mult": 3.0,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-16.3%**, PF 0.385, 87 trades, max DD -1637.52
- Optimizer out-of-sample: net **-6.82%**, PF 0.389, 29 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-10 09:19 | 5000 | -16.64 | 0.375 | -6.35 | 0.414 | False |
| 2026-06-10 13:16 | 5000 | -16.03 | 0.386 | -6.69 | 0.401 | False |
| 2026-06-10 17:09 | 5000 | -16.91 | 0.373 | -6.69 | 0.402 | False |
| 2026-06-10 20:57 | 5000 | -16.86 | 0.374 | -7.3 | 0.382 | False |
| 2026-06-11 00:55 | 5000 | -16.86 | 0.374 | -6.18 | 0.424 | False |
| 2026-06-11 05:39 | 5000 | -16.41 | 0.382 | -6.53 | 0.39 | False |
| 2026-06-11 09:34 | 5000 | -16.41 | 0.382 | -6.53 | 0.39 | False |
| 2026-06-11 13:24 | 5000 | -16.31 | 0.385 | -7.24 | 0.364 | False |
| 2026-06-11 17:19 | 5000 | -16.31 | 0.385 | -7.25 | 0.363 | False |
| 2026-06-11 20:52 | 5000 | -16.3 | 0.385 | -6.82 | 0.389 | False |

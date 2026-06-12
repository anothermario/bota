# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-06-12 17:03_

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

- Current-params net profit (full sample): **-15.72%**, PF 0.408, 87 trades, max DD -1656.46
- Optimizer out-of-sample: net **-6.52%**, PF 0.391, 27 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-11 05:39 | 5000 | -16.41 | 0.382 | -6.53 | 0.39 | False |
| 2026-06-11 09:34 | 5000 | -16.41 | 0.382 | -6.53 | 0.39 | False |
| 2026-06-11 13:24 | 5000 | -16.31 | 0.385 | -7.24 | 0.364 | False |
| 2026-06-11 17:19 | 5000 | -16.31 | 0.385 | -7.25 | 0.363 | False |
| 2026-06-11 20:52 | 5000 | -16.3 | 0.385 | -6.82 | 0.389 | False |
| 2026-06-12 00:58 | 5000 | -16.12 | 0.389 | -5.97 | 0.447 | False |
| 2026-06-12 05:38 | 5000 | -16.12 | 0.389 | -6.15 | 0.441 | False |
| 2026-06-12 09:29 | 5000 | -16.12 | 0.389 | -6.67 | 0.385 | False |
| 2026-06-12 13:14 | 5000 | -16.13 | 0.389 | -6.76 | 0.382 | False |
| 2026-06-12 17:03 | 5000 | -15.72 | 0.408 | -6.52 | 0.391 | False |

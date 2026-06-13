# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-06-13 12:41_

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

- Current-params net profit (full sample): **-15.96%**, PF 0.384, 85 trades, max DD -1595.59
- Optimizer out-of-sample: net **-3.44%**, PF 0.538, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-12 00:58 | 5000 | -16.12 | 0.389 | -5.97 | 0.447 | False |
| 2026-06-12 05:38 | 5000 | -16.12 | 0.389 | -6.15 | 0.441 | False |
| 2026-06-12 09:29 | 5000 | -16.12 | 0.389 | -6.67 | 0.385 | False |
| 2026-06-12 13:14 | 5000 | -16.13 | 0.389 | -6.76 | 0.382 | False |
| 2026-06-12 17:03 | 5000 | -15.72 | 0.408 | -6.52 | 0.391 | False |
| 2026-06-12 20:48 | 5000 | -15.68 | 0.409 | -6.62 | 0.387 | False |
| 2026-06-13 00:57 | 5000 | -16.55 | 0.374 | -5.64 | 0.428 | False |
| 2026-06-13 05:35 | 5000 | -16.4 | 0.376 | -6.03 | 0.411 | False |
| 2026-06-13 09:08 | 5000 | -16.48 | 0.375 | -4.13 | 0.491 | False |
| 2026-06-13 12:41 | 5000 | -15.96 | 0.384 | -3.44 | 0.538 | False |

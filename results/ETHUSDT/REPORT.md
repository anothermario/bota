# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-08-04 17:47_

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

- Current-params net profit (full sample): **-17.57%**, PF 0.481, 102 trades, max DD -2030.29
- Optimizer out-of-sample: net **-5.8%**, PF 0.372, 28 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-03 06:58 | 5000 | -17.75 | 0.465 | -7.09 | 0.259 | False |
| 2026-08-03 11:21 | 5000 | -16.13 | 0.504 | -4.45 | 0.526 | False |
| 2026-08-03 14:35 | 5000 | -16.16 | 0.504 | -4.46 | 0.527 | False |
| 2026-08-03 17:49 | 5000 | -16.16 | 0.504 | -4.5 | 0.525 | False |
| 2026-08-03 21:01 | 5000 | -16.26 | 0.502 | -3.92 | 0.561 | False |
| 2026-08-04 02:25 | 5000 | -16.62 | 0.496 | -5.04 | 0.478 | False |
| 2026-08-04 06:26 | 5000 | -16.82 | 0.492 | -5.04 | 0.478 | False |
| 2026-08-04 10:37 | 5000 | -16.82 | 0.492 | -4.77 | 0.493 | False |
| 2026-08-04 14:08 | 5000 | -17.52 | 0.482 | -5.66 | 0.45 | False |
| 2026-08-04 17:47 | 5000 | -17.57 | 0.481 | -5.8 | 0.372 | False |

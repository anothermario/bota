# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-08-05 05:05_

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

- Current-params net profit (full sample): **-16.47%**, PF 0.503, 101 trades, max DD -2057.38
- Optimizer out-of-sample: net **-3.27%**, PF 0.606, 30 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-03 17:49 | 5000 | -16.16 | 0.504 | -4.5 | 0.525 | False |
| 2026-08-03 21:01 | 5000 | -16.26 | 0.502 | -3.92 | 0.561 | False |
| 2026-08-04 02:25 | 5000 | -16.62 | 0.496 | -5.04 | 0.478 | False |
| 2026-08-04 06:26 | 5000 | -16.82 | 0.492 | -5.04 | 0.478 | False |
| 2026-08-04 10:37 | 5000 | -16.82 | 0.492 | -4.77 | 0.493 | False |
| 2026-08-04 14:08 | 5000 | -17.52 | 0.482 | -5.66 | 0.45 | False |
| 2026-08-04 17:47 | 5000 | -17.57 | 0.481 | -5.8 | 0.372 | False |
| 2026-08-04 20:33 | 5000 | -16.48 | 0.502 | -3.56 | 0.587 | False |
| 2026-08-05 00:35 | 5000 | -16.48 | 0.503 | -3.39 | 0.599 | False |
| 2026-08-05 05:05 | 5000 | -16.47 | 0.503 | -3.27 | 0.606 | False |

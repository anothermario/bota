# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-05 16:10_

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

- Current-params net profit (full sample): **-16.5%**, PF 0.383, 96 trades, max DD -1771.78
- Optimizer out-of-sample: net **-3.79%**, PF 0.383, 18 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-04 04:13 | 5000 | -15.81 | 0.403 | -3.73 | 0.41 | False |
| 2026-09-04 08:16 | 5000 | -15.82 | 0.403 | -5.03 | 0.29 | False |
| 2026-09-04 12:17 | 5000 | -16.41 | 0.384 | -5.03 | 0.29 | False |
| 2026-09-04 16:12 | 5000 | -16.62 | 0.381 | -4.7 | 0.305 | False |
| 2026-09-04 20:10 | 5000 | -16.4 | 0.385 | -4.49 | 0.314 | False |
| 2026-09-05 00:29 | 5000 | -16.41 | 0.385 | -3.74 | 0.387 | False |
| 2026-09-05 04:12 | 5000 | -16.4 | 0.385 | -3.74 | 0.387 | False |
| 2026-09-05 08:13 | 5000 | -16.39 | 0.385 | -3.73 | 0.387 | False |
| 2026-09-05 12:14 | 5000 | -15.92 | 0.393 | -3.73 | 0.387 | False |
| 2026-09-05 16:10 | 5000 | -16.5 | 0.383 | -3.79 | 0.383 | False |

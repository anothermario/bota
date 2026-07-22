# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-22 21:06_

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

- Current-params net profit (full sample): **-15.31%**, PF 0.428, 65 trades, max DD -1530.93
- Optimizer out-of-sample: net **-6.74%**, PF 0.175, 16 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-21 10:24 | 5000 | -13.72 | 0.455 | -5.86 | 0.195 | False |
| 2026-07-21 13:47 | 5000 | -13.72 | 0.455 | -5.79 | 0.197 | False |
| 2026-07-21 17:18 | 5000 | -13.9 | 0.452 | -5.43 | 0.209 | False |
| 2026-07-21 21:08 | 5000 | -14.13 | 0.447 | -5.69 | 0.2 | False |
| 2026-07-22 02:33 | 5000 | -14.13 | 0.447 | -5.39 | 0.21 | False |
| 2026-07-22 06:27 | 5000 | -14.16 | 0.447 | -4.99 | 0.278 | False |
| 2026-07-22 10:24 | 5000 | -14.63 | 0.439 | -5.44 | 0.264 | False |
| 2026-07-22 13:50 | 5000 | -14.59 | 0.439 | -6.23 | 0.186 | False |
| 2026-07-22 17:17 | 5000 | -14.63 | 0.439 | -5.96 | 0.194 | False |
| 2026-07-22 21:06 | 5000 | -15.31 | 0.428 | -6.74 | 0.175 | False |

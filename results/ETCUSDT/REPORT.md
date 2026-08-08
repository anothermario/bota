# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-08 20:08_

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
  "don_len": 15,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-14.36%**, PF 0.441, 61 trades, max DD -1489.8
- Optimizer out-of-sample: net **-0.51%**, PF 0.923, 16 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-07 08:26 | 5000 | -15.62 | 0.434 | -1.68 | 0.777 | False |
| 2026-08-07 12:19 | 5000 | -15.02 | 0.445 | -1.3 | 0.819 | False |
| 2026-08-07 16:19 | 5000 | -15.76 | 0.431 | -1.28 | 0.822 | False |
| 2026-08-07 20:15 | 5000 | -16.43 | 0.419 | -1.34 | 0.815 | False |
| 2026-08-08 00:19 | 5000 | -15.97 | 0.427 | -0.75 | 0.887 | False |
| 2026-08-08 04:25 | 5000 | -15.93 | 0.428 | -0.31 | 0.951 | False |
| 2026-08-08 08:14 | 5000 | -15.54 | 0.435 | -0.3 | 0.952 | False |
| 2026-08-08 12:10 | 5000 | -15.56 | 0.435 | -0.17 | 0.973 | False |
| 2026-08-08 16:09 | 5000 | -14.8 | 0.449 | 0.1 | 1.016 | True |
| 2026-08-08 20:08 | 5000 | -14.36 | 0.441 | -0.51 | 0.923 | False |

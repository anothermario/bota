# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-11 08:23_

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

- Current-params net profit (full sample): **-15.06%**, PF 0.417, 59 trades, max DD -1579.53
- Optimizer out-of-sample: net **-5.99%**, PF 0.142, 15 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-09 20:09 | 5000 | -13.97 | 0.448 | -2.95 | 0.628 | False |
| 2026-08-10 00:21 | 5000 | -13.75 | 0.454 | -3.62 | 0.579 | False |
| 2026-08-10 04:33 | 5000 | -14.4 | 0.442 | -4.5 | 0.514 | False |
| 2026-08-10 08:35 | 5000 | -15.81 | 0.403 | -4.46 | 0.518 | False |
| 2026-08-10 12:19 | 5000 | -15.68 | 0.405 | -6.67 | 0.263 | False |
| 2026-08-10 16:19 | 5000 | -14.86 | 0.421 | -7.19 | 0.187 | False |
| 2026-08-10 20:15 | 5000 | -14.89 | 0.421 | -7.38 | 0.181 | False |
| 2026-08-11 00:20 | 5000 | -14.89 | 0.421 | -5.94 | 0.194 | False |
| 2026-08-11 04:31 | 5000 | -15.06 | 0.417 | -4.09 | 0.248 | False |
| 2026-08-11 08:23 | 5000 | -15.06 | 0.417 | -5.99 | 0.142 | False |

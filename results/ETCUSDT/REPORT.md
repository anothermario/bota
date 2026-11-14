# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-11-14 12:09_

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
  "chand_len": 26,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-15.14%**, PF 0.409, 65 trades, max DD -1662.2
- Optimizer out-of-sample: net **-5.5%**, PF 0.355, 18 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-13 00:19 | 5000 | -14.33 | 0.427 | -7.66 | 0.179 | False |
| 2026-11-13 04:09 | 5000 | -14.35 | 0.427 | -7.17 | 0.19 | False |
| 2026-11-13 08:10 | 5000 | -14.56 | 0.423 | -7.25 | 0.188 | False |
| 2026-11-13 12:10 | 5000 | -14.74 | 0.415 | -7.05 | 0.193 | False |
| 2026-11-13 16:08 | 5000 | -14.74 | 0.415 | -6.36 | 0.21 | False |
| 2026-11-13 20:07 | 5000 | -14.74 | 0.415 | -4.85 | 0.416 | False |
| 2026-11-14 00:19 | 5000 | -14.74 | 0.415 | -6.26 | 0.323 | False |
| 2026-11-14 04:08 | 5000 | -14.62 | 0.417 | -6.43 | 0.247 | False |
| 2026-11-14 08:08 | 5000 | -14.92 | 0.419 | -6.68 | 0.24 | False |
| 2026-11-14 12:09 | 5000 | -15.14 | 0.409 | -5.5 | 0.355 | False |

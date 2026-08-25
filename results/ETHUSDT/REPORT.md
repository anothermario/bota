# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-08-25 16:14_

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

- Current-params net profit (full sample): **-21.9%**, PF 0.289, 106 trades, max DD -2195.39
- Optimizer out-of-sample: net **-4.57%**, PF 0.298, 26 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-24 04:17 | 5000 | -20.94 | 0.307 | -5.13 | 0.246 | False |
| 2026-08-24 08:17 | 5000 | -20.79 | 0.309 | -5.15 | 0.245 | False |
| 2026-08-24 12:10 | 5000 | -20.78 | 0.309 | -4.92 | 0.254 | False |
| 2026-08-24 16:11 | 5000 | -20.82 | 0.308 | -4.97 | 0.252 | False |
| 2026-08-24 20:08 | 5000 | -21.7 | 0.29 | -4.7 | 0.263 | False |
| 2026-08-25 00:14 | 5000 | -21.7 | 0.29 | -4.7 | 0.263 | False |
| 2026-08-25 04:15 | 5000 | -21.7 | 0.29 | -4.73 | 0.262 | False |
| 2026-08-25 08:16 | 5000 | -21.67 | 0.29 | -4.16 | 0.288 | False |
| 2026-08-25 12:11 | 5000 | -21.31 | 0.295 | -4.16 | 0.288 | False |
| 2026-08-25 16:14 | 5000 | -21.9 | 0.289 | -4.57 | 0.298 | False |

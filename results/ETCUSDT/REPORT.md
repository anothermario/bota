# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-21 13:47_

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

- Current-params net profit (full sample): **-13.72%**, PF 0.455, 62 trades, max DD -1372.12
- Optimizer out-of-sample: net **-5.79%**, PF 0.197, 14 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-20 02:51 | 5000 | -13.68 | 0.454 | -5.03 | 0.335 | False |
| 2026-07-20 06:44 | 5000 | -13.69 | 0.454 | -4.96 | 0.345 | False |
| 2026-07-20 10:51 | 5000 | -13.25 | 0.463 | -5.62 | 0.253 | False |
| 2026-07-20 14:03 | 5000 | -13.25 | 0.463 | -6.62 | 0.174 | False |
| 2026-07-20 18:01 | 5000 | -13.25 | 0.463 | -6.08 | 0.187 | False |
| 2026-07-20 21:11 | 5000 | -13.27 | 0.463 | -6.11 | 0.187 | False |
| 2026-07-21 02:34 | 5000 | -13.69 | 0.455 | -6.56 | 0.176 | False |
| 2026-07-21 06:27 | 5000 | -13.69 | 0.455 | -6.56 | 0.176 | False |
| 2026-07-21 10:24 | 5000 | -13.72 | 0.455 | -5.86 | 0.195 | False |
| 2026-07-21 13:47 | 5000 | -13.72 | 0.455 | -5.79 | 0.197 | False |

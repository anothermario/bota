# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-06-24 05:24_

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
  "chand_len": 18,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-8.82%**, PF 0.68, 74 trades, max DD -1213.4
- Optimizer out-of-sample: net **1.36%**, PF 1.279, 14 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-22 17:34 | 5000 | -11.32 | 0.602 | -1.48 | 0.736 | False |
| 2026-06-22 21:04 | 5000 | -10.89 | 0.613 | -1.75 | 0.704 | False |
| 2026-06-23 00:50 | 5000 | -11.17 | 0.606 | -1.6 | 0.723 | False |
| 2026-06-23 05:25 | 5000 | -11.14 | 0.607 | -1.74 | 0.705 | False |
| 2026-06-23 09:13 | 5000 | -10.89 | 0.613 | -0.41 | 0.916 | False |
| 2026-06-23 13:03 | 5000 | -9.46 | 0.663 | 1.27 | 1.284 | False |
| 2026-06-23 16:52 | 5000 | -9.87 | 0.652 | 1.19 | 1.263 | False |
| 2026-06-23 20:47 | 5000 | -9.22 | 0.67 | 0.63 | 1.13 | False |
| 2026-06-24 00:47 | 5000 | -8.82 | 0.68 | 2.85 | 1.705 | False |
| 2026-06-24 05:24 | 5000 | -8.82 | 0.68 | 1.36 | 1.279 | False |

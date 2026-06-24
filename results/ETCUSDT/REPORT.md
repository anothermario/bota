# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-06-24 12:50_

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

- Current-params net profit (full sample): **-9.33%**, PF 0.671, 76 trades, max DD -1213.41
- Optimizer out-of-sample: net **1.13%**, PF 1.225, 14 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-23 00:50 | 5000 | -11.17 | 0.606 | -1.6 | 0.723 | False |
| 2026-06-23 05:25 | 5000 | -11.14 | 0.607 | -1.74 | 0.705 | False |
| 2026-06-23 09:13 | 5000 | -10.89 | 0.613 | -0.41 | 0.916 | False |
| 2026-06-23 13:03 | 5000 | -9.46 | 0.663 | 1.27 | 1.284 | False |
| 2026-06-23 16:52 | 5000 | -9.87 | 0.652 | 1.19 | 1.263 | False |
| 2026-06-23 20:47 | 5000 | -9.22 | 0.67 | 0.63 | 1.13 | False |
| 2026-06-24 00:47 | 5000 | -8.82 | 0.68 | 2.85 | 1.705 | False |
| 2026-06-24 05:24 | 5000 | -8.82 | 0.68 | 1.36 | 1.279 | False |
| 2026-06-24 09:11 | 5000 | -8.45 | 0.693 | 2.09 | 1.482 | True |
| 2026-06-24 12:50 | 5000 | -9.33 | 0.671 | 1.13 | 1.225 | False |

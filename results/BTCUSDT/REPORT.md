# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-28 12:19_

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
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-8.23%**, PF 0.607, 66 trades, max DD -940.06
- Optimizer out-of-sample: net **-0.81%**, PF 0.889, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-27 00:35 | 5000 | -8.6 | 0.593 | -1.05 | 0.856 | False |
| 2026-09-27 04:13 | 5000 | -8.61 | 0.593 | -1.05 | 0.856 | False |
| 2026-09-27 08:14 | 5000 | -8.41 | 0.599 | -1.05 | 0.856 | False |
| 2026-09-27 12:16 | 5000 | -8.45 | 0.599 | -1.09 | 0.856 | False |
| 2026-09-27 16:11 | 5000 | -8.7 | 0.591 | -1.29 | 0.83 | False |
| 2026-09-27 20:11 | 5000 | -8.35 | 0.602 | -1.29 | 0.83 | False |
| 2026-09-28 00:35 | 5000 | -8.2 | 0.609 | -1.28 | 0.83 | False |
| 2026-09-28 04:15 | 5000 | -8.74 | 0.591 | -1.1 | 0.855 | False |
| 2026-09-28 08:22 | 5000 | -8.39 | 0.601 | -1.1 | 0.855 | False |
| 2026-09-28 12:19 | 5000 | -8.23 | 0.607 | -0.81 | 0.889 | False |

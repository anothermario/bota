# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-06-23 09:13_

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

- Current-params net profit (full sample): **-10.89%**, PF 0.613, 75 trades, max DD -1228.49
- Optimizer out-of-sample: net **-0.41%**, PF 0.916, 13 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-21 20:35 | 5000 | -11.38 | 0.598 | 0.94 | 1.232 | False |
| 2026-06-22 00:58 | 5000 | -10.74 | 0.613 | 0.93 | 1.231 | False |
| 2026-06-22 05:54 | 5000 | -11.51 | 0.595 | 1.37 | 1.336 | False |
| 2026-06-22 10:06 | 5000 | -10.49 | 0.62 | 1.53 | 1.375 | False |
| 2026-06-22 13:57 | 5000 | -10.48 | 0.62 | 0.82 | 1.203 | False |
| 2026-06-22 17:34 | 5000 | -11.32 | 0.602 | -1.48 | 0.736 | False |
| 2026-06-22 21:04 | 5000 | -10.89 | 0.613 | -1.75 | 0.704 | False |
| 2026-06-23 00:50 | 5000 | -11.17 | 0.606 | -1.6 | 0.723 | False |
| 2026-06-23 05:25 | 5000 | -11.14 | 0.607 | -1.74 | 0.705 | False |
| 2026-06-23 09:13 | 5000 | -10.89 | 0.613 | -0.41 | 0.916 | False |

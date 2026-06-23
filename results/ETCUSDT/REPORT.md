# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-06-23 16:52_

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

- Current-params net profit (full sample): **-9.87%**, PF 0.652, 76 trades, max DD -1268.76
- Optimizer out-of-sample: net **1.19%**, PF 1.263, 14 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-22 05:54 | 5000 | -11.51 | 0.595 | 1.37 | 1.336 | False |
| 2026-06-22 10:06 | 5000 | -10.49 | 0.62 | 1.53 | 1.375 | False |
| 2026-06-22 13:57 | 5000 | -10.48 | 0.62 | 0.82 | 1.203 | False |
| 2026-06-22 17:34 | 5000 | -11.32 | 0.602 | -1.48 | 0.736 | False |
| 2026-06-22 21:04 | 5000 | -10.89 | 0.613 | -1.75 | 0.704 | False |
| 2026-06-23 00:50 | 5000 | -11.17 | 0.606 | -1.6 | 0.723 | False |
| 2026-06-23 05:25 | 5000 | -11.14 | 0.607 | -1.74 | 0.705 | False |
| 2026-06-23 09:13 | 5000 | -10.89 | 0.613 | -0.41 | 0.916 | False |
| 2026-06-23 13:03 | 5000 | -9.46 | 0.663 | 1.27 | 1.284 | False |
| 2026-06-23 16:52 | 5000 | -9.87 | 0.652 | 1.19 | 1.263 | False |

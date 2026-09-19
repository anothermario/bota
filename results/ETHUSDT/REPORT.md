# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-19 20:10_

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

- Current-params net profit (full sample): **-13.07%**, PF 0.527, 101 trades, max DD -1645.94
- Optimizer out-of-sample: net **-7.53%**, PF 0.38, 35 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-18 08:15 | 5000 | -16.43 | 0.403 | -5.8 | 0.491 | False |
| 2026-09-18 12:16 | 5000 | -16.81 | 0.397 | -5.79 | 0.491 | False |
| 2026-09-18 16:11 | 5000 | -15.99 | 0.411 | -5.79 | 0.491 | False |
| 2026-09-18 20:11 | 5000 | -15.99 | 0.411 | -6.04 | 0.468 | False |
| 2026-09-19 00:29 | 5000 | -12.46 | 0.54 | -2.63 | 0.766 | False |
| 2026-09-19 04:12 | 5000 | -12.46 | 0.54 | -3.63 | 0.673 | False |
| 2026-09-19 08:13 | 5000 | -12.46 | 0.54 | -3.64 | 0.673 | False |
| 2026-09-19 12:15 | 5000 | -12.49 | 0.54 | -3.65 | 0.674 | False |
| 2026-09-19 16:10 | 5000 | -12.69 | 0.536 | -7.45 | 0.396 | False |
| 2026-09-19 20:10 | 5000 | -13.07 | 0.527 | -7.53 | 0.38 | False |

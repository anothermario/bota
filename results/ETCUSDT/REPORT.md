# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-08 08:14_

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

- Current-params net profit (full sample): **-15.54%**, PF 0.435, 67 trades, max DD -1568.56
- Optimizer out-of-sample: net **-0.3%**, PF 0.952, 17 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-06 21:58 | 5000 | -16.27 | 0.42 | -2.86 | 0.667 | False |
| 2026-08-07 01:16 | 5000 | -16.19 | 0.423 | -2.67 | 0.685 | False |
| 2026-08-07 04:41 | 5000 | -16.42 | 0.419 | -1.86 | 0.759 | False |
| 2026-08-07 08:26 | 5000 | -15.62 | 0.434 | -1.68 | 0.777 | False |
| 2026-08-07 12:19 | 5000 | -15.02 | 0.445 | -1.3 | 0.819 | False |
| 2026-08-07 16:19 | 5000 | -15.76 | 0.431 | -1.28 | 0.822 | False |
| 2026-08-07 20:15 | 5000 | -16.43 | 0.419 | -1.34 | 0.815 | False |
| 2026-08-08 00:19 | 5000 | -15.97 | 0.427 | -0.75 | 0.887 | False |
| 2026-08-08 04:25 | 5000 | -15.93 | 0.428 | -0.31 | 0.951 | False |
| 2026-08-08 08:14 | 5000 | -15.54 | 0.435 | -0.3 | 0.952 | False |

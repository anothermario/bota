# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-06-16 13:53_

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
  "don_len": 20,
  "atr_len": 14,
  "atr_mult": 3.0,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-12.76%**, PF 0.501, 89 trades, max DD -1551.76
- Optimizer out-of-sample: net **-0.71%**, PF 0.903, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-15 00:59 | 5000 | -15.93 | 0.387 | -3.36 | 0.548 | False |
| 2026-06-15 05:52 | 5000 | -16.18 | 0.383 | -3.36 | 0.548 | False |
| 2026-06-15 10:12 | 5000 | -15.49 | 0.395 | -2.74 | 0.629 | False |
| 2026-06-15 14:12 | 5000 | -14.39 | 0.439 | -2.76 | 0.629 | False |
| 2026-06-15 17:41 | 5000 | -14.39 | 0.439 | -3.24 | 0.563 | False |
| 2026-06-15 21:05 | 5000 | -14.29 | 0.442 | -1.16 | 0.842 | False |
| 2026-06-16 01:04 | 5000 | -14.32 | 0.442 | -1.27 | 0.83 | False |
| 2026-06-16 05:54 | 5000 | -14.5 | 0.438 | -1.27 | 0.83 | False |
| 2026-06-16 09:51 | 5000 | -13.3 | 0.485 | -0.88 | 0.883 | False |
| 2026-06-16 13:53 | 5000 | -12.76 | 0.501 | -0.71 | 0.903 | False |

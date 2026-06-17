# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-06-17 05:43_

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
  "don_len": 30,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 26,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-12.76%**, PF 0.501, 89 trades, max DD -1551.71
- Optimizer out-of-sample: net **0.85%**, PF 1.145, 20 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-15 17:41 | 5000 | -14.39 | 0.439 | -3.24 | 0.563 | False |
| 2026-06-15 21:05 | 5000 | -14.29 | 0.442 | -1.16 | 0.842 | False |
| 2026-06-16 01:04 | 5000 | -14.32 | 0.442 | -1.27 | 0.83 | False |
| 2026-06-16 05:54 | 5000 | -14.5 | 0.438 | -1.27 | 0.83 | False |
| 2026-06-16 09:51 | 5000 | -13.3 | 0.485 | -0.88 | 0.883 | False |
| 2026-06-16 13:53 | 5000 | -12.76 | 0.501 | -0.71 | 0.903 | False |
| 2026-06-16 17:45 | 5000 | -13.07 | 0.495 | -0.17 | 0.975 | False |
| 2026-06-16 21:06 | 5000 | -13.07 | 0.495 | -0.17 | 0.975 | False |
| 2026-06-17 00:58 | 5000 | -12.76 | 0.501 | -0.17 | 0.975 | False |
| 2026-06-17 05:43 | 5000 | -12.76 | 0.501 | 0.85 | 1.145 | True |

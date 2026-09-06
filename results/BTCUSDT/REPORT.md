# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-06 12:14_

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

- Current-params net profit (full sample): **-7.67%**, PF 0.576, 67 trades, max DD -1045.02
- Optimizer out-of-sample: net **-3.77%**, PF 0.438, 15 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-05 00:29 | 5000 | -9.47 | 0.519 | -2.23 | 0.672 | False |
| 2026-09-05 04:12 | 5000 | -9.49 | 0.519 | -2.21 | 0.676 | False |
| 2026-09-05 08:13 | 5000 | -8.8 | 0.539 | -2.73 | 0.597 | False |
| 2026-09-05 12:14 | 5000 | -8.8 | 0.539 | -3.05 | 0.548 | False |
| 2026-09-05 16:10 | 5000 | -8.81 | 0.539 | -4.63 | 0.386 | False |
| 2026-09-05 20:10 | 5000 | -8.33 | 0.554 | -3.18 | 0.504 | False |
| 2026-09-06 00:34 | 5000 | -8.33 | 0.554 | -4.53 | 0.391 | False |
| 2026-09-06 04:12 | 5000 | -7.67 | 0.576 | -4.55 | 0.39 | False |
| 2026-09-06 08:13 | 5000 | -7.67 | 0.576 | -3.77 | 0.438 | False |
| 2026-09-06 12:14 | 5000 | -7.67 | 0.576 | -3.77 | 0.438 | False |

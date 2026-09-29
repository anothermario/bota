# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-29 20:13_

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

- Current-params net profit (full sample): **-9.44%**, PF 0.574, 68 trades, max DD -1044.57
- Optimizer out-of-sample: net **-0.9%**, PF 0.879, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-28 08:22 | 5000 | -8.39 | 0.601 | -1.1 | 0.855 | False |
| 2026-09-28 12:19 | 5000 | -8.23 | 0.607 | -0.81 | 0.889 | False |
| 2026-09-28 16:13 | 5000 | -9.11 | 0.583 | -1.86 | 0.778 | False |
| 2026-09-28 20:11 | 5000 | -9.11 | 0.583 | -1.58 | 0.805 | False |
| 2026-09-29 00:32 | 5000 | -9.11 | 0.583 | -1.39 | 0.825 | False |
| 2026-09-29 04:14 | 5000 | -9.11 | 0.583 | -1.42 | 0.821 | False |
| 2026-09-29 08:16 | 5000 | -9.11 | 0.583 | -0.63 | 0.913 | False |
| 2026-09-29 12:18 | 5000 | -9.23 | 0.579 | -0.62 | 0.915 | False |
| 2026-09-29 16:13 | 5000 | -8.87 | 0.594 | -0.66 | 0.914 | False |
| 2026-09-29 20:13 | 5000 | -9.44 | 0.574 | -0.9 | 0.879 | False |

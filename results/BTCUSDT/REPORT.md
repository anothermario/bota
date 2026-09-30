# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-30 20:13_

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

- Current-params net profit (full sample): **-9.29%**, PF 0.584, 67 trades, max DD -1083.34
- Optimizer out-of-sample: net **-2.95%**, PF 0.641, 26 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-29 08:16 | 5000 | -9.11 | 0.583 | -0.63 | 0.913 | False |
| 2026-09-29 12:18 | 5000 | -9.23 | 0.579 | -0.62 | 0.915 | False |
| 2026-09-29 16:13 | 5000 | -8.87 | 0.594 | -0.66 | 0.914 | False |
| 2026-09-29 20:13 | 5000 | -9.44 | 0.574 | -0.9 | 0.879 | False |
| 2026-09-30 00:34 | 5000 | -9.3 | 0.578 | -0.94 | 0.875 | False |
| 2026-09-30 04:14 | 5000 | -9.3 | 0.578 | -0.51 | 0.928 | False |
| 2026-09-30 08:16 | 5000 | -8.95 | 0.593 | -1.11 | 0.843 | False |
| 2026-09-30 12:21 | 5000 | -8.95 | 0.593 | -2.56 | 0.695 | False |
| 2026-09-30 16:13 | 5000 | -9.29 | 0.584 | -3.31 | 0.613 | False |
| 2026-09-30 20:13 | 5000 | -9.29 | 0.584 | -2.95 | 0.641 | False |

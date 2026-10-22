# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-22 16:13_

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
  "chand_len": 26,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-7.8%**, PF 0.68, 76 trades, max DD -1025.37
- Optimizer out-of-sample: net **1.34%**, PF 1.218, 23 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-21 04:13 | 5000 | -8.91 | 0.632 | -0.77 | 0.889 | False |
| 2026-10-21 08:15 | 5000 | -8.91 | 0.632 | -0.23 | 0.964 | False |
| 2026-10-21 12:16 | 5000 | -8.63 | 0.641 | -0.62 | 0.914 | False |
| 2026-10-21 16:11 | 5000 | -8.72 | 0.639 | -0.13 | 0.983 | False |
| 2026-10-21 20:11 | 5000 | -8.74 | 0.638 | -0.5 | 0.925 | False |
| 2026-10-22 00:29 | 5000 | -8.78 | 0.638 | -0.55 | 0.924 | False |
| 2026-10-22 04:12 | 5000 | -9.01 | 0.632 | -0.24 | 0.967 | False |
| 2026-10-22 08:15 | 5000 | -9.01 | 0.632 | -0.25 | 0.967 | False |
| 2026-10-22 12:17 | 5000 | -9.01 | 0.632 | 0.04 | 1.012 | True |
| 2026-10-22 16:13 | 5000 | -7.8 | 0.68 | 1.34 | 1.218 | True |

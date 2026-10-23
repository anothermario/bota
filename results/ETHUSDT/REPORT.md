# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-23 08:15_

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

- Current-params net profit (full sample): **-7.8%**, PF 0.68, 76 trades, max DD -1025.35
- Optimizer out-of-sample: net **0.82%**, PF 1.133, 22 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-21 20:11 | 5000 | -8.74 | 0.638 | -0.5 | 0.925 | False |
| 2026-10-22 00:29 | 5000 | -8.78 | 0.638 | -0.55 | 0.924 | False |
| 2026-10-22 04:12 | 5000 | -9.01 | 0.632 | -0.24 | 0.967 | False |
| 2026-10-22 08:15 | 5000 | -9.01 | 0.632 | -0.25 | 0.967 | False |
| 2026-10-22 12:17 | 5000 | -9.01 | 0.632 | 0.04 | 1.012 | True |
| 2026-10-22 16:13 | 5000 | -7.8 | 0.68 | 1.34 | 1.218 | True |
| 2026-10-22 20:11 | 5000 | -7.8 | 0.68 | 0.52 | 1.08 | True |
| 2026-10-23 00:30 | 5000 | -7.8 | 0.68 | 0.83 | 1.135 | True |
| 2026-10-23 04:13 | 5000 | -7.8 | 0.68 | 0.83 | 1.135 | True |
| 2026-10-23 08:15 | 5000 | -7.8 | 0.68 | 0.82 | 1.133 | True |

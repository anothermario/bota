# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-29 08:17_

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

- Current-params net profit (full sample): **-2.83%**, PF 0.873, 56 trades, max DD -938.37
- Optimizer out-of-sample: net **-1.98%**, PF 0.691, 16 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-27 20:11 | 5000 | -1.13 | 0.945 | -2.22 | 0.671 | False |
| 2026-09-28 00:35 | 5000 | -2.01 | 0.907 | -2.72 | 0.625 | False |
| 2026-09-28 04:15 | 5000 | -2.01 | 0.907 | -3.74 | 0.535 | False |
| 2026-09-28 08:22 | 5000 | -2.02 | 0.907 | -2.91 | 0.601 | False |
| 2026-09-28 12:20 | 5000 | -2.43 | 0.889 | -3.32 | 0.567 | False |
| 2026-09-28 16:14 | 5000 | -2.43 | 0.889 | -2.37 | 0.65 | False |
| 2026-09-28 20:12 | 5000 | -2.43 | 0.889 | -2.37 | 0.65 | False |
| 2026-09-29 00:33 | 5000 | -2.43 | 0.889 | -2.04 | 0.684 | False |
| 2026-09-29 04:14 | 5000 | -2.44 | 0.89 | -2.07 | 0.682 | False |
| 2026-09-29 08:17 | 5000 | -2.83 | 0.873 | -1.98 | 0.691 | False |

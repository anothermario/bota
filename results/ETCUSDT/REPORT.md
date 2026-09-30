# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-30 00:34_

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

- Current-params net profit (full sample): **-3.54%**, PF 0.848, 57 trades, max DD -1083.23
- Optimizer out-of-sample: net **-3.96%**, PF 0.527, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-28 12:20 | 5000 | -2.43 | 0.889 | -3.32 | 0.567 | False |
| 2026-09-28 16:14 | 5000 | -2.43 | 0.889 | -2.37 | 0.65 | False |
| 2026-09-28 20:12 | 5000 | -2.43 | 0.889 | -2.37 | 0.65 | False |
| 2026-09-29 00:33 | 5000 | -2.43 | 0.889 | -2.04 | 0.684 | False |
| 2026-09-29 04:14 | 5000 | -2.44 | 0.89 | -2.07 | 0.682 | False |
| 2026-09-29 08:17 | 5000 | -2.83 | 0.873 | -1.98 | 0.691 | False |
| 2026-09-29 12:18 | 5000 | -2.17 | 0.901 | -2.0 | 0.691 | False |
| 2026-09-29 16:13 | 5000 | -2.91 | 0.871 | -3.32 | 0.57 | False |
| 2026-09-29 20:13 | 5000 | -3.54 | 0.848 | -3.94 | 0.528 | False |
| 2026-09-30 00:34 | 5000 | -3.54 | 0.848 | -3.96 | 0.527 | False |

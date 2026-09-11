# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-11 16:12_

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

- Current-params net profit (full sample): **-1.87%**, PF 0.914, 54 trades, max DD -639.85
- Optimizer out-of-sample: net **-3.41%**, PF 0.58, 17 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-10 04:13 | 5000 | -1.47 | 0.926 | -3.86 | 0.413 | False |
| 2026-09-10 08:16 | 5000 | -1.5 | 0.924 | -3.39 | 0.447 | False |
| 2026-09-10 12:17 | 5000 | -2.23 | 0.889 | -3.98 | 0.408 | False |
| 2026-09-10 16:11 | 5000 | -1.72 | 0.913 | -2.52 | 0.569 | False |
| 2026-09-10 20:10 | 5000 | -1.72 | 0.913 | -2.59 | 0.557 | False |
| 2026-09-11 00:31 | 5000 | 0.29 | 1.015 | -0.53 | 0.909 | False |
| 2026-09-11 04:14 | 5000 | 0.5 | 1.026 | -0.55 | 0.905 | False |
| 2026-09-11 08:15 | 5000 | -0.1 | 0.995 | -2.5 | 0.651 | False |
| 2026-09-11 12:17 | 5000 | -0.12 | 0.995 | -2.52 | 0.651 | False |
| 2026-09-11 16:12 | 5000 | -1.87 | 0.914 | -3.41 | 0.58 | False |

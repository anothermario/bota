# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-13 08:14_

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

- Current-params net profit (full sample): **0.01%**, PF 1.0, 53 trades, max DD -652.64
- Optimizer out-of-sample: net **-2.46%**, PF 0.66, 16 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-11 20:11 | 5000 | -1.87 | 0.914 | -3.41 | 0.58 | False |
| 2026-09-12 00:29 | 5000 | -1.87 | 0.914 | -3.41 | 0.58 | False |
| 2026-09-12 04:12 | 5000 | -1.87 | 0.914 | -4.07 | 0.535 | False |
| 2026-09-12 08:13 | 5000 | -1.87 | 0.914 | -4.08 | 0.535 | False |
| 2026-09-12 12:15 | 5000 | -1.02 | 0.952 | -3.41 | 0.58 | False |
| 2026-09-12 16:11 | 5000 | -1.02 | 0.952 | -3.41 | 0.58 | False |
| 2026-09-12 20:10 | 5000 | -0.51 | 0.977 | -3.45 | 0.58 | False |
| 2026-09-13 00:34 | 5000 | -0.51 | 0.977 | -2.42 | 0.667 | False |
| 2026-09-13 04:13 | 5000 | -0.56 | 0.973 | -2.46 | 0.66 | False |
| 2026-09-13 08:14 | 5000 | 0.01 | 1.0 | -2.46 | 0.66 | False |

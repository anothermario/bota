# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-12 16:11_

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

- Current-params net profit (full sample): **-1.02%**, PF 0.952, 53 trades, max DD -645.39
- Optimizer out-of-sample: net **-3.41%**, PF 0.58, 17 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-11 04:14 | 5000 | 0.5 | 1.026 | -0.55 | 0.905 | False |
| 2026-09-11 08:15 | 5000 | -0.1 | 0.995 | -2.5 | 0.651 | False |
| 2026-09-11 12:17 | 5000 | -0.12 | 0.995 | -2.52 | 0.651 | False |
| 2026-09-11 16:12 | 5000 | -1.87 | 0.914 | -3.41 | 0.58 | False |
| 2026-09-11 20:11 | 5000 | -1.87 | 0.914 | -3.41 | 0.58 | False |
| 2026-09-12 00:29 | 5000 | -1.87 | 0.914 | -3.41 | 0.58 | False |
| 2026-09-12 04:12 | 5000 | -1.87 | 0.914 | -4.07 | 0.535 | False |
| 2026-09-12 08:13 | 5000 | -1.87 | 0.914 | -4.08 | 0.535 | False |
| 2026-09-12 12:15 | 5000 | -1.02 | 0.952 | -3.41 | 0.58 | False |
| 2026-09-12 16:11 | 5000 | -1.02 | 0.952 | -3.41 | 0.58 | False |

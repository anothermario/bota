# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-22 16:11_

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

- Current-params net profit (full sample): **-3.37%**, PF 0.839, 54 trades, max DD -799.38
- Optimizer out-of-sample: net **-4.41%**, PF 0.513, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-21 04:15 | 5000 | -2.7 | 0.872 | -4.21 | 0.523 | False |
| 2026-09-21 08:18 | 5000 | -2.7 | 0.872 | -3.3 | 0.586 | False |
| 2026-09-21 12:17 | 5000 | -2.69 | 0.872 | -3.3 | 0.586 | False |
| 2026-09-21 16:13 | 5000 | -2.72 | 0.872 | -3.31 | 0.586 | False |
| 2026-09-21 20:11 | 5000 | -3.22 | 0.851 | -3.84 | 0.548 | False |
| 2026-09-22 00:31 | 5000 | -1.43 | 0.933 | -3.84 | 0.548 | False |
| 2026-09-22 04:13 | 5000 | -1.47 | 0.931 | -3.85 | 0.548 | False |
| 2026-09-22 08:16 | 5000 | -1.84 | 0.913 | -3.85 | 0.548 | False |
| 2026-09-22 12:17 | 5000 | -2.55 | 0.879 | -3.42 | 0.578 | False |
| 2026-09-22 16:11 | 5000 | -3.37 | 0.839 | -4.41 | 0.513 | False |

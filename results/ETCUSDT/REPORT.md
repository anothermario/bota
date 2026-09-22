# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-22 04:13_

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

- Current-params net profit (full sample): **-1.47%**, PF 0.931, 55 trades, max DD -814.98
- Optimizer out-of-sample: net **-3.85%**, PF 0.548, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-20 16:11 | 5000 | -2.83 | 0.866 | -3.84 | 0.546 | False |
| 2026-09-20 20:10 | 5000 | -2.83 | 0.866 | -4.21 | 0.523 | False |
| 2026-09-21 00:33 | 5000 | -2.7 | 0.872 | -4.22 | 0.523 | False |
| 2026-09-21 04:15 | 5000 | -2.7 | 0.872 | -4.21 | 0.523 | False |
| 2026-09-21 08:18 | 5000 | -2.7 | 0.872 | -3.3 | 0.586 | False |
| 2026-09-21 12:17 | 5000 | -2.69 | 0.872 | -3.3 | 0.586 | False |
| 2026-09-21 16:13 | 5000 | -2.72 | 0.872 | -3.31 | 0.586 | False |
| 2026-09-21 20:11 | 5000 | -3.22 | 0.851 | -3.84 | 0.548 | False |
| 2026-09-22 00:31 | 5000 | -1.43 | 0.933 | -3.84 | 0.548 | False |
| 2026-09-22 04:13 | 5000 | -1.47 | 0.931 | -3.85 | 0.548 | False |

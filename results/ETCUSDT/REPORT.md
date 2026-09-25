# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-25 20:10_

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

- Current-params net profit (full sample): **-1.45%**, PF 0.931, 55 trades, max DD -811.39
- Optimizer out-of-sample: net **-4.12%**, PF 0.507, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-24 08:17 | 5000 | -3.39 | 0.84 | -3.23 | 0.604 | False |
| 2026-09-24 12:17 | 5000 | -1.31 | 0.937 | -1.14 | 0.848 | False |
| 2026-09-24 16:13 | 5000 | -2.3 | 0.894 | -2.34 | 0.726 | False |
| 2026-09-24 20:12 | 5000 | -1.45 | 0.931 | -2.47 | 0.709 | False |
| 2026-09-25 00:31 | 5000 | -1.45 | 0.931 | -2.54 | 0.7 | False |
| 2026-09-25 04:14 | 5000 | -1.45 | 0.931 | -3.3 | 0.608 | False |
| 2026-09-25 08:16 | 5000 | -1.45 | 0.931 | -3.59 | 0.572 | False |
| 2026-09-25 12:17 | 5000 | -1.45 | 0.931 | -4.12 | 0.507 | False |
| 2026-09-25 16:13 | 5000 | -2.22 | 0.897 | -4.12 | 0.507 | False |
| 2026-09-25 20:10 | 5000 | -1.45 | 0.931 | -4.12 | 0.507 | False |

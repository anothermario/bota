# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-25 00:31_

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

- Current-params net profit (full sample): **-1.45%**, PF 0.931, 55 trades, max DD -811.38
- Optimizer out-of-sample: net **-2.54%**, PF 0.7, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-23 12:17 | 5000 | -3.09 | 0.852 | -3.21 | 0.603 | False |
| 2026-09-23 16:13 | 5000 | -3.1 | 0.852 | -3.22 | 0.603 | False |
| 2026-09-23 20:12 | 5000 | -3.89 | 0.82 | -3.22 | 0.603 | False |
| 2026-09-24 00:30 | 5000 | -3.89 | 0.82 | -3.22 | 0.603 | False |
| 2026-09-24 04:13 | 5000 | -3.3 | 0.844 | -2.64 | 0.653 | False |
| 2026-09-24 08:17 | 5000 | -3.39 | 0.84 | -3.23 | 0.604 | False |
| 2026-09-24 12:17 | 5000 | -1.31 | 0.937 | -1.14 | 0.848 | False |
| 2026-09-24 16:13 | 5000 | -2.3 | 0.894 | -2.34 | 0.726 | False |
| 2026-09-24 20:12 | 5000 | -1.45 | 0.931 | -2.47 | 0.709 | False |
| 2026-09-25 00:31 | 5000 | -1.45 | 0.931 | -2.54 | 0.7 | False |

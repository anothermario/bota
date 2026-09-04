# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-04 16:12_

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

- Current-params net profit (full sample): **-5.23%**, PF 0.751, 51 trades, max DD -844.8
- Optimizer out-of-sample: net **1.67%**, PF 1.256, 14 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-03 05:15 | 5000 | -6.28 | 0.7 | 1.26 | 1.185 | True |
| 2026-09-03 08:16 | 5000 | -6.42 | 0.695 | 1.26 | 1.186 | True |
| 2026-09-03 12:18 | 5000 | -6.93 | 0.678 | 1.26 | 1.185 | True |
| 2026-09-03 16:12 | 5000 | -7.2 | 0.676 | 1.23 | 1.185 | True |
| 2026-09-03 20:10 | 5000 | -6.3 | 0.7 | 1.24 | 1.186 | True |
| 2026-09-04 00:29 | 5000 | -5.14 | 0.755 | 3.34 | 1.551 | True |
| 2026-09-04 04:13 | 5000 | -5.14 | 0.755 | 3.33 | 1.551 | True |
| 2026-09-04 08:16 | 5000 | -5.69 | 0.733 | 3.24 | 1.536 | False |
| 2026-09-04 12:17 | 5000 | -5.21 | 0.751 | 3.21 | 1.531 | False |
| 2026-09-04 16:12 | 5000 | -5.23 | 0.751 | 1.67 | 1.256 | False |

# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-05 12:14_

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
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-8.8%**, PF 0.539, 69 trades, max DD -1099.09
- Optimizer out-of-sample: net **-3.05%**, PF 0.548, 16 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-04 00:28 | 5000 | -7.48 | 0.615 | -1.66 | 0.733 | False |
| 2026-09-04 04:13 | 5000 | -7.52 | 0.615 | -1.7 | 0.733 | False |
| 2026-09-04 08:15 | 5000 | -8.66 | 0.55 | -2.53 | 0.662 | False |
| 2026-09-04 12:17 | 5000 | -9.48 | 0.519 | -2.28 | 0.667 | False |
| 2026-09-04 16:12 | 5000 | -9.48 | 0.519 | -2.78 | 0.621 | False |
| 2026-09-04 20:10 | 5000 | -9.48 | 0.519 | -2.24 | 0.672 | False |
| 2026-09-05 00:29 | 5000 | -9.47 | 0.519 | -2.23 | 0.672 | False |
| 2026-09-05 04:12 | 5000 | -9.49 | 0.519 | -2.21 | 0.676 | False |
| 2026-09-05 08:13 | 5000 | -8.8 | 0.539 | -2.73 | 0.597 | False |
| 2026-09-05 12:14 | 5000 | -8.8 | 0.539 | -3.05 | 0.548 | False |

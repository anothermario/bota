# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-28 16:09_

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

- Current-params net profit (full sample): **-10.0%**, PF 0.583, 75 trades, max DD -999.79
- Optimizer out-of-sample: net **-3.25%**, PF 0.474, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-27 04:12 | 5000 | -9.71 | 0.61 | -1.75 | 0.776 | False |
| 2026-10-27 08:15 | 5000 | -9.44 | 0.622 | -1.76 | 0.775 | False |
| 2026-10-27 12:17 | 5000 | -10.44 | 0.577 | -2.57 | 0.708 | False |
| 2026-10-27 16:10 | 5000 | -10.82 | 0.561 | -0.76 | 0.889 | False |
| 2026-10-27 20:09 | 5000 | -11.21 | 0.552 | -2.04 | 0.699 | False |
| 2026-10-28 00:22 | 5000 | -10.77 | 0.562 | -3.5 | 0.475 | False |
| 2026-10-28 04:10 | 5000 | -10.77 | 0.562 | -3.5 | 0.476 | False |
| 2026-10-28 08:11 | 5000 | -10.8 | 0.562 | -3.73 | 0.439 | False |
| 2026-10-28 12:12 | 5000 | -10.6 | 0.567 | -3.74 | 0.439 | False |
| 2026-10-28 16:09 | 5000 | -10.0 | 0.583 | -3.25 | 0.474 | False |

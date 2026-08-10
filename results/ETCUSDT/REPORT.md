# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-10 20:15_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.3,
  "use_adx": true,
  "adx_len": 14,
  "adx_thresh": 20.0,
  "don_len": 15,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-14.89%**, PF 0.421, 58 trades, max DD -1562.83
- Optimizer out-of-sample: net **-7.38%**, PF 0.181, 18 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-09 08:15 | 5000 | -13.96 | 0.449 | -1.83 | 0.718 | False |
| 2026-08-09 12:11 | 5000 | -13.96 | 0.449 | -1.83 | 0.719 | False |
| 2026-08-09 16:09 | 5000 | -13.98 | 0.448 | -2.9 | 0.63 | False |
| 2026-08-09 20:09 | 5000 | -13.97 | 0.448 | -2.95 | 0.628 | False |
| 2026-08-10 00:21 | 5000 | -13.75 | 0.454 | -3.62 | 0.579 | False |
| 2026-08-10 04:33 | 5000 | -14.4 | 0.442 | -4.5 | 0.514 | False |
| 2026-08-10 08:35 | 5000 | -15.81 | 0.403 | -4.46 | 0.518 | False |
| 2026-08-10 12:19 | 5000 | -15.68 | 0.405 | -6.67 | 0.263 | False |
| 2026-08-10 16:19 | 5000 | -14.86 | 0.421 | -7.19 | 0.187 | False |
| 2026-08-10 20:15 | 5000 | -14.89 | 0.421 | -7.38 | 0.181 | False |

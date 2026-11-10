# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-11-10 04:08_

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

- Current-params net profit (full sample): **-14.94%**, PF 0.413, 67 trades, max DD -1537.81
- Optimizer out-of-sample: net **-5.83%**, PF 0.374, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-08 16:07 | 5000 | -11.19 | 0.549 | -5.2 | 0.4 | False |
| 2026-11-08 20:07 | 5000 | -12.3 | 0.498 | -6.45 | 0.334 | False |
| 2026-11-09 00:21 | 5000 | -14.72 | 0.421 | -7.86 | 0.14 | False |
| 2026-11-09 04:10 | 5000 | -14.72 | 0.421 | -7.86 | 0.14 | False |
| 2026-11-09 08:11 | 5000 | -14.04 | 0.435 | -4.98 | 0.467 | False |
| 2026-11-09 12:11 | 5000 | -15.1 | 0.407 | -5.03 | 0.466 | False |
| 2026-11-09 16:08 | 5000 | -15.12 | 0.407 | -6.37 | 0.341 | False |
| 2026-11-09 20:07 | 5000 | -14.94 | 0.413 | -5.83 | 0.374 | False |
| 2026-11-10 00:18 | 5000 | -14.94 | 0.413 | -5.83 | 0.374 | False |
| 2026-11-10 04:08 | 5000 | -14.94 | 0.413 | -5.83 | 0.374 | False |

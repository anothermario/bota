# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-11-15 20:07_

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

- Current-params net profit (full sample): **-12.62%**, PF 0.485, 64 trades, max DD -1556.13
- Optimizer out-of-sample: net **-2.52%**, PF 0.682, 18 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-14 08:08 | 5000 | -14.92 | 0.419 | -6.68 | 0.24 | False |
| 2026-11-14 12:09 | 5000 | -15.14 | 0.409 | -5.5 | 0.355 | False |
| 2026-11-14 16:07 | 5000 | -15.21 | 0.407 | -5.52 | 0.355 | False |
| 2026-11-14 20:07 | 5000 | -15.04 | 0.414 | -5.52 | 0.355 | False |
| 2026-11-15 00:21 | 5000 | -16.54 | 0.349 | -5.52 | 0.355 | False |
| 2026-11-15 04:08 | 5000 | -13.35 | 0.469 | -2.24 | 0.739 | False |
| 2026-11-15 08:09 | 5000 | -13.49 | 0.466 | -1.59 | 0.8 | False |
| 2026-11-15 12:10 | 5000 | -12.62 | 0.485 | -2.62 | 0.674 | False |
| 2026-11-15 16:07 | 5000 | -12.62 | 0.485 | -3.27 | 0.622 | False |
| 2026-11-15 20:07 | 5000 | -12.62 | 0.485 | -2.52 | 0.682 | False |

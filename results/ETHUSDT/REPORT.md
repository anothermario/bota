# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-29 16:09_

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

- Current-params net profit (full sample): **-10.82%**, PF 0.564, 77 trades, max DD -1082.38
- Optimizer out-of-sample: net **-3.65%**, PF 0.489, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-28 04:10 | 5000 | -10.77 | 0.562 | -3.5 | 0.476 | False |
| 2026-10-28 08:11 | 5000 | -10.8 | 0.562 | -3.73 | 0.439 | False |
| 2026-10-28 12:12 | 5000 | -10.6 | 0.567 | -3.74 | 0.439 | False |
| 2026-10-28 16:09 | 5000 | -10.0 | 0.583 | -3.25 | 0.474 | False |
| 2026-10-28 20:09 | 5000 | -10.33 | 0.575 | -3.28 | 0.474 | False |
| 2026-10-29 00:22 | 5000 | -10.8 | 0.563 | -3.79 | 0.437 | False |
| 2026-10-29 04:10 | 5000 | -10.52 | 0.571 | -3.82 | 0.437 | False |
| 2026-10-29 08:11 | 5000 | -10.8 | 0.564 | -4.12 | 0.416 | False |
| 2026-10-29 12:13 | 5000 | -10.8 | 0.564 | -3.62 | 0.489 | False |
| 2026-10-29 16:09 | 5000 | -10.82 | 0.564 | -3.65 | 0.489 | False |

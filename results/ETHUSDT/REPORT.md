# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-08-08 20:08_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.25,
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

- Current-params net profit (full sample): **-20.92%**, PF 0.368, 101 trades, max DD -2142.03
- Optimizer out-of-sample: net **-4.14%**, PF 0.448, 33 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-07 08:26 | 5000 | -20.44 | 0.371 | -4.59 | 0.418 | False |
| 2026-08-07 12:18 | 5000 | -20.44 | 0.371 | -4.69 | 0.415 | False |
| 2026-08-07 16:19 | 5000 | -20.5 | 0.372 | -5.21 | 0.388 | False |
| 2026-08-07 20:14 | 5000 | -20.52 | 0.372 | -4.49 | 0.427 | False |
| 2026-08-08 00:19 | 5000 | -20.15 | 0.392 | -5.12 | 0.394 | False |
| 2026-08-08 04:25 | 5000 | -20.62 | 0.375 | -4.87 | 0.406 | False |
| 2026-08-08 08:14 | 5000 | -21.45 | 0.36 | -4.86 | 0.406 | False |
| 2026-08-08 12:10 | 5000 | -20.74 | 0.37 | -5.05 | 0.397 | False |
| 2026-08-08 16:08 | 5000 | -20.77 | 0.37 | -5.11 | 0.396 | False |
| 2026-08-08 20:08 | 5000 | -20.92 | 0.368 | -4.14 | 0.448 | False |

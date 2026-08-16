# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-16 16:05_

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

- Current-params net profit (full sample): **-12.04%**, PF 0.389, 67 trades, max DD -1238.73
- Optimizer out-of-sample: net **-1.72%**, PF 0.482, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-15 04:10 | 5000 | -12.41 | 0.437 | -2.54 | 0.412 | False |
| 2026-08-15 08:07 | 5000 | -12.76 | 0.406 | -2.91 | 0.377 | False |
| 2026-08-15 12:06 | 5000 | -13.76 | 0.352 | -2.69 | 0.366 | False |
| 2026-08-15 16:05 | 5000 | -13.76 | 0.352 | -1.71 | 0.557 | False |
| 2026-08-15 20:04 | 5000 | -13.76 | 0.352 | -2.37 | 0.396 | False |
| 2026-08-16 00:14 | 5000 | -13.76 | 0.352 | -1.68 | 0.482 | False |
| 2026-08-16 04:14 | 5000 | -13.08 | 0.366 | -1.68 | 0.482 | False |
| 2026-08-16 08:07 | 5000 | -13.04 | 0.367 | -1.68 | 0.482 | False |
| 2026-08-16 12:06 | 5000 | -12.08 | 0.387 | -1.91 | 0.45 | False |
| 2026-08-16 16:05 | 5000 | -12.04 | 0.389 | -1.72 | 0.482 | False |

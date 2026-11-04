# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-11-04 20:07_

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
  "atr_mult": 3.0,
  "chand_len": 18,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-12.89%**, PF 0.482, 75 trades, max DD -1574.64
- Optimizer out-of-sample: net **-8.57%**, PF 0.226, 29 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-03 08:10 | 5000 | -12.45 | 0.481 | -7.8 | 0.309 | False |
| 2026-11-03 12:10 | 5000 | -12.45 | 0.481 | -8.81 | 0.217 | False |
| 2026-11-03 16:08 | 5000 | -12.71 | 0.476 | -9.2 | 0.209 | False |
| 2026-11-03 20:07 | 5000 | -12.71 | 0.476 | -9.2 | 0.209 | False |
| 2026-11-04 00:19 | 5000 | -13.22 | 0.467 | -9.74 | 0.2 | False |
| 2026-11-04 04:08 | 5000 | -13.23 | 0.472 | -9.04 | 0.257 | False |
| 2026-11-04 08:10 | 5000 | -12.88 | 0.481 | -9.78 | 0.242 | False |
| 2026-11-04 12:10 | 5000 | -12.71 | 0.485 | -9.79 | 0.241 | False |
| 2026-11-04 16:07 | 5000 | -13.09 | 0.477 | -10.2 | 0.234 | False |
| 2026-11-04 20:07 | 5000 | -12.89 | 0.482 | -8.57 | 0.226 | False |

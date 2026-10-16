# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-10-16 20:10_

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

- Current-params net profit (full sample): **-12.06%**, PF 0.469, 62 trades, max DD -1206.39
- Optimizer out-of-sample: net **-3.83%**, PF 0.345, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-15 08:15 | 5000 | -11.75 | 0.472 | -2.99 | 0.402 | False |
| 2026-10-15 12:16 | 5000 | -10.14 | 0.526 | -2.99 | 0.402 | False |
| 2026-10-15 16:12 | 5000 | -10.97 | 0.505 | -3.78 | 0.347 | False |
| 2026-10-15 20:10 | 5000 | -11.95 | 0.47 | -4.3 | 0.317 | False |
| 2026-10-16 00:27 | 5000 | -11.42 | 0.482 | -3.59 | 0.359 | False |
| 2026-10-16 04:12 | 5000 | -11.42 | 0.482 | -3.59 | 0.359 | False |
| 2026-10-16 08:15 | 5000 | -11.42 | 0.482 | -3.59 | 0.359 | False |
| 2026-10-16 12:16 | 5000 | -11.42 | 0.482 | -3.57 | 0.361 | False |
| 2026-10-16 16:12 | 5000 | -11.42 | 0.482 | -3.17 | 0.389 | False |
| 2026-10-16 20:10 | 5000 | -12.06 | 0.469 | -3.83 | 0.345 | False |

# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-16 00:14_

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

- Current-params net profit (full sample): **-13.76%**, PF 0.352, 70 trades, max DD -1376.36
- Optimizer out-of-sample: net **-1.68%**, PF 0.482, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-14 12:18 | 5000 | -12.35 | 0.438 | -2.3 | 0.46 | False |
| 2026-08-14 16:18 | 5000 | -12.47 | 0.434 | -2.36 | 0.449 | False |
| 2026-08-14 20:11 | 5000 | -11.84 | 0.449 | -2.51 | 0.412 | False |
| 2026-08-15 00:14 | 5000 | -11.85 | 0.449 | -2.51 | 0.412 | False |
| 2026-08-15 04:10 | 5000 | -12.41 | 0.437 | -2.54 | 0.412 | False |
| 2026-08-15 08:07 | 5000 | -12.76 | 0.406 | -2.91 | 0.377 | False |
| 2026-08-15 12:06 | 5000 | -13.76 | 0.352 | -2.69 | 0.366 | False |
| 2026-08-15 16:05 | 5000 | -13.76 | 0.352 | -1.71 | 0.557 | False |
| 2026-08-15 20:04 | 5000 | -13.76 | 0.352 | -2.37 | 0.396 | False |
| 2026-08-16 00:14 | 5000 | -13.76 | 0.352 | -1.68 | 0.482 | False |

# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-11-14 12:09_

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

- Current-params net profit (full sample): **-15.14%**, PF 0.385, 76 trades, max DD -1513.57
- Optimizer out-of-sample: net **-4.25%**, PF 0.494, 26 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-13 00:19 | 5000 | -14.46 | 0.384 | -6.57 | 0.184 | False |
| 2026-11-13 04:08 | 5000 | -14.48 | 0.384 | -6.07 | 0.198 | False |
| 2026-11-13 08:10 | 5000 | -13.42 | 0.428 | -4.9 | 0.35 | False |
| 2026-11-13 12:10 | 5000 | -13.42 | 0.428 | -4.57 | 0.366 | False |
| 2026-11-13 16:07 | 5000 | -14.03 | 0.417 | -5.17 | 0.338 | False |
| 2026-11-13 20:07 | 5000 | -14.03 | 0.417 | -4.68 | 0.467 | False |
| 2026-11-14 00:19 | 5000 | -14.04 | 0.417 | -4.58 | 0.472 | False |
| 2026-11-14 04:08 | 5000 | -15.07 | 0.389 | -4.63 | 0.471 | False |
| 2026-11-14 08:08 | 5000 | -15.16 | 0.385 | -4.25 | 0.494 | False |
| 2026-11-14 12:09 | 5000 | -15.14 | 0.385 | -4.25 | 0.494 | False |

# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-16 04:14_

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

- Current-params net profit (full sample): **-16.11%**, PF 0.322, 58 trades, max DD -1636.24
- Optimizer out-of-sample: net **-3.5%**, PF 0.289, 14 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-14 16:19 | 5000 | -15.2 | 0.39 | -2.96 | 0.386 | False |
| 2026-08-14 20:11 | 5000 | -15.15 | 0.381 | -3.46 | 0.289 | False |
| 2026-08-15 00:14 | 5000 | -14.31 | 0.417 | -3.46 | 0.289 | False |
| 2026-08-15 04:11 | 5000 | -14.24 | 0.42 | -3.98 | 0.26 | False |
| 2026-08-15 08:07 | 5000 | -14.72 | 0.412 | -3.08 | 0.376 | False |
| 2026-08-15 12:06 | 5000 | -15.27 | 0.361 | -3.46 | 0.289 | False |
| 2026-08-15 16:05 | 5000 | -15.45 | 0.352 | -3.46 | 0.289 | False |
| 2026-08-15 20:05 | 5000 | -16.16 | 0.321 | -3.46 | 0.289 | False |
| 2026-08-16 00:14 | 5000 | -16.04 | 0.323 | -3.46 | 0.289 | False |
| 2026-08-16 04:14 | 5000 | -16.11 | 0.322 | -3.5 | 0.289 | False |

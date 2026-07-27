# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-27 21:08_

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

- Current-params net profit (full sample): **-16.14%**, PF 0.403, 73 trades, max DD -1619.93
- Optimizer out-of-sample: net **-6.96%**, PF 0.33, 27 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-26 09:58 | 5000 | -15.28 | 0.417 | -6.28 | 0.351 | False |
| 2026-07-26 13:19 | 5000 | -15.28 | 0.417 | -6.28 | 0.351 | False |
| 2026-07-26 16:59 | 5000 | -15.28 | 0.417 | -6.28 | 0.351 | False |
| 2026-07-26 20:56 | 5000 | -15.28 | 0.417 | -6.11 | 0.358 | False |
| 2026-07-27 02:48 | 5000 | -15.39 | 0.415 | -6.24 | 0.354 | False |
| 2026-07-27 07:29 | 5000 | -15.42 | 0.415 | -6.52 | 0.344 | False |
| 2026-07-27 11:19 | 5000 | -15.63 | 0.412 | -6.38 | 0.349 | False |
| 2026-07-27 14:30 | 5000 | -15.63 | 0.412 | -6.38 | 0.349 | False |
| 2026-07-27 17:41 | 5000 | -15.63 | 0.412 | -6.38 | 0.349 | False |
| 2026-07-27 21:08 | 5000 | -16.14 | 0.403 | -6.96 | 0.33 | False |

# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-28 14:03_

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

- Current-params net profit (full sample): **-15.76%**, PF 0.41, 73 trades, max DD -1644.23
- Optimizer out-of-sample: net **-6.59%**, PF 0.343, 26 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-27 02:48 | 5000 | -15.39 | 0.415 | -6.24 | 0.354 | False |
| 2026-07-27 07:29 | 5000 | -15.42 | 0.415 | -6.52 | 0.344 | False |
| 2026-07-27 11:19 | 5000 | -15.63 | 0.412 | -6.38 | 0.349 | False |
| 2026-07-27 14:30 | 5000 | -15.63 | 0.412 | -6.38 | 0.349 | False |
| 2026-07-27 17:41 | 5000 | -15.63 | 0.412 | -6.38 | 0.349 | False |
| 2026-07-27 21:08 | 5000 | -16.14 | 0.403 | -6.96 | 0.33 | False |
| 2026-07-28 02:27 | 5000 | -15.66 | 0.412 | -6.67 | 0.341 | False |
| 2026-07-28 06:25 | 5000 | -15.77 | 0.41 | -6.59 | 0.343 | False |
| 2026-07-28 10:33 | 5000 | -15.76 | 0.41 | -6.59 | 0.343 | False |
| 2026-07-28 14:03 | 5000 | -15.76 | 0.41 | -6.59 | 0.343 | False |

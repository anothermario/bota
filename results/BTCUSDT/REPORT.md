# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-10 00:29_

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

- Current-params net profit (full sample): **-7.95%**, PF 0.555, 65 trades, max DD -884.99
- Optimizer out-of-sample: net **-3.94%**, PF 0.432, 15 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-08 12:17 | 5000 | -8.83 | 0.527 | -5.39 | 0.351 | False |
| 2026-09-08 16:13 | 5000 | -8.92 | 0.522 | -3.94 | 0.429 | False |
| 2026-09-08 20:11 | 5000 | -8.92 | 0.522 | -5.39 | 0.351 | False |
| 2026-09-09 00:31 | 5000 | -8.44 | 0.537 | -5.06 | 0.367 | False |
| 2026-09-09 04:13 | 5000 | -8.86 | 0.524 | -3.17 | 0.527 | False |
| 2026-09-09 08:15 | 5000 | -8.48 | 0.537 | -2.82 | 0.519 | False |
| 2026-09-09 12:16 | 5000 | -8.64 | 0.532 | -3.91 | 0.432 | False |
| 2026-09-09 16:12 | 5000 | -8.65 | 0.531 | -3.91 | 0.432 | False |
| 2026-09-09 20:10 | 5000 | -7.92 | 0.555 | -2.44 | 0.553 | False |
| 2026-09-10 00:29 | 5000 | -7.95 | 0.555 | -3.94 | 0.432 | False |

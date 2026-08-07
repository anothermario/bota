# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-08-07 08:26_

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

- Current-params net profit (full sample): **-20.44%**, PF 0.371, 99 trades, max DD -2044.08
- Optimizer out-of-sample: net **-4.59%**, PF 0.418, 31 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-05 16:35 | 5000 | -16.57 | 0.499 | -5.16 | 0.418 | False |
| 2026-08-05 20:32 | 5000 | -16.97 | 0.485 | -5.02 | 0.422 | False |
| 2026-08-06 00:31 | 5000 | -17.33 | 0.478 | -5.36 | 0.404 | False |
| 2026-08-06 05:05 | 5000 | -17.18 | 0.484 | -4.9 | 0.374 | False |
| 2026-08-06 08:58 | 5000 | -17.75 | 0.463 | -4.87 | 0.375 | False |
| 2026-08-06 12:41 | 5000 | -19.64 | 0.404 | -4.09 | 0.447 | False |
| 2026-08-06 21:58 | 5000 | -20.14 | 0.377 | -3.72 | 0.472 | False |
| 2026-08-07 01:16 | 5000 | -20.47 | 0.373 | -4.37 | 0.432 | False |
| 2026-08-07 04:41 | 5000 | -19.99 | 0.38 | -4.37 | 0.432 | False |
| 2026-08-07 08:26 | 5000 | -20.44 | 0.371 | -4.59 | 0.418 | False |

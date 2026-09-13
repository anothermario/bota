# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-13 12:15_

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

- Current-params net profit (full sample): **-16.54%**, PF 0.409, 101 trades, max DD -1666.48
- Optimizer out-of-sample: net **-5.59%**, PF 0.455, 29 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-12 00:29 | 5000 | -16.81 | 0.4 | -5.59 | 0.434 | False |
| 2026-09-12 04:12 | 5000 | -16.54 | 0.405 | -6.47 | 0.396 | False |
| 2026-09-12 08:13 | 5000 | -16.65 | 0.403 | -6.32 | 0.403 | False |
| 2026-09-12 12:14 | 5000 | -17.1 | 0.396 | -5.7 | 0.43 | False |
| 2026-09-12 16:11 | 5000 | -17.11 | 0.395 | -5.86 | 0.423 | False |
| 2026-09-12 20:10 | 5000 | -16.79 | 0.407 | -5.27 | 0.474 | False |
| 2026-09-13 00:34 | 5000 | -16.97 | 0.404 | -5.47 | 0.463 | False |
| 2026-09-13 04:12 | 5000 | -16.95 | 0.404 | -5.79 | 0.393 | False |
| 2026-09-13 08:14 | 5000 | -16.24 | 0.416 | -5.56 | 0.455 | False |
| 2026-09-13 12:15 | 5000 | -16.54 | 0.409 | -5.59 | 0.455 | False |

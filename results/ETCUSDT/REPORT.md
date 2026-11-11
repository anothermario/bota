# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-11-11 16:08_

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

- Current-params net profit (full sample): **-14.18%**, PF 0.428, 65 trades, max DD -1551.54
- Optimizer out-of-sample: net **-5.73%**, PF 0.4, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-10 04:08 | 5000 | -14.94 | 0.413 | -5.83 | 0.374 | False |
| 2026-11-10 08:10 | 5000 | -14.53 | 0.421 | -5.18 | 0.404 | False |
| 2026-11-10 12:10 | 5000 | -14.53 | 0.421 | -4.26 | 0.454 | False |
| 2026-11-10 16:08 | 5000 | -14.53 | 0.421 | -5.69 | 0.342 | False |
| 2026-11-10 20:07 | 5000 | -14.53 | 0.421 | -4.55 | 0.459 | False |
| 2026-11-11 00:19 | 5000 | -14.53 | 0.421 | -4.05 | 0.489 | False |
| 2026-11-11 04:08 | 5000 | -14.53 | 0.421 | -4.7 | 0.451 | False |
| 2026-11-11 08:10 | 5000 | -14.53 | 0.421 | -4.7 | 0.451 | False |
| 2026-11-11 12:11 | 5000 | -14.18 | 0.428 | -4.7 | 0.451 | False |
| 2026-11-11 16:08 | 5000 | -14.18 | 0.428 | -5.73 | 0.4 | False |

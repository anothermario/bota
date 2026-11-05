# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-11-05 08:11_

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

- Current-params net profit (full sample): **-14.66%**, PF 0.441, 69 trades, max DD -1548.39
- Optimizer out-of-sample: net **-3.52%**, PF 0.565, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-03 20:07 | 5000 | -14.73 | 0.437 | -4.33 | 0.506 | False |
| 2026-11-04 00:19 | 5000 | -14.72 | 0.437 | -4.4 | 0.502 | False |
| 2026-11-04 04:08 | 5000 | -14.22 | 0.448 | -4.32 | 0.511 | False |
| 2026-11-04 08:10 | 5000 | -14.22 | 0.448 | -4.32 | 0.511 | False |
| 2026-11-04 12:10 | 5000 | -13.94 | 0.454 | -4.34 | 0.511 | False |
| 2026-11-04 16:07 | 5000 | -14.33 | 0.447 | -4.71 | 0.491 | False |
| 2026-11-04 20:07 | 5000 | -13.9 | 0.456 | -3.99 | 0.534 | False |
| 2026-11-05 00:20 | 5000 | -14.42 | 0.445 | -3.25 | 0.586 | False |
| 2026-11-05 04:09 | 5000 | -14.66 | 0.441 | -3.52 | 0.565 | False |
| 2026-11-05 08:11 | 5000 | -14.66 | 0.441 | -3.52 | 0.565 | False |

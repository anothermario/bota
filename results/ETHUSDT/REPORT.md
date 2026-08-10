# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-08-10 04:33_

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

- Current-params net profit (full sample): **-22.1%**, PF 0.332, 101 trades, max DD -2209.72
- Optimizer out-of-sample: net **-5.37%**, PF 0.305, 28 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-08 16:08 | 5000 | -20.77 | 0.37 | -5.11 | 0.396 | False |
| 2026-08-08 20:08 | 5000 | -20.92 | 0.368 | -4.14 | 0.448 | False |
| 2026-08-09 00:20 | 5000 | -20.95 | 0.368 | -3.85 | 0.469 | False |
| 2026-08-09 04:29 | 5000 | -20.44 | 0.376 | -4.07 | 0.456 | False |
| 2026-08-09 08:15 | 5000 | -20.54 | 0.374 | -4.33 | 0.44 | False |
| 2026-08-09 12:11 | 5000 | -21.21 | 0.353 | -4.57 | 0.365 | False |
| 2026-08-09 16:09 | 5000 | -22.24 | 0.329 | -4.57 | 0.365 | False |
| 2026-08-09 20:09 | 5000 | -22.24 | 0.329 | -4.57 | 0.365 | False |
| 2026-08-10 00:21 | 5000 | -22.1 | 0.332 | -5.65 | 0.293 | False |
| 2026-08-10 04:33 | 5000 | -22.1 | 0.332 | -5.37 | 0.305 | False |

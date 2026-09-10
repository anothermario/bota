# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-10 20:10_

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

- Current-params net profit (full sample): **-15.07%**, PF 0.433, 95 trades, max DD -1596.8
- Optimizer out-of-sample: net **-3.89%**, PF 0.487, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-09 08:15 | 5000 | -15.04 | 0.43 | -3.5 | 0.502 | False |
| 2026-09-09 12:16 | 5000 | -15.85 | 0.417 | -4.29 | 0.451 | False |
| 2026-09-09 16:12 | 5000 | -15.85 | 0.417 | -4.27 | 0.453 | False |
| 2026-09-09 20:11 | 5000 | -15.55 | 0.423 | -4.89 | 0.42 | False |
| 2026-09-10 00:29 | 5000 | -15.31 | 0.427 | -4.16 | 0.459 | False |
| 2026-09-10 04:13 | 5000 | -14.51 | 0.442 | -4.18 | 0.458 | False |
| 2026-09-10 08:15 | 5000 | -14.95 | 0.434 | -4.02 | 0.471 | False |
| 2026-09-10 12:16 | 5000 | -14.95 | 0.436 | -4.71 | 0.429 | False |
| 2026-09-10 16:11 | 5000 | -15.03 | 0.434 | -4.92 | 0.419 | False |
| 2026-09-10 20:10 | 5000 | -15.07 | 0.433 | -3.89 | 0.487 | False |

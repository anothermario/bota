# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-17 12:17_

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

- Current-params net profit (full sample): **-16.29%**, PF 0.408, 100 trades, max DD -1643.66
- Optimizer out-of-sample: net **-5.82%**, PF 0.488, 33 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-16 00:30 | 5000 | -15.55 | 0.452 | -5.94 | 0.478 | False |
| 2026-09-16 04:13 | 5000 | -15.26 | 0.458 | -6.95 | 0.437 | False |
| 2026-09-16 08:16 | 5000 | -15.29 | 0.457 | -6.29 | 0.463 | False |
| 2026-09-16 12:17 | 5000 | -15.81 | 0.43 | -5.59 | 0.494 | False |
| 2026-09-16 16:13 | 5000 | -15.64 | 0.433 | -5.58 | 0.495 | False |
| 2026-09-16 20:12 | 5000 | -17.26 | 0.388 | -6.12 | 0.473 | False |
| 2026-09-17 00:30 | 5000 | -16.79 | 0.396 | -6.11 | 0.473 | False |
| 2026-09-17 04:14 | 5000 | -16.96 | 0.393 | -6.76 | 0.447 | False |
| 2026-09-17 08:16 | 5000 | -17.0 | 0.393 | -6.0 | 0.48 | False |
| 2026-09-17 12:17 | 5000 | -16.29 | 0.408 | -5.82 | 0.488 | False |

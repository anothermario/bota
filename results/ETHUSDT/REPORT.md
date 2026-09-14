# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-14 12:18_

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

- Current-params net profit (full sample): **-15.85%**, PF 0.424, 101 trades, max DD -1709.95
- Optimizer out-of-sample: net **-5.96%**, PF 0.449, 33 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-13 00:34 | 5000 | -16.97 | 0.404 | -5.47 | 0.463 | False |
| 2026-09-13 04:12 | 5000 | -16.95 | 0.404 | -5.79 | 0.393 | False |
| 2026-09-13 08:14 | 5000 | -16.24 | 0.416 | -5.56 | 0.455 | False |
| 2026-09-13 12:15 | 5000 | -16.54 | 0.409 | -5.59 | 0.455 | False |
| 2026-09-13 16:11 | 5000 | -16.21 | 0.418 | -5.33 | 0.477 | False |
| 2026-09-13 20:10 | 5000 | -16.18 | 0.419 | -5.08 | 0.507 | False |
| 2026-09-14 00:33 | 5000 | -15.83 | 0.437 | -5.41 | 0.475 | False |
| 2026-09-14 04:14 | 5000 | -15.06 | 0.452 | -5.68 | 0.462 | False |
| 2026-09-14 08:18 | 5000 | -15.07 | 0.452 | -5.68 | 0.462 | False |
| 2026-09-14 12:18 | 5000 | -15.85 | 0.424 | -5.96 | 0.449 | False |

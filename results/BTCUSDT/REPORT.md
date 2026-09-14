# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-14 20:11_

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

- Current-params net profit (full sample): **-8.73%**, PF 0.505, 66 trades, max DD -877.98
- Optimizer out-of-sample: net **-5.09%**, PF 0.371, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-13 08:14 | 5000 | -7.41 | 0.564 | -4.12 | 0.419 | False |
| 2026-09-13 12:15 | 5000 | -6.98 | 0.58 | -4.61 | 0.393 | False |
| 2026-09-13 16:11 | 5000 | -7.04 | 0.577 | -4.22 | 0.413 | False |
| 2026-09-13 20:10 | 5000 | -7.73 | 0.554 | -4.26 | 0.413 | False |
| 2026-09-14 00:33 | 5000 | -8.12 | 0.541 | -4.68 | 0.39 | False |
| 2026-09-14 04:14 | 5000 | -8.18 | 0.541 | -4.98 | 0.376 | False |
| 2026-09-14 08:17 | 5000 | -9.44 | 0.482 | -6.39 | 0.318 | False |
| 2026-09-14 12:17 | 5000 | -8.93 | 0.497 | -5.06 | 0.371 | False |
| 2026-09-14 16:11 | 5000 | -8.93 | 0.497 | -5.06 | 0.371 | False |
| 2026-09-14 20:11 | 5000 | -8.73 | 0.505 | -5.09 | 0.371 | False |

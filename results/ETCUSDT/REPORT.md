# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-18 20:06_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.3,
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

- Current-params net profit (full sample): **-13.88%**, PF 0.406, 58 trades, max DD -1501.75
- Optimizer out-of-sample: net **-3.06%**, PF 0.425, 15 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-17 08:15 | 5000 | -15.26 | 0.356 | -5.47 | 0.193 | False |
| 2026-08-17 12:08 | 5000 | -14.45 | 0.371 | -4.0 | 0.249 | False |
| 2026-08-17 16:06 | 5000 | -14.98 | 0.359 | -4.0 | 0.249 | False |
| 2026-08-17 20:07 | 5000 | -14.51 | 0.368 | -4.0 | 0.249 | False |
| 2026-08-18 00:14 | 5000 | -14.55 | 0.368 | -4.0 | 0.249 | False |
| 2026-08-18 04:15 | 5000 | -13.62 | 0.405 | -4.04 | 0.249 | False |
| 2026-08-18 08:11 | 5000 | -13.6 | 0.406 | -4.78 | 0.217 | False |
| 2026-08-18 12:09 | 5000 | -13.41 | 0.416 | -6.55 | 0.301 | False |
| 2026-08-18 16:08 | 5000 | -14.59 | 0.393 | -3.06 | 0.425 | False |
| 2026-08-18 20:06 | 5000 | -13.88 | 0.406 | -3.06 | 0.425 | False |

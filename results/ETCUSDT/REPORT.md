# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-16 13:48_

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
  "chand_len": 18,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-11.08%**, PF 0.537, 64 trades, max DD -1167.66
- Optimizer out-of-sample: net **-3.63%**, PF 0.362, 14 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-15 02:22 | 5000 | -12.11 | 0.513 | -3.02 | 0.412 | False |
| 2026-07-15 06:13 | 5000 | -12.08 | 0.515 | -3.64 | 0.362 | False |
| 2026-07-15 10:01 | 5000 | -11.82 | 0.522 | -3.83 | 0.362 | False |
| 2026-07-15 13:41 | 5000 | -11.82 | 0.523 | -3.99 | 0.339 | False |
| 2026-07-15 17:16 | 5000 | -12.68 | 0.498 | -5.5 | 0.27 | False |
| 2026-07-15 20:59 | 5000 | -12.44 | 0.504 | -4.33 | 0.338 | False |
| 2026-07-16 02:30 | 5000 | -12.42 | 0.504 | -3.69 | 0.405 | False |
| 2026-07-16 06:17 | 5000 | -12.44 | 0.504 | -4.47 | 0.315 | False |
| 2026-07-16 10:08 | 5000 | -11.84 | 0.518 | -3.99 | 0.341 | False |
| 2026-07-16 13:48 | 5000 | -11.08 | 0.537 | -3.63 | 0.362 | False |

# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-17 13:25_

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

- Current-params net profit (full sample): **-13.02%**, PF 0.483, 65 trades, max DD -1301.62
- Optimizer out-of-sample: net **-4.81%**, PF 0.3, 15 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-16 02:30 | 5000 | -12.42 | 0.504 | -3.69 | 0.405 | False |
| 2026-07-16 06:17 | 5000 | -12.44 | 0.504 | -4.47 | 0.315 | False |
| 2026-07-16 10:08 | 5000 | -11.84 | 0.518 | -3.99 | 0.341 | False |
| 2026-07-16 13:48 | 5000 | -11.08 | 0.537 | -3.63 | 0.362 | False |
| 2026-07-16 17:14 | 5000 | -11.14 | 0.535 | -4.0 | 0.339 | False |
| 2026-07-16 20:56 | 5000 | -11.9 | 0.505 | -4.19 | 0.33 | False |
| 2026-07-17 02:33 | 5000 | -12.26 | 0.498 | -3.63 | 0.362 | False |
| 2026-07-17 06:14 | 5000 | -12.29 | 0.498 | -3.66 | 0.362 | False |
| 2026-07-17 09:56 | 5000 | -13.01 | 0.483 | -4.46 | 0.316 | False |
| 2026-07-17 13:25 | 5000 | -13.02 | 0.483 | -4.81 | 0.3 | False |

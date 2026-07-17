# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-17 20:53_

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

- Current-params net profit (full sample): **-13.45%**, PF 0.475, 65 trades, max DD -1345.05
- Optimizer out-of-sample: net **-5.84%**, PF 0.26, 17 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-16 10:08 | 5000 | -11.84 | 0.518 | -3.99 | 0.341 | False |
| 2026-07-16 13:48 | 5000 | -11.08 | 0.537 | -3.63 | 0.362 | False |
| 2026-07-16 17:14 | 5000 | -11.14 | 0.535 | -4.0 | 0.339 | False |
| 2026-07-16 20:56 | 5000 | -11.9 | 0.505 | -4.19 | 0.33 | False |
| 2026-07-17 02:33 | 5000 | -12.26 | 0.498 | -3.63 | 0.362 | False |
| 2026-07-17 06:14 | 5000 | -12.29 | 0.498 | -3.66 | 0.362 | False |
| 2026-07-17 09:56 | 5000 | -13.01 | 0.483 | -4.46 | 0.316 | False |
| 2026-07-17 13:25 | 5000 | -13.02 | 0.483 | -4.81 | 0.3 | False |
| 2026-07-17 17:10 | 5000 | -12.77 | 0.489 | -4.48 | 0.317 | False |
| 2026-07-17 20:53 | 5000 | -13.45 | 0.475 | -5.84 | 0.26 | False |

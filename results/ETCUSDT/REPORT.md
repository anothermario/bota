# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-08 21:07_

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

- Current-params net profit (full sample): **-12.8%**, PF 0.526, 73 trades, max DD -1279.72
- Optimizer out-of-sample: net **-5.81%**, PF 0.336, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-07 10:54 | 5000 | -13.01 | 0.528 | -6.75 | 0.303 | False |
| 2026-07-07 14:31 | 5000 | -13.36 | 0.513 | -6.75 | 0.303 | False |
| 2026-07-07 17:58 | 5000 | -13.65 | 0.507 | -6.89 | 0.298 | False |
| 2026-07-07 21:23 | 5000 | -14.04 | 0.499 | -6.59 | 0.324 | False |
| 2026-07-08 02:35 | 5000 | -13.43 | 0.512 | -5.66 | 0.361 | False |
| 2026-07-08 06:27 | 5000 | -13.01 | 0.521 | -5.97 | 0.331 | False |
| 2026-07-08 10:17 | 5000 | -13.01 | 0.521 | -5.87 | 0.335 | False |
| 2026-07-08 14:03 | 5000 | -13.03 | 0.521 | -5.87 | 0.335 | False |
| 2026-07-08 17:28 | 5000 | -12.99 | 0.521 | -6.57 | 0.309 | False |
| 2026-07-08 21:07 | 5000 | -12.8 | 0.526 | -5.81 | 0.336 | False |

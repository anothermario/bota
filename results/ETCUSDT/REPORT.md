# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-08 14:03_

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

- Current-params net profit (full sample): **-13.03%**, PF 0.521, 74 trades, max DD -1302.56
- Optimizer out-of-sample: net **-5.87%**, PF 0.335, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-07 03:17 | 5000 | -13.02 | 0.528 | -6.72 | 0.303 | False |
| 2026-07-07 07:37 | 5000 | -13.11 | 0.524 | -6.75 | 0.303 | False |
| 2026-07-07 10:54 | 5000 | -13.01 | 0.528 | -6.75 | 0.303 | False |
| 2026-07-07 14:31 | 5000 | -13.36 | 0.513 | -6.75 | 0.303 | False |
| 2026-07-07 17:58 | 5000 | -13.65 | 0.507 | -6.89 | 0.298 | False |
| 2026-07-07 21:23 | 5000 | -14.04 | 0.499 | -6.59 | 0.324 | False |
| 2026-07-08 02:35 | 5000 | -13.43 | 0.512 | -5.66 | 0.361 | False |
| 2026-07-08 06:27 | 5000 | -13.01 | 0.521 | -5.97 | 0.331 | False |
| 2026-07-08 10:17 | 5000 | -13.01 | 0.521 | -5.87 | 0.335 | False |
| 2026-07-08 14:03 | 5000 | -13.03 | 0.521 | -5.87 | 0.335 | False |

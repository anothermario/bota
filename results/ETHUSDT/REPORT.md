# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-08-23 04:15_

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

- Current-params net profit (full sample): **-19.46%**, PF 0.349, 106 trades, max DD -2115.69
- Optimizer out-of-sample: net **-4.77%**, PF 0.248, 27 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-21 16:09 | 5000 | -20.16 | 0.356 | -4.45 | 0.259 | False |
| 2026-08-21 20:06 | 5000 | -19.82 | 0.361 | -4.45 | 0.259 | False |
| 2026-08-22 00:14 | 5000 | -19.68 | 0.363 | -5.06 | 0.346 | False |
| 2026-08-22 04:13 | 5000 | -19.07 | 0.372 | -5.06 | 0.346 | False |
| 2026-08-22 08:08 | 5000 | -19.37 | 0.368 | -5.2 | 0.347 | False |
| 2026-08-22 12:07 | 5000 | -20.18 | 0.338 | -4.6 | 0.264 | False |
| 2026-08-22 16:05 | 5000 | -20.43 | 0.335 | -5.22 | 0.239 | False |
| 2026-08-22 20:05 | 5000 | -19.98 | 0.342 | -5.27 | 0.228 | False |
| 2026-08-23 00:14 | 5000 | -19.49 | 0.348 | -4.77 | 0.248 | False |
| 2026-08-23 04:15 | 5000 | -19.46 | 0.349 | -4.77 | 0.248 | False |

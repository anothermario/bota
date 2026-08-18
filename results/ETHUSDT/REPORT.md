# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-08-18 04:15_

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

- Current-params net profit (full sample): **-19.66%**, PF 0.351, 101 trades, max DD -2013.52
- Optimizer out-of-sample: net **-5.57%**, PF 0.258, 24 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-16 16:05 | 5000 | -21.04 | 0.326 | -6.64 | 0.22 | False |
| 2026-08-16 20:04 | 5000 | -21.52 | 0.32 | -6.66 | 0.219 | False |
| 2026-08-17 00:14 | 5000 | -20.91 | 0.329 | -6.66 | 0.22 | False |
| 2026-08-17 04:17 | 5000 | -20.72 | 0.332 | -6.48 | 0.226 | False |
| 2026-08-17 08:15 | 5000 | -20.88 | 0.33 | -6.26 | 0.232 | False |
| 2026-08-17 12:08 | 5000 | -20.2 | 0.339 | -4.25 | 0.352 | False |
| 2026-08-17 16:06 | 5000 | -20.23 | 0.339 | -4.26 | 0.352 | False |
| 2026-08-17 20:07 | 5000 | -20.23 | 0.339 | -4.22 | 0.354 | False |
| 2026-08-18 00:14 | 5000 | -19.71 | 0.347 | -5.55 | 0.258 | False |
| 2026-08-18 04:15 | 5000 | -19.66 | 0.351 | -5.57 | 0.258 | False |

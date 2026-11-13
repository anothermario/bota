# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-11-13 20:07_

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
  "chand_len": 26,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-14.03%**, PF 0.417, 77 trades, max DD -1498.14
- Optimizer out-of-sample: net **-4.68%**, PF 0.467, 28 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-12 08:10 | 5000 | -15.26 | 0.36 | -6.34 | 0.149 | False |
| 2026-11-12 12:11 | 5000 | -15.27 | 0.36 | -6.34 | 0.149 | False |
| 2026-11-12 16:08 | 5000 | -14.78 | 0.378 | -6.57 | 0.184 | False |
| 2026-11-12 20:07 | 5000 | -14.79 | 0.378 | -6.56 | 0.184 | False |
| 2026-11-13 00:19 | 5000 | -14.46 | 0.384 | -6.57 | 0.184 | False |
| 2026-11-13 04:08 | 5000 | -14.48 | 0.384 | -6.07 | 0.198 | False |
| 2026-11-13 08:10 | 5000 | -13.42 | 0.428 | -4.9 | 0.35 | False |
| 2026-11-13 12:10 | 5000 | -13.42 | 0.428 | -4.57 | 0.366 | False |
| 2026-11-13 16:07 | 5000 | -14.03 | 0.417 | -5.17 | 0.338 | False |
| 2026-11-13 20:07 | 5000 | -14.03 | 0.417 | -4.68 | 0.467 | False |

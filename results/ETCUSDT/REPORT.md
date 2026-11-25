# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-11-25 20:07_

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

- Current-params net profit (full sample): **-12.65%**, PF 0.499, 66 trades, max DD -1284.15
- Optimizer out-of-sample: net **-5.51%**, PF 0.452, 27 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-24 08:10 | 5000 | -13.0 | 0.49 | -6.1 | 0.433 | False |
| 2026-11-24 12:11 | 5000 | -13.0 | 0.49 | -6.1 | 0.433 | False |
| 2026-11-24 16:08 | 5000 | -13.0 | 0.49 | -6.12 | 0.432 | False |
| 2026-11-24 20:07 | 5000 | -13.0 | 0.49 | -5.33 | 0.469 | False |
| 2026-11-25 00:19 | 5000 | -13.0 | 0.49 | -6.08 | 0.424 | False |
| 2026-11-25 04:09 | 5000 | -12.99 | 0.49 | -6.0 | 0.427 | False |
| 2026-11-25 08:10 | 5000 | -13.01 | 0.49 | -6.01 | 0.427 | False |
| 2026-11-25 12:11 | 5000 | -12.41 | 0.504 | -5.55 | 0.448 | False |
| 2026-11-25 16:09 | 5000 | -12.37 | 0.505 | -5.49 | 0.452 | False |
| 2026-11-25 20:07 | 5000 | -12.65 | 0.499 | -5.51 | 0.452 | False |

# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-14 16:19_

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

- Current-params net profit (full sample): **-15.2%**, PF 0.39, 61 trades, max DD -1648.98
- Optimizer out-of-sample: net **-2.96%**, PF 0.386, 14 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-13 04:38 | 5000 | -14.8 | 0.428 | -5.55 | 0.177 | False |
| 2026-08-13 08:33 | 5000 | -14.61 | 0.437 | -4.57 | 0.196 | False |
| 2026-08-13 12:20 | 5000 | -13.96 | 0.449 | -4.57 | 0.196 | False |
| 2026-08-13 16:20 | 5000 | -14.18 | 0.439 | -5.09 | 0.244 | False |
| 2026-08-13 20:13 | 5000 | -15.56 | 0.377 | -4.58 | 0.195 | False |
| 2026-08-14 00:26 | 5000 | -15.04 | 0.399 | -3.75 | 0.23 | False |
| 2026-08-14 04:36 | 5000 | -16.2 | 0.367 | -3.78 | 0.23 | False |
| 2026-08-14 08:31 | 5000 | -15.49 | 0.379 | -3.78 | 0.23 | False |
| 2026-08-14 12:18 | 5000 | -15.49 | 0.379 | -3.78 | 0.23 | False |
| 2026-08-14 16:19 | 5000 | -15.2 | 0.39 | -2.96 | 0.386 | False |

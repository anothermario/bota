# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-25 09:46_

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

- Current-params net profit (full sample): **-12.61%**, PF 0.511, 65 trades, max DD -1514.74
- Optimizer out-of-sample: net **-8.57%**, PF 0.249, 24 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-23 21:03 | 5000 | -15.2 | 0.433 | -8.53 | 0.143 | False |
| 2026-07-24 02:34 | 5000 | -15.55 | 0.427 | -8.25 | 0.148 | False |
| 2026-07-24 06:25 | 5000 | -15.82 | 0.423 | -8.55 | 0.143 | False |
| 2026-07-24 10:15 | 5000 | -15.82 | 0.423 | -8.55 | 0.143 | False |
| 2026-07-24 13:42 | 5000 | -15.42 | 0.431 | -8.57 | 0.143 | False |
| 2026-07-24 17:37 | 5000 | -15.42 | 0.431 | -8.57 | 0.143 | False |
| 2026-07-24 21:02 | 5000 | -14.99 | 0.439 | -8.57 | 0.143 | False |
| 2026-07-25 02:33 | 5000 | -13.45 | 0.492 | -7.82 | 0.268 | False |
| 2026-07-25 06:17 | 5000 | -12.61 | 0.511 | -8.61 | 0.248 | False |
| 2026-07-25 09:46 | 5000 | -12.61 | 0.511 | -8.57 | 0.249 | False |

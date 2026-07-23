# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-23 21:02_

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
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-12.54%**, PF 0.553, 72 trades, max DD -1734.46
- Optimizer out-of-sample: net **-8.1%**, PF 0.249, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-22 10:24 | 5000 | -11.08 | 0.607 | -8.44 | 0.241 | False |
| 2026-07-22 13:50 | 5000 | -11.08 | 0.607 | -8.08 | 0.249 | False |
| 2026-07-22 17:17 | 5000 | -10.84 | 0.613 | -8.08 | 0.249 | False |
| 2026-07-22 21:05 | 5000 | -10.84 | 0.613 | -8.08 | 0.249 | False |
| 2026-07-23 02:37 | 5000 | -11.24 | 0.597 | -8.42 | 0.241 | False |
| 2026-07-23 06:29 | 5000 | -11.76 | 0.576 | -8.42 | 0.241 | False |
| 2026-07-23 10:21 | 5000 | -12.82 | 0.545 | -8.42 | 0.241 | False |
| 2026-07-23 13:54 | 5000 | -12.11 | 0.561 | -8.09 | 0.248 | False |
| 2026-07-23 17:21 | 5000 | -12.14 | 0.561 | -7.69 | 0.26 | False |
| 2026-07-23 21:02 | 5000 | -12.54 | 0.553 | -8.1 | 0.249 | False |

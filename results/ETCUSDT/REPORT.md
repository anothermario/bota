# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-06-18 05:40_

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
  "don_len": 20,
  "atr_len": 14,
  "atr_mult": 3.0,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-12.19%**, PF 0.571, 82 trades, max DD -1627.37
- Optimizer out-of-sample: net **-0.65%**, PF 0.889, 15 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-16 17:45 | 5000 | -12.17 | 0.571 | -1.14 | 0.814 | False |
| 2026-06-16 21:06 | 5000 | -12.17 | 0.571 | -1.14 | 0.814 | False |
| 2026-06-17 00:58 | 5000 | -12.17 | 0.571 | -1.14 | 0.814 | False |
| 2026-06-17 05:43 | 5000 | -12.17 | 0.571 | -1.14 | 0.814 | False |
| 2026-06-17 09:43 | 5000 | -12.17 | 0.571 | -1.14 | 0.814 | False |
| 2026-06-17 13:21 | 5000 | -12.17 | 0.571 | -1.14 | 0.814 | False |
| 2026-06-17 17:06 | 5000 | -12.17 | 0.571 | -1.15 | 0.814 | False |
| 2026-06-17 20:47 | 5000 | -12.17 | 0.571 | -1.14 | 0.815 | False |
| 2026-06-18 00:58 | 5000 | -12.17 | 0.571 | -0.63 | 0.889 | False |
| 2026-06-18 05:40 | 5000 | -12.19 | 0.571 | -0.65 | 0.889 | False |

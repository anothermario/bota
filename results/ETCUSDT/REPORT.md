# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-06-18 17:07_

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

- Current-params net profit (full sample): **-11.9%**, PF 0.585, 82 trades, max DD -1639.32
- Optimizer out-of-sample: net **-0.56%**, PF 0.901, 15 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-17 05:43 | 5000 | -12.17 | 0.571 | -1.14 | 0.814 | False |
| 2026-06-17 09:43 | 5000 | -12.17 | 0.571 | -1.14 | 0.814 | False |
| 2026-06-17 13:21 | 5000 | -12.17 | 0.571 | -1.14 | 0.814 | False |
| 2026-06-17 17:06 | 5000 | -12.17 | 0.571 | -1.15 | 0.814 | False |
| 2026-06-17 20:47 | 5000 | -12.17 | 0.571 | -1.14 | 0.815 | False |
| 2026-06-18 00:58 | 5000 | -12.17 | 0.571 | -0.63 | 0.889 | False |
| 2026-06-18 05:40 | 5000 | -12.19 | 0.571 | -0.65 | 0.889 | False |
| 2026-06-18 09:35 | 5000 | -12.2 | 0.571 | -0.16 | 0.974 | False |
| 2026-06-18 13:15 | 5000 | -12.33 | 0.568 | -0.16 | 0.973 | False |
| 2026-06-18 17:07 | 5000 | -11.9 | 0.585 | -0.56 | 0.901 | False |

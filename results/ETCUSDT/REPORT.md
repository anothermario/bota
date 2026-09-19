# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-19 08:14_

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

- Current-params net profit (full sample): **-2.67%**, PF 0.872, 54 trades, max DD -793.52
- Optimizer out-of-sample: net **-1.85%**, PF 0.773, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-17 20:12 | 5000 | -4.76 | 0.772 | -2.79 | 0.662 | False |
| 2026-09-18 00:30 | 5000 | -4.76 | 0.772 | -2.79 | 0.662 | False |
| 2026-09-18 04:13 | 5000 | -4.78 | 0.772 | -2.82 | 0.662 | False |
| 2026-09-18 08:15 | 5000 | -4.78 | 0.772 | -2.81 | 0.662 | False |
| 2026-09-18 12:16 | 5000 | -3.05 | 0.854 | -1.05 | 0.872 | False |
| 2026-09-18 16:11 | 5000 | -3.07 | 0.854 | -1.09 | 0.87 | False |
| 2026-09-18 20:11 | 5000 | -3.07 | 0.854 | -1.23 | 0.853 | False |
| 2026-09-19 00:30 | 5000 | -3.07 | 0.854 | -1.29 | 0.845 | False |
| 2026-09-19 04:12 | 5000 | -3.06 | 0.854 | -2.26 | 0.725 | False |
| 2026-09-19 08:14 | 5000 | -2.67 | 0.872 | -1.85 | 0.773 | False |

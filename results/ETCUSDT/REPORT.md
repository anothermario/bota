# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-20 00:35_

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

- Current-params net profit (full sample): **-2.3%**, PF 0.889, 54 trades, max DD -800.36
- Optimizer out-of-sample: net **-2.25%**, PF 0.737, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-18 12:16 | 5000 | -3.05 | 0.854 | -1.05 | 0.872 | False |
| 2026-09-18 16:11 | 5000 | -3.07 | 0.854 | -1.09 | 0.87 | False |
| 2026-09-18 20:11 | 5000 | -3.07 | 0.854 | -1.23 | 0.853 | False |
| 2026-09-19 00:30 | 5000 | -3.07 | 0.854 | -1.29 | 0.845 | False |
| 2026-09-19 04:12 | 5000 | -3.06 | 0.854 | -2.26 | 0.725 | False |
| 2026-09-19 08:14 | 5000 | -2.67 | 0.872 | -1.85 | 0.773 | False |
| 2026-09-19 12:15 | 5000 | -1.84 | 0.91 | -2.47 | 0.718 | False |
| 2026-09-19 16:10 | 5000 | -2.3 | 0.889 | -2.94 | 0.681 | False |
| 2026-09-19 20:10 | 5000 | -2.3 | 0.889 | -2.32 | 0.731 | False |
| 2026-09-20 00:35 | 5000 | -2.3 | 0.889 | -2.25 | 0.737 | False |

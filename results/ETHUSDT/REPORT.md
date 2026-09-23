# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-23 16:13_

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

- Current-params net profit (full sample): **-12.14%**, PF 0.558, 98 trades, max DD -1647.56
- Optimizer out-of-sample: net **-6.05%**, PF 0.505, 37 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-22 04:13 | 5000 | -12.68 | 0.545 | -7.49 | 0.425 | False |
| 2026-09-22 08:16 | 5000 | -12.37 | 0.552 | -6.7 | 0.455 | False |
| 2026-09-22 12:17 | 5000 | -12.29 | 0.554 | -6.97 | 0.444 | False |
| 2026-09-22 16:11 | 5000 | -11.8 | 0.565 | -6.52 | 0.461 | False |
| 2026-09-22 20:10 | 5000 | -11.8 | 0.565 | -6.52 | 0.461 | False |
| 2026-09-23 00:28 | 5000 | -11.62 | 0.57 | -6.52 | 0.461 | False |
| 2026-09-23 04:14 | 5000 | -11.61 | 0.57 | -6.52 | 0.461 | False |
| 2026-09-23 08:16 | 5000 | -12.22 | 0.551 | -6.53 | 0.461 | False |
| 2026-09-23 12:17 | 5000 | -11.96 | 0.556 | -7.32 | 0.432 | False |
| 2026-09-23 16:13 | 5000 | -12.14 | 0.558 | -6.05 | 0.505 | False |

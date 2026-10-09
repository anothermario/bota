# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-09 08:18_

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

- Current-params net profit (full sample): **-15.05%**, PF 0.513, 105 trades, max DD -1620.02
- Optimizer out-of-sample: net **-6.24%**, PF 0.193, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-07 20:13 | 5000 | -15.98 | 0.485 | -7.16 | 0.14 | False |
| 2026-10-08 00:33 | 5000 | -16.18 | 0.481 | -7.16 | 0.14 | False |
| 2026-10-08 04:15 | 5000 | -15.76 | 0.489 | -7.16 | 0.14 | False |
| 2026-10-08 08:18 | 5000 | -15.76 | 0.489 | -7.16 | 0.14 | False |
| 2026-10-08 12:18 | 5000 | -15.62 | 0.492 | -7.18 | 0.141 | False |
| 2026-10-08 16:14 | 5000 | -14.92 | 0.514 | -6.4 | 0.234 | False |
| 2026-10-08 20:12 | 5000 | -14.89 | 0.516 | -7.07 | 0.173 | False |
| 2026-10-09 00:35 | 5000 | -14.67 | 0.52 | -6.78 | 0.179 | False |
| 2026-10-09 04:16 | 5000 | -15.04 | 0.513 | -6.24 | 0.193 | False |
| 2026-10-09 08:18 | 5000 | -15.05 | 0.513 | -6.24 | 0.193 | False |

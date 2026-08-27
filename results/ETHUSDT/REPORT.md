# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-08-27 11:26_

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

- Current-params net profit (full sample): **-21.21%**, PF 0.299, 104 trades, max DD -2121.3
- Optimizer out-of-sample: net **-6.34%**, PF 0.098, 27 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-25 20:07 | 5000 | -22.06 | 0.286 | -4.57 | 0.298 | False |
| 2026-08-26 00:15 | 5000 | -22.02 | 0.287 | -5.55 | 0.189 | False |
| 2026-08-26 04:16 | 5000 | -22.03 | 0.287 | -6.16 | 0.1 | False |
| 2026-08-26 08:16 | 5000 | -21.44 | 0.294 | -6.15 | 0.1 | False |
| 2026-08-26 12:11 | 5000 | -21.87 | 0.29 | -6.77 | 0.091 | False |
| 2026-08-26 16:29 | 5000 | -21.89 | 0.29 | -6.77 | 0.091 | False |
| 2026-08-26 20:50 | 5000 | -21.65 | 0.292 | -6.77 | 0.091 | False |
| 2026-08-27 01:35 | 5000 | -21.68 | 0.292 | -6.13 | 0.101 | False |
| 2026-08-27 06:08 | 5000 | -21.87 | 0.29 | -5.14 | 0.081 | False |
| 2026-08-27 11:26 | 5000 | -21.21 | 0.299 | -6.34 | 0.098 | False |

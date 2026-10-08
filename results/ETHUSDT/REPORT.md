# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-08 12:18_

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

- Current-params net profit (full sample): **-15.62%**, PF 0.492, 101 trades, max DD -1614.35
- Optimizer out-of-sample: net **-7.18%**, PF 0.141, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-07 00:34 | 5000 | -16.31 | 0.471 | -8.47 | 0.073 | False |
| 2026-10-07 04:15 | 5000 | -16.59 | 0.467 | -7.85 | 0.079 | False |
| 2026-10-07 08:17 | 5000 | -16.79 | 0.464 | -8.01 | 0.077 | False |
| 2026-10-07 12:19 | 5000 | -16.8 | 0.464 | -8.43 | 0.074 | False |
| 2026-10-07 16:13 | 5000 | -16.83 | 0.463 | -7.69 | 0.081 | False |
| 2026-10-07 20:13 | 5000 | -15.98 | 0.485 | -7.16 | 0.14 | False |
| 2026-10-08 00:33 | 5000 | -16.18 | 0.481 | -7.16 | 0.14 | False |
| 2026-10-08 04:15 | 5000 | -15.76 | 0.489 | -7.16 | 0.14 | False |
| 2026-10-08 08:18 | 5000 | -15.76 | 0.489 | -7.16 | 0.14 | False |
| 2026-10-08 12:18 | 5000 | -15.62 | 0.492 | -7.18 | 0.141 | False |

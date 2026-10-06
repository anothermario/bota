# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-06 16:14_

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

- Current-params net profit (full sample): **-15.94%**, PF 0.476, 101 trades, max DD -1593.73
- Optimizer out-of-sample: net **-6.46%**, PF 0.19, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-05 00:36 | 5000 | -14.7 | 0.496 | -4.8 | 0.38 | False |
| 2026-10-05 04:19 | 5000 | -15.08 | 0.489 | -4.93 | 0.368 | False |
| 2026-10-05 08:24 | 5000 | -14.86 | 0.494 | -5.53 | 0.29 | False |
| 2026-10-05 12:19 | 5000 | -14.86 | 0.494 | -5.5 | 0.291 | False |
| 2026-10-05 16:14 | 5000 | -15.11 | 0.489 | -5.5 | 0.291 | False |
| 2026-10-06 00:33 | 5000 | -15.15 | 0.489 | -6.15 | 0.206 | False |
| 2026-10-06 04:14 | 5000 | -15.56 | 0.482 | -6.64 | 0.194 | False |
| 2026-10-06 08:16 | 5000 | -15.48 | 0.483 | -6.39 | 0.2 | False |
| 2026-10-06 12:18 | 5000 | -16.12 | 0.473 | -6.38 | 0.201 | False |
| 2026-10-06 16:14 | 5000 | -15.94 | 0.476 | -6.46 | 0.19 | False |

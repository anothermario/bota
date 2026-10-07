# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-07 04:15_

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

- Current-params net profit (full sample): **-16.59%**, PF 0.467, 103 trades, max DD -1659.24
- Optimizer out-of-sample: net **-7.85%**, PF 0.079, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-05 12:19 | 5000 | -14.86 | 0.494 | -5.5 | 0.291 | False |
| 2026-10-05 16:14 | 5000 | -15.11 | 0.489 | -5.5 | 0.291 | False |
| 2026-10-06 00:33 | 5000 | -15.15 | 0.489 | -6.15 | 0.206 | False |
| 2026-10-06 04:14 | 5000 | -15.56 | 0.482 | -6.64 | 0.194 | False |
| 2026-10-06 08:16 | 5000 | -15.48 | 0.483 | -6.39 | 0.2 | False |
| 2026-10-06 12:18 | 5000 | -16.12 | 0.473 | -6.38 | 0.201 | False |
| 2026-10-06 16:14 | 5000 | -15.94 | 0.476 | -6.46 | 0.19 | False |
| 2026-10-06 20:13 | 5000 | -15.98 | 0.476 | -8.02 | 0.077 | False |
| 2026-10-07 00:34 | 5000 | -16.31 | 0.471 | -8.47 | 0.073 | False |
| 2026-10-07 04:15 | 5000 | -16.59 | 0.467 | -7.85 | 0.079 | False |

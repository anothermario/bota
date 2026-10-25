# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-25 08:13_

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

- Current-params net profit (full sample): **-10.14%**, PF 0.598, 66 trades, max DD -1599.65
- Optimizer out-of-sample: net **-4.84%**, PF 0.497, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-23 20:11 | 5000 | -11.36 | 0.559 | -3.44 | 0.595 | False |
| 2026-10-24 00:28 | 5000 | -10.82 | 0.573 | -3.32 | 0.604 | False |
| 2026-10-24 04:12 | 5000 | -10.82 | 0.573 | -3.34 | 0.601 | False |
| 2026-10-24 08:13 | 5000 | -10.85 | 0.573 | -4.13 | 0.511 | False |
| 2026-10-24 12:14 | 5000 | -10.85 | 0.573 | -4.5 | 0.488 | False |
| 2026-10-24 16:10 | 5000 | -10.85 | 0.573 | -4.08 | 0.514 | False |
| 2026-10-24 20:09 | 5000 | -9.78 | 0.614 | -2.93 | 0.648 | False |
| 2026-10-25 00:31 | 5000 | -9.77 | 0.614 | -2.93 | 0.648 | False |
| 2026-10-25 04:12 | 5000 | -9.81 | 0.613 | -2.93 | 0.648 | False |
| 2026-10-25 08:13 | 5000 | -10.14 | 0.598 | -4.84 | 0.497 | False |

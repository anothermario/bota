# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-30 12:13_

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

- Current-params net profit (full sample): **-13.75%**, PF 0.493, 70 trades, max DD -1587.64
- Optimizer out-of-sample: net **-2.76%**, PF 0.639, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-29 00:22 | 5000 | -14.63 | 0.459 | -4.53 | 0.483 | False |
| 2026-10-29 04:10 | 5000 | -14.65 | 0.459 | -4.03 | 0.495 | False |
| 2026-10-29 08:11 | 5000 | -13.33 | 0.493 | -3.5 | 0.559 | False |
| 2026-10-29 12:13 | 5000 | -13.33 | 0.493 | -3.51 | 0.6 | False |
| 2026-10-29 16:09 | 5000 | -13.36 | 0.493 | -3.28 | 0.619 | False |
| 2026-10-29 20:09 | 5000 | -12.99 | 0.507 | -2.86 | 0.665 | False |
| 2026-10-30 00:23 | 5000 | -13.34 | 0.5 | -2.8 | 0.67 | False |
| 2026-10-30 04:10 | 5000 | -13.94 | 0.489 | -3.47 | 0.583 | False |
| 2026-10-30 08:11 | 5000 | -13.93 | 0.489 | -2.96 | 0.677 | False |
| 2026-10-30 12:13 | 5000 | -13.75 | 0.493 | -2.76 | 0.639 | False |

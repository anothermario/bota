# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-31 12:09_

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

- Current-params net profit (full sample): **-14.04%**, PF 0.482, 70 trades, max DD -1582.94
- Optimizer out-of-sample: net **-4.13%**, PF 0.565, 25 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-30 00:23 | 5000 | -13.34 | 0.5 | -2.8 | 0.67 | False |
| 2026-10-30 04:10 | 5000 | -13.94 | 0.489 | -3.47 | 0.583 | False |
| 2026-10-30 08:11 | 5000 | -13.93 | 0.489 | -2.96 | 0.677 | False |
| 2026-10-30 12:13 | 5000 | -13.75 | 0.493 | -2.76 | 0.639 | False |
| 2026-10-30 16:08 | 5000 | -13.75 | 0.493 | -2.77 | 0.675 | False |
| 2026-10-30 20:07 | 5000 | -13.74 | 0.493 | -3.74 | 0.603 | False |
| 2026-10-31 00:19 | 5000 | -13.72 | 0.494 | -3.72 | 0.605 | False |
| 2026-10-31 04:08 | 5000 | -13.92 | 0.486 | -4.09 | 0.565 | False |
| 2026-10-31 08:08 | 5000 | -14.05 | 0.48 | -4.09 | 0.564 | False |
| 2026-10-31 12:09 | 5000 | -14.04 | 0.482 | -4.13 | 0.565 | False |

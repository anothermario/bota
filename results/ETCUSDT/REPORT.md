# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-07 04:41_

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
  "chand_len": 18,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-16.42%**, PF 0.419, 69 trades, max DD -1656.83
- Optimizer out-of-sample: net **-1.86%**, PF 0.759, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-05 12:39 | 5000 | -12.33 | 0.563 | -3.31 | 0.629 | False |
| 2026-08-05 16:35 | 5000 | -12.31 | 0.56 | -3.31 | 0.629 | False |
| 2026-08-05 20:32 | 5000 | -13.27 | 0.521 | -3.11 | 0.644 | False |
| 2026-08-06 00:32 | 5000 | -13.9 | 0.494 | -3.34 | 0.648 | False |
| 2026-08-06 05:05 | 5000 | -13.93 | 0.493 | -3.06 | 0.668 | False |
| 2026-08-06 08:59 | 5000 | -14.86 | 0.453 | -2.54 | 0.69 | False |
| 2026-08-06 12:41 | 5000 | -15.71 | 0.429 | -2.54 | 0.692 | False |
| 2026-08-06 21:58 | 5000 | -16.27 | 0.42 | -2.86 | 0.667 | False |
| 2026-08-07 01:16 | 5000 | -16.19 | 0.423 | -2.67 | 0.685 | False |
| 2026-08-07 04:41 | 5000 | -16.42 | 0.419 | -1.86 | 0.759 | False |

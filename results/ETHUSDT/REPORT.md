# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-01 04:14_

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

- Current-params net profit (full sample): **-13.37%**, PF 0.538, 98 trades, max DD -1424.56
- Optimizer out-of-sample: net **-4.96%**, PF 0.416, 25 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-29 16:13 | 5000 | -13.65 | 0.523 | -2.16 | 0.785 | False |
| 2026-09-29 20:13 | 5000 | -13.83 | 0.519 | -1.95 | 0.803 | False |
| 2026-09-30 00:34 | 5000 | -13.57 | 0.524 | -0.69 | 0.923 | False |
| 2026-09-30 04:14 | 5000 | -13.54 | 0.525 | -0.88 | 0.888 | False |
| 2026-09-30 08:16 | 5000 | -13.31 | 0.53 | -1.59 | 0.818 | False |
| 2026-09-30 12:21 | 5000 | -13.01 | 0.539 | -0.97 | 0.887 | False |
| 2026-09-30 16:14 | 5000 | -13.93 | 0.522 | -3.1 | 0.692 | False |
| 2026-09-30 20:14 | 5000 | -13.33 | 0.535 | -2.55 | 0.733 | False |
| 2026-10-01 00:38 | 5000 | -13.77 | 0.53 | -2.66 | 0.689 | False |
| 2026-10-01 04:14 | 5000 | -13.37 | 0.538 | -4.96 | 0.416 | False |

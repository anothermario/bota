# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-30 20:14_

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

- Current-params net profit (full sample): **-13.33%**, PF 0.535, 97 trades, max DD -1435.59
- Optimizer out-of-sample: net **-2.55%**, PF 0.733, 26 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-29 08:16 | 5000 | -13.53 | 0.524 | -1.04 | 0.879 | False |
| 2026-09-29 12:18 | 5000 | -13.62 | 0.523 | -1.62 | 0.817 | False |
| 2026-09-29 16:13 | 5000 | -13.65 | 0.523 | -2.16 | 0.785 | False |
| 2026-09-29 20:13 | 5000 | -13.83 | 0.519 | -1.95 | 0.803 | False |
| 2026-09-30 00:34 | 5000 | -13.57 | 0.524 | -0.69 | 0.923 | False |
| 2026-09-30 04:14 | 5000 | -13.54 | 0.525 | -0.88 | 0.888 | False |
| 2026-09-30 08:16 | 5000 | -13.31 | 0.53 | -1.59 | 0.818 | False |
| 2026-09-30 12:21 | 5000 | -13.01 | 0.539 | -0.97 | 0.887 | False |
| 2026-09-30 16:14 | 5000 | -13.93 | 0.522 | -3.1 | 0.692 | False |
| 2026-09-30 20:14 | 5000 | -13.33 | 0.535 | -2.55 | 0.733 | False |

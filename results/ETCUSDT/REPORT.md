# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-15 16:12_

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

- Current-params net profit (full sample): **-4.26%**, PF 0.803, 54 trades, max DD -718.75
- Optimizer out-of-sample: net **-2.77%**, PF 0.662, 18 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-14 04:14 | 5000 | -1.27 | 0.942 | -3.57 | 0.574 | False |
| 2026-09-14 08:18 | 5000 | -2.46 | 0.886 | -3.78 | 0.571 | False |
| 2026-09-14 12:18 | 5000 | -2.47 | 0.885 | -3.36 | 0.589 | False |
| 2026-09-14 16:11 | 5000 | -2.52 | 0.883 | -3.51 | 0.579 | False |
| 2026-09-14 20:12 | 5000 | -2.51 | 0.883 | -2.73 | 0.64 | False |
| 2026-09-15 00:32 | 5000 | -2.51 | 0.884 | -2.73 | 0.64 | False |
| 2026-09-15 04:13 | 5000 | -2.55 | 0.883 | -2.75 | 0.64 | False |
| 2026-09-15 08:16 | 5000 | -2.58 | 0.881 | -2.27 | 0.685 | False |
| 2026-09-15 12:17 | 5000 | -4.37 | 0.795 | -2.87 | 0.632 | False |
| 2026-09-15 16:12 | 5000 | -4.26 | 0.803 | -2.77 | 0.662 | False |

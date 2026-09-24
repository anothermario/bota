# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-24 16:13_

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

- Current-params net profit (full sample): **-13.77%**, PF 0.509, 99 trades, max DD -1641.1
- Optimizer out-of-sample: net **-3.72%**, PF 0.564, 32 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-23 04:14 | 5000 | -11.61 | 0.57 | -6.52 | 0.461 | False |
| 2026-09-23 08:16 | 5000 | -12.22 | 0.551 | -6.53 | 0.461 | False |
| 2026-09-23 12:17 | 5000 | -11.96 | 0.556 | -7.32 | 0.432 | False |
| 2026-09-23 16:13 | 5000 | -12.14 | 0.558 | -6.05 | 0.505 | False |
| 2026-09-23 20:12 | 5000 | -11.41 | 0.576 | -5.98 | 0.509 | False |
| 2026-09-24 00:30 | 5000 | -11.9 | 0.556 | -4.03 | 0.544 | False |
| 2026-09-24 04:13 | 5000 | -13.53 | 0.512 | -4.5 | 0.514 | False |
| 2026-09-24 08:17 | 5000 | -12.83 | 0.527 | -5.29 | 0.472 | False |
| 2026-09-24 12:17 | 5000 | -12.93 | 0.525 | -4.49 | 0.515 | False |
| 2026-09-24 16:13 | 5000 | -13.77 | 0.509 | -3.72 | 0.564 | False |

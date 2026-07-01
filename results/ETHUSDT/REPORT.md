# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-01 13:01_

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

- Current-params net profit (full sample): **-12.46%**, PF 0.576, 89 trades, max DD -1245.69
- Optimizer out-of-sample: net **-5.63%**, PF 0.233, 18 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-30 00:52 | 5000 | -12.4 | 0.578 | -2.31 | 0.632 | False |
| 2026-06-30 05:27 | 5000 | -12.24 | 0.582 | -1.92 | 0.678 | False |
| 2026-06-30 09:11 | 5000 | -12.4 | 0.578 | -1.93 | 0.679 | False |
| 2026-06-30 12:45 | 5000 | -11.96 | 0.589 | -2.1 | 0.657 | False |
| 2026-06-30 16:47 | 5000 | -10.98 | 0.615 | -1.32 | 0.781 | False |
| 2026-06-30 20:41 | 5000 | -11.28 | 0.608 | -2.72 | 0.54 | False |
| 2026-07-01 00:54 | 5000 | -10.98 | 0.615 | -2.82 | 0.524 | False |
| 2026-07-01 05:36 | 5000 | -11.0 | 0.616 | -2.82 | 0.528 | False |
| 2026-07-01 09:12 | 5000 | -11.64 | 0.602 | -4.2 | 0.377 | False |
| 2026-07-01 13:01 | 5000 | -12.46 | 0.576 | -5.63 | 0.233 | False |

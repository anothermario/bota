# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-26 00:30_

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

- Current-params net profit (full sample): **-9.66%**, PF 0.604, 78 trades, max DD -1038.99
- Optimizer out-of-sample: net **-1.41%**, PF 0.811, 24 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-24 12:14 | 5000 | -7.03 | 0.707 | -0.69 | 0.901 | False |
| 2026-10-24 16:10 | 5000 | -7.3 | 0.699 | -0.98 | 0.863 | False |
| 2026-10-24 20:09 | 5000 | -7.56 | 0.69 | -1.26 | 0.826 | False |
| 2026-10-25 00:31 | 5000 | -7.55 | 0.69 | -1.26 | 0.826 | False |
| 2026-10-25 04:12 | 5000 | -7.6 | 0.69 | -1.3 | 0.826 | False |
| 2026-10-25 08:13 | 5000 | -8.28 | 0.668 | -1.8 | 0.773 | False |
| 2026-10-25 12:14 | 5000 | -9.66 | 0.604 | -1.7 | 0.781 | False |
| 2026-10-25 16:10 | 5000 | -9.66 | 0.604 | -1.7 | 0.78 | False |
| 2026-10-25 20:10 | 5000 | -9.66 | 0.604 | -1.7 | 0.781 | False |
| 2026-10-26 00:30 | 5000 | -9.66 | 0.604 | -1.41 | 0.811 | False |

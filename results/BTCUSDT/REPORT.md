# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-20 12:09_

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
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-10.17%**, PF 0.484, 73 trades, max DD -1281.01
- Optimizer out-of-sample: net **-1.12%**, PF 0.689, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-19 00:13 | 5000 | -10.78 | 0.434 | -1.75 | 0.37 | False |
| 2026-08-19 04:15 | 5000 | -10.78 | 0.434 | -1.75 | 0.37 | False |
| 2026-08-19 08:11 | 5000 | -10.82 | 0.434 | -1.79 | 0.37 | False |
| 2026-08-19 12:09 | 5000 | -11.05 | 0.428 | -2.7 | 0.275 | False |
| 2026-08-19 16:08 | 5000 | -10.15 | 0.484 | -1.72 | 0.583 | False |
| 2026-08-19 20:06 | 5000 | -10.15 | 0.484 | -1.1 | 0.689 | False |
| 2026-08-20 00:14 | 5000 | -10.15 | 0.484 | -1.1 | 0.689 | False |
| 2026-08-20 04:14 | 5000 | -10.15 | 0.484 | -1.1 | 0.689 | False |
| 2026-08-20 08:13 | 5000 | -10.15 | 0.484 | -1.1 | 0.689 | False |
| 2026-08-20 12:09 | 5000 | -10.17 | 0.484 | -1.12 | 0.689 | False |

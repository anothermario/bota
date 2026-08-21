# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-21 00:15_

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

- Current-params net profit (full sample): **-11.1%**, PF 0.431, 74 trades, max DD -1267.97
- Optimizer out-of-sample: net **-1.55%**, PF 0.609, 24 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-19 12:09 | 5000 | -11.05 | 0.428 | -2.7 | 0.275 | False |
| 2026-08-19 16:08 | 5000 | -10.15 | 0.484 | -1.72 | 0.583 | False |
| 2026-08-19 20:06 | 5000 | -10.15 | 0.484 | -1.1 | 0.689 | False |
| 2026-08-20 00:14 | 5000 | -10.15 | 0.484 | -1.1 | 0.689 | False |
| 2026-08-20 04:14 | 5000 | -10.15 | 0.484 | -1.1 | 0.689 | False |
| 2026-08-20 08:13 | 5000 | -10.15 | 0.484 | -1.1 | 0.689 | False |
| 2026-08-20 12:09 | 5000 | -10.17 | 0.484 | -1.12 | 0.689 | False |
| 2026-08-20 16:09 | 5000 | -10.01 | 0.494 | -1.14 | 0.681 | False |
| 2026-08-20 20:07 | 5000 | -10.19 | 0.483 | -1.55 | 0.609 | False |
| 2026-08-21 00:15 | 5000 | -11.1 | 0.431 | -1.55 | 0.609 | False |

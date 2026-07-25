# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-25 09:45_

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

- Current-params net profit (full sample): **-17.76%**, PF 0.482, 92 trades, max DD -2118.59
- Optimizer out-of-sample: net **-9.86%**, PF 0.217, 32 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-23 21:03 | 5000 | -16.75 | 0.506 | -10.19 | 0.159 | False |
| 2026-07-24 02:34 | 5000 | -16.31 | 0.515 | -9.42 | 0.171 | False |
| 2026-07-24 06:25 | 5000 | -16.27 | 0.515 | -9.87 | 0.171 | False |
| 2026-07-24 10:15 | 5000 | -17.2 | 0.5 | -10.28 | 0.166 | False |
| 2026-07-24 13:42 | 5000 | -17.25 | 0.5 | -10.31 | 0.166 | False |
| 2026-07-24 17:36 | 5000 | -17.98 | 0.474 | -10.46 | 0.201 | False |
| 2026-07-24 21:02 | 5000 | -18.75 | 0.46 | -10.31 | 0.166 | False |
| 2026-07-25 02:32 | 5000 | -17.84 | 0.479 | -10.31 | 0.166 | False |
| 2026-07-25 06:17 | 5000 | -17.82 | 0.48 | -10.3 | 0.166 | False |
| 2026-07-25 09:45 | 5000 | -17.76 | 0.482 | -9.86 | 0.217 | False |

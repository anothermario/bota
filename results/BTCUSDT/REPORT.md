# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-08 20:08_

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

- Current-params net profit (full sample): **-13.12%**, PF 0.43, 70 trades, max DD -1337.17
- Optimizer out-of-sample: net **-5.06%**, PF 0.346, 31 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-07 08:26 | 5000 | -14.18 | 0.408 | -5.75 | 0.315 | False |
| 2026-08-07 12:18 | 5000 | -13.65 | 0.42 | -5.79 | 0.315 | False |
| 2026-08-07 16:19 | 5000 | -13.71 | 0.418 | -5.36 | 0.332 | False |
| 2026-08-07 20:14 | 5000 | -13.71 | 0.418 | -5.36 | 0.332 | False |
| 2026-08-08 00:19 | 5000 | -13.7 | 0.418 | -5.63 | 0.32 | False |
| 2026-08-08 04:25 | 5000 | -13.91 | 0.414 | -4.89 | 0.353 | False |
| 2026-08-08 08:14 | 5000 | -13.37 | 0.425 | -5.55 | 0.323 | False |
| 2026-08-08 12:10 | 5000 | -13.12 | 0.43 | -5.55 | 0.323 | False |
| 2026-08-08 16:08 | 5000 | -13.12 | 0.43 | -4.93 | 0.354 | False |
| 2026-08-08 20:08 | 5000 | -13.12 | 0.43 | -5.06 | 0.346 | False |

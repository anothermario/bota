# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-08 04:25_

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

- Current-params net profit (full sample): **-13.91%**, PF 0.414, 72 trades, max DD -1415.99
- Optimizer out-of-sample: net **-4.89%**, PF 0.353, 30 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-06 12:41 | 5000 | -14.79 | 0.396 | -5.51 | 0.325 | False |
| 2026-08-06 21:58 | 5000 | -14.69 | 0.398 | -5.5 | 0.325 | False |
| 2026-08-07 01:16 | 5000 | -14.73 | 0.398 | -5.54 | 0.325 | False |
| 2026-08-07 04:40 | 5000 | -14.19 | 0.408 | -5.75 | 0.315 | False |
| 2026-08-07 08:26 | 5000 | -14.18 | 0.408 | -5.75 | 0.315 | False |
| 2026-08-07 12:18 | 5000 | -13.65 | 0.42 | -5.79 | 0.315 | False |
| 2026-08-07 16:19 | 5000 | -13.71 | 0.418 | -5.36 | 0.332 | False |
| 2026-08-07 20:14 | 5000 | -13.71 | 0.418 | -5.36 | 0.332 | False |
| 2026-08-08 00:19 | 5000 | -13.7 | 0.418 | -5.63 | 0.32 | False |
| 2026-08-08 04:25 | 5000 | -13.91 | 0.414 | -4.89 | 0.353 | False |

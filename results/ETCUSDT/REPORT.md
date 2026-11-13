# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-11-13 12:10_

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

- Current-params net profit (full sample): **-14.74%**, PF 0.415, 65 trades, max DD -1600.17
- Optimizer out-of-sample: net **-7.05%**, PF 0.193, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-12 00:19 | 5000 | -14.81 | 0.418 | -5.39 | 0.417 | False |
| 2026-11-12 04:08 | 5000 | -14.82 | 0.417 | -4.47 | 0.498 | False |
| 2026-11-12 08:10 | 5000 | -14.33 | 0.427 | -7.94 | 0.173 | False |
| 2026-11-12 12:11 | 5000 | -14.33 | 0.427 | -7.65 | 0.179 | False |
| 2026-11-12 16:08 | 5000 | -14.33 | 0.427 | -7.65 | 0.179 | False |
| 2026-11-12 20:07 | 5000 | -14.33 | 0.427 | -5.51 | 0.412 | False |
| 2026-11-13 00:19 | 5000 | -14.33 | 0.427 | -7.66 | 0.179 | False |
| 2026-11-13 04:09 | 5000 | -14.35 | 0.427 | -7.17 | 0.19 | False |
| 2026-11-13 08:10 | 5000 | -14.56 | 0.423 | -7.25 | 0.188 | False |
| 2026-11-13 12:10 | 5000 | -14.74 | 0.415 | -7.05 | 0.193 | False |

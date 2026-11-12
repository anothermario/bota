# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-11-12 20:07_

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

- Current-params net profit (full sample): **-14.33%**, PF 0.427, 65 trades, max DD -1580.34
- Optimizer out-of-sample: net **-5.51%**, PF 0.412, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-11 08:10 | 5000 | -14.53 | 0.421 | -4.7 | 0.451 | False |
| 2026-11-11 12:11 | 5000 | -14.18 | 0.428 | -4.7 | 0.451 | False |
| 2026-11-11 16:08 | 5000 | -14.18 | 0.428 | -5.73 | 0.4 | False |
| 2026-11-11 20:07 | 5000 | -14.18 | 0.428 | -3.91 | 0.522 | False |
| 2026-11-12 00:19 | 5000 | -14.81 | 0.418 | -5.39 | 0.417 | False |
| 2026-11-12 04:08 | 5000 | -14.82 | 0.417 | -4.47 | 0.498 | False |
| 2026-11-12 08:10 | 5000 | -14.33 | 0.427 | -7.94 | 0.173 | False |
| 2026-11-12 12:11 | 5000 | -14.33 | 0.427 | -7.65 | 0.179 | False |
| 2026-11-12 16:08 | 5000 | -14.33 | 0.427 | -7.65 | 0.179 | False |
| 2026-11-12 20:07 | 5000 | -14.33 | 0.427 | -5.51 | 0.412 | False |

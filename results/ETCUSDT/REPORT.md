# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-05 17:09_

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
  "chand_len": 18,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-11.77%**, PF 0.574, 78 trades, max DD -1373.02
- Optimizer out-of-sample: net **-6.24%**, PF 0.318, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-04 06:46 | 5000 | -13.79 | 0.531 | -7.14 | 0.291 | False |
| 2026-07-04 10:09 | 5000 | -13.79 | 0.531 | -4.46 | 0.492 | False |
| 2026-07-04 13:23 | 5000 | -13.6 | 0.535 | -6.96 | 0.298 | False |
| 2026-07-04 17:04 | 5000 | -13.6 | 0.535 | -6.94 | 0.3 | False |
| 2026-07-04 20:56 | 5000 | -13.61 | 0.535 | -6.91 | 0.303 | False |
| 2026-07-05 03:19 | 5000 | -12.75 | 0.554 | -7.57 | 0.221 | False |
| 2026-07-05 07:25 | 5000 | -12.71 | 0.555 | -7.02 | 0.235 | False |
| 2026-07-05 10:12 | 5000 | -12.38 | 0.562 | -7.02 | 0.235 | False |
| 2026-07-05 13:37 | 5000 | -12.36 | 0.561 | -6.24 | 0.318 | False |
| 2026-07-05 17:09 | 5000 | -11.77 | 0.574 | -6.24 | 0.318 | False |

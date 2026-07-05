# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-05 03:19_

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

- Current-params net profit (full sample): **-12.75%**, PF 0.554, 79 trades, max DD -1364.4
- Optimizer out-of-sample: net **-7.57%**, PF 0.221, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-03 14:01 | 5000 | -12.78 | 0.547 | -6.68 | 0.306 | False |
| 2026-07-03 17:25 | 5000 | -12.6 | 0.553 | -6.22 | 0.321 | False |
| 2026-07-03 21:05 | 5000 | -12.61 | 0.553 | -6.22 | 0.321 | False |
| 2026-07-04 02:49 | 5000 | -12.99 | 0.546 | -6.25 | 0.321 | False |
| 2026-07-04 06:46 | 5000 | -13.79 | 0.531 | -7.14 | 0.291 | False |
| 2026-07-04 10:09 | 5000 | -13.79 | 0.531 | -4.46 | 0.492 | False |
| 2026-07-04 13:23 | 5000 | -13.6 | 0.535 | -6.96 | 0.298 | False |
| 2026-07-04 17:04 | 5000 | -13.6 | 0.535 | -6.94 | 0.3 | False |
| 2026-07-04 20:56 | 5000 | -13.61 | 0.535 | -6.91 | 0.303 | False |
| 2026-07-05 03:19 | 5000 | -12.75 | 0.554 | -7.57 | 0.221 | False |

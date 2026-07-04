# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-04 13:23_

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

- Current-params net profit (full sample): **-13.6%**, PF 0.535, 80 trades, max DD -1360.33
- Optimizer out-of-sample: net **-6.96%**, PF 0.298, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-03 02:53 | 5000 | -12.43 | 0.567 | -6.97 | 0.269 | False |
| 2026-07-03 07:19 | 5000 | -11.96 | 0.579 | -6.98 | 0.269 | False |
| 2026-07-03 10:34 | 5000 | -13.14 | 0.539 | -7.1 | 0.266 | False |
| 2026-07-03 14:01 | 5000 | -12.78 | 0.547 | -6.68 | 0.306 | False |
| 2026-07-03 17:25 | 5000 | -12.6 | 0.553 | -6.22 | 0.321 | False |
| 2026-07-03 21:05 | 5000 | -12.61 | 0.553 | -6.22 | 0.321 | False |
| 2026-07-04 02:49 | 5000 | -12.99 | 0.546 | -6.25 | 0.321 | False |
| 2026-07-04 06:46 | 5000 | -13.79 | 0.531 | -7.14 | 0.291 | False |
| 2026-07-04 10:09 | 5000 | -13.79 | 0.531 | -4.46 | 0.492 | False |
| 2026-07-04 13:23 | 5000 | -13.6 | 0.535 | -6.96 | 0.298 | False |

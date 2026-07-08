# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-08 14:03_

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

- Current-params net profit (full sample): **-13.87%**, PF 0.574, 96 trades, max DD -1387.27
- Optimizer out-of-sample: net **-7.56%**, PF 0.289, 31 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-07 03:17 | 5000 | -12.38 | 0.608 | -7.36 | 0.316 | False |
| 2026-07-07 07:37 | 5000 | -12.73 | 0.595 | -6.68 | 0.338 | False |
| 2026-07-07 10:54 | 5000 | -12.73 | 0.595 | -6.68 | 0.338 | False |
| 2026-07-07 14:31 | 5000 | -13.25 | 0.584 | -6.66 | 0.34 | False |
| 2026-07-07 17:58 | 5000 | -13.28 | 0.583 | -6.72 | 0.334 | False |
| 2026-07-07 21:23 | 5000 | -13.81 | 0.574 | -7.24 | 0.296 | False |
| 2026-07-08 02:35 | 5000 | -13.35 | 0.584 | -7.03 | 0.303 | False |
| 2026-07-08 06:27 | 5000 | -13.35 | 0.584 | -7.03 | 0.304 | False |
| 2026-07-08 10:17 | 5000 | -13.33 | 0.584 | -7.01 | 0.306 | False |
| 2026-07-08 14:03 | 5000 | -13.87 | 0.574 | -7.56 | 0.289 | False |

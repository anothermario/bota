# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-09 17:55_

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

- Current-params net profit (full sample): **-13.51%**, PF 0.585, 94 trades, max DD -1350.55
- Optimizer out-of-sample: net **-8.8%**, PF 0.227, 30 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-08 06:27 | 5000 | -13.35 | 0.584 | -7.03 | 0.304 | False |
| 2026-07-08 10:17 | 5000 | -13.33 | 0.584 | -7.01 | 0.306 | False |
| 2026-07-08 14:03 | 5000 | -13.87 | 0.574 | -7.56 | 0.289 | False |
| 2026-07-08 17:28 | 5000 | -14.6 | 0.562 | -8.86 | 0.225 | False |
| 2026-07-08 21:07 | 5000 | -14.35 | 0.567 | -8.98 | 0.223 | False |
| 2026-07-09 02:53 | 5000 | -14.34 | 0.567 | -8.97 | 0.223 | False |
| 2026-07-09 07:41 | 5000 | -14.32 | 0.567 | -8.97 | 0.223 | False |
| 2026-07-09 10:53 | 5000 | -14.09 | 0.572 | -8.83 | 0.226 | False |
| 2026-07-09 14:56 | 5000 | -14.12 | 0.572 | -8.84 | 0.226 | False |
| 2026-07-09 17:55 | 5000 | -13.51 | 0.585 | -8.8 | 0.227 | False |

# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-10 02:56_

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

- Current-params net profit (full sample): **-14.48%**, PF 0.567, 95 trades, max DD -1447.52
- Optimizer out-of-sample: net **-9.58%**, PF 0.13, 29 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-08 14:03 | 5000 | -13.87 | 0.574 | -7.56 | 0.289 | False |
| 2026-07-08 17:28 | 5000 | -14.6 | 0.562 | -8.86 | 0.225 | False |
| 2026-07-08 21:07 | 5000 | -14.35 | 0.567 | -8.98 | 0.223 | False |
| 2026-07-09 02:53 | 5000 | -14.34 | 0.567 | -8.97 | 0.223 | False |
| 2026-07-09 07:41 | 5000 | -14.32 | 0.567 | -8.97 | 0.223 | False |
| 2026-07-09 10:53 | 5000 | -14.09 | 0.572 | -8.83 | 0.226 | False |
| 2026-07-09 14:56 | 5000 | -14.12 | 0.572 | -8.84 | 0.226 | False |
| 2026-07-09 17:55 | 5000 | -13.51 | 0.585 | -8.8 | 0.227 | False |
| 2026-07-09 21:22 | 5000 | -13.7 | 0.582 | -8.18 | 0.242 | False |
| 2026-07-10 02:56 | 5000 | -14.48 | 0.567 | -9.58 | 0.13 | False |

# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-29 17:13_

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

- Current-params net profit (full sample): **-20.53%**, PF 0.406, 96 trades, max DD -2052.75
- Optimizer out-of-sample: net **-8.23%**, PF 0.212, 29 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-28 06:26 | 5000 | -20.02 | 0.428 | -9.98 | 0.179 | False |
| 2026-07-28 10:33 | 5000 | -19.68 | 0.44 | -9.18 | 0.193 | False |
| 2026-07-28 14:03 | 5000 | -19.69 | 0.439 | -9.18 | 0.193 | False |
| 2026-07-28 17:26 | 5000 | -19.71 | 0.439 | -9.21 | 0.192 | False |
| 2026-07-28 21:06 | 5000 | -19.98 | 0.439 | -8.38 | 0.285 | False |
| 2026-07-29 02:31 | 5000 | -21.05 | 0.401 | -8.23 | 0.213 | False |
| 2026-07-29 06:29 | 5000 | -21.13 | 0.398 | -8.23 | 0.213 | False |
| 2026-07-29 10:38 | 5000 | -21.14 | 0.398 | -8.23 | 0.213 | False |
| 2026-07-29 14:07 | 5000 | -21.13 | 0.398 | -8.23 | 0.213 | False |
| 2026-07-29 17:13 | 5000 | -20.53 | 0.406 | -8.23 | 0.212 | False |

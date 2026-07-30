# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-30 13:57_

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

- Current-params net profit (full sample): **-19.39%**, PF 0.424, 94 trades, max DD -1939.07
- Optimizer out-of-sample: net **-7.44%**, PF 0.289, 26 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-29 02:31 | 5000 | -21.05 | 0.401 | -8.23 | 0.213 | False |
| 2026-07-29 06:29 | 5000 | -21.13 | 0.398 | -8.23 | 0.213 | False |
| 2026-07-29 10:38 | 5000 | -21.14 | 0.398 | -8.23 | 0.213 | False |
| 2026-07-29 14:07 | 5000 | -21.13 | 0.398 | -8.23 | 0.213 | False |
| 2026-07-29 17:13 | 5000 | -20.53 | 0.406 | -8.23 | 0.212 | False |
| 2026-07-29 20:54 | 5000 | -20.16 | 0.412 | -8.5 | 0.179 | False |
| 2026-07-30 02:13 | 5000 | -19.5 | 0.422 | -7.76 | 0.279 | False |
| 2026-07-30 06:26 | 5000 | -19.68 | 0.419 | -7.76 | 0.279 | False |
| 2026-07-30 10:23 | 5000 | -20.01 | 0.414 | -7.4 | 0.289 | False |
| 2026-07-30 13:57 | 5000 | -19.39 | 0.424 | -7.44 | 0.289 | False |

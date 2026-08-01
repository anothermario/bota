# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-08-01 06:28_

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

- Current-params net profit (full sample): **-17.66%**, PF 0.46, 93 trades, max DD -1999.72
- Optimizer out-of-sample: net **-6.19%**, PF 0.367, 27 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-30 17:25 | 5000 | -19.83 | 0.418 | -7.94 | 0.275 | False |
| 2026-07-30 21:08 | 5000 | -19.83 | 0.418 | -7.94 | 0.275 | False |
| 2026-07-31 02:42 | 5000 | -19.77 | 0.419 | -7.42 | 0.29 | False |
| 2026-07-31 06:42 | 5000 | -19.31 | 0.43 | -8.65 | 0.177 | False |
| 2026-07-31 10:37 | 5000 | -19.29 | 0.432 | -7.03 | 0.303 | False |
| 2026-07-31 14:03 | 5000 | -19.53 | 0.424 | -7.08 | 0.301 | False |
| 2026-07-31 17:27 | 5000 | -19.53 | 0.424 | -7.09 | 0.301 | False |
| 2026-07-31 21:02 | 5000 | -19.02 | 0.437 | -6.88 | 0.342 | False |
| 2026-08-01 02:41 | 5000 | -18.26 | 0.45 | -6.0 | 0.375 | False |
| 2026-08-01 06:28 | 5000 | -17.66 | 0.46 | -6.19 | 0.367 | False |

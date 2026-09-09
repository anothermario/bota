# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-09 04:13_

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
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-8.86%**, PF 0.524, 66 trades, max DD -998.6
- Optimizer out-of-sample: net **-3.17%**, PF 0.527, 15 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-07 16:11 | 5000 | -7.78 | 0.56 | -3.14 | 0.488 | False |
| 2026-09-07 20:10 | 5000 | -8.28 | 0.543 | -4.03 | 0.422 | False |
| 2026-09-08 00:31 | 5000 | -8.28 | 0.543 | -4.28 | 0.407 | False |
| 2026-09-08 04:13 | 5000 | -8.28 | 0.543 | -4.35 | 0.403 | False |
| 2026-09-08 08:16 | 5000 | -8.32 | 0.543 | -4.85 | 0.378 | False |
| 2026-09-08 12:17 | 5000 | -8.83 | 0.527 | -5.39 | 0.351 | False |
| 2026-09-08 16:13 | 5000 | -8.92 | 0.522 | -3.94 | 0.429 | False |
| 2026-09-08 20:11 | 5000 | -8.92 | 0.522 | -5.39 | 0.351 | False |
| 2026-09-09 00:31 | 5000 | -8.44 | 0.537 | -5.06 | 0.367 | False |
| 2026-09-09 04:13 | 5000 | -8.86 | 0.524 | -3.17 | 0.527 | False |

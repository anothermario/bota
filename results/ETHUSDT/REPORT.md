# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-08 20:11_

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

- Current-params net profit (full sample): **-15.57%**, PF 0.42, 95 trades, max DD -1556.8
- Optimizer out-of-sample: net **-4.62%**, PF 0.43, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-07 08:17 | 5000 | -15.37 | 0.421 | -4.47 | 0.443 | False |
| 2026-09-07 12:17 | 5000 | -14.83 | 0.431 | -4.47 | 0.442 | False |
| 2026-09-07 16:11 | 5000 | -14.83 | 0.431 | -3.97 | 0.473 | False |
| 2026-09-07 20:10 | 5000 | -14.83 | 0.431 | -4.07 | 0.465 | False |
| 2026-09-08 00:31 | 5000 | -14.83 | 0.431 | -4.7 | 0.424 | False |
| 2026-09-08 04:13 | 5000 | -14.83 | 0.431 | -4.4 | 0.44 | False |
| 2026-09-08 08:16 | 5000 | -15.06 | 0.428 | -3.82 | 0.479 | False |
| 2026-09-08 12:17 | 5000 | -15.79 | 0.416 | -4.66 | 0.428 | False |
| 2026-09-08 16:13 | 5000 | -15.54 | 0.42 | -4.62 | 0.43 | False |
| 2026-09-08 20:11 | 5000 | -15.57 | 0.42 | -4.62 | 0.43 | False |

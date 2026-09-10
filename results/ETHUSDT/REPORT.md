# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-10 00:29_

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

- Current-params net profit (full sample): **-15.31%**, PF 0.427, 96 trades, max DD -1531.06
- Optimizer out-of-sample: net **-4.16%**, PF 0.459, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-08 12:17 | 5000 | -15.79 | 0.416 | -4.66 | 0.428 | False |
| 2026-09-08 16:13 | 5000 | -15.54 | 0.42 | -4.62 | 0.43 | False |
| 2026-09-08 20:11 | 5000 | -15.57 | 0.42 | -4.62 | 0.43 | False |
| 2026-09-09 00:31 | 5000 | -15.54 | 0.42 | -3.94 | 0.471 | False |
| 2026-09-09 04:13 | 5000 | -15.58 | 0.42 | -4.88 | 0.416 | False |
| 2026-09-09 08:15 | 5000 | -15.04 | 0.43 | -3.5 | 0.502 | False |
| 2026-09-09 12:16 | 5000 | -15.85 | 0.417 | -4.29 | 0.451 | False |
| 2026-09-09 16:12 | 5000 | -15.85 | 0.417 | -4.27 | 0.453 | False |
| 2026-09-09 20:11 | 5000 | -15.55 | 0.423 | -4.89 | 0.42 | False |
| 2026-09-10 00:29 | 5000 | -15.31 | 0.427 | -4.16 | 0.459 | False |

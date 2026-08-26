# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-08-26 04:16_

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

- Current-params net profit (full sample): **-22.03%**, PF 0.287, 106 trades, max DD -2203.31
- Optimizer out-of-sample: net **-6.16%**, PF 0.1, 26 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-24 16:11 | 5000 | -20.82 | 0.308 | -4.97 | 0.252 | False |
| 2026-08-24 20:08 | 5000 | -21.7 | 0.29 | -4.7 | 0.263 | False |
| 2026-08-25 00:14 | 5000 | -21.7 | 0.29 | -4.7 | 0.263 | False |
| 2026-08-25 04:15 | 5000 | -21.7 | 0.29 | -4.73 | 0.262 | False |
| 2026-08-25 08:16 | 5000 | -21.67 | 0.29 | -4.16 | 0.288 | False |
| 2026-08-25 12:11 | 5000 | -21.31 | 0.295 | -4.16 | 0.288 | False |
| 2026-08-25 16:14 | 5000 | -21.9 | 0.289 | -4.57 | 0.298 | False |
| 2026-08-25 20:07 | 5000 | -22.06 | 0.286 | -4.57 | 0.298 | False |
| 2026-08-26 00:15 | 5000 | -22.02 | 0.287 | -5.55 | 0.189 | False |
| 2026-08-26 04:16 | 5000 | -22.03 | 0.287 | -6.16 | 0.1 | False |

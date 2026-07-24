# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-24 06:25_

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
  "chand_len": 18,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-15.82%**, PF 0.423, 67 trades, max DD -1582.04
- Optimizer out-of-sample: net **-8.55%**, PF 0.143, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-22 17:17 | 5000 | -14.63 | 0.439 | -5.96 | 0.194 | False |
| 2026-07-22 21:06 | 5000 | -15.31 | 0.428 | -6.74 | 0.175 | False |
| 2026-07-23 02:38 | 5000 | -15.85 | 0.419 | -7.32 | 0.163 | False |
| 2026-07-23 06:29 | 5000 | -15.51 | 0.425 | -7.32 | 0.163 | False |
| 2026-07-23 10:21 | 5000 | -15.49 | 0.426 | -7.32 | 0.163 | False |
| 2026-07-23 13:55 | 5000 | -15.18 | 0.433 | -7.84 | 0.154 | False |
| 2026-07-23 17:22 | 5000 | -15.2 | 0.433 | -7.87 | 0.154 | False |
| 2026-07-23 21:03 | 5000 | -15.2 | 0.433 | -8.53 | 0.143 | False |
| 2026-07-24 02:34 | 5000 | -15.55 | 0.427 | -8.25 | 0.148 | False |
| 2026-07-24 06:25 | 5000 | -15.82 | 0.423 | -8.55 | 0.143 | False |

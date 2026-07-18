# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-18 06:04_

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

- Current-params net profit (full sample): **-7.87%**, PF 0.68, 68 trades, max DD -1359.38
- Optimizer out-of-sample: net **-5.82%**, PF 0.31, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-16 17:14 | 5000 | -9.55 | 0.625 | -5.95 | 0.304 | False |
| 2026-07-16 20:56 | 5000 | -9.42 | 0.628 | -5.96 | 0.303 | False |
| 2026-07-17 02:32 | 5000 | -9.45 | 0.628 | -6.46 | 0.244 | False |
| 2026-07-17 06:14 | 5000 | -8.86 | 0.645 | -6.46 | 0.244 | False |
| 2026-07-17 09:56 | 5000 | -7.74 | 0.678 | -6.46 | 0.244 | False |
| 2026-07-17 13:25 | 5000 | -7.79 | 0.681 | -5.89 | 0.307 | False |
| 2026-07-17 17:10 | 5000 | -7.79 | 0.681 | -5.89 | 0.307 | False |
| 2026-07-17 20:53 | 5000 | -7.79 | 0.682 | -6.37 | 0.29 | False |
| 2026-07-18 02:24 | 5000 | -7.62 | 0.687 | -5.82 | 0.311 | False |
| 2026-07-18 06:04 | 5000 | -7.87 | 0.68 | -5.82 | 0.31 | False |

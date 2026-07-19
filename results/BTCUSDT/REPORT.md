# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-19 06:29_

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

- Current-params net profit (full sample): **-7.78%**, PF 0.68, 67 trades, max DD -1359.32
- Optimizer out-of-sample: net **-5.15%**, PF 0.346, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-17 17:10 | 5000 | -7.79 | 0.681 | -5.89 | 0.307 | False |
| 2026-07-17 20:53 | 5000 | -7.79 | 0.682 | -6.37 | 0.29 | False |
| 2026-07-18 02:24 | 5000 | -7.62 | 0.687 | -5.82 | 0.311 | False |
| 2026-07-18 06:04 | 5000 | -7.87 | 0.68 | -5.82 | 0.31 | False |
| 2026-07-18 09:23 | 5000 | -7.62 | 0.687 | -5.82 | 0.311 | False |
| 2026-07-18 13:12 | 5000 | -7.62 | 0.687 | -5.82 | 0.311 | False |
| 2026-07-18 16:57 | 5000 | -7.62 | 0.687 | -5.53 | 0.322 | False |
| 2026-07-18 20:45 | 5000 | -7.63 | 0.688 | -5.57 | 0.322 | False |
| 2026-07-19 02:35 | 5000 | -7.91 | 0.676 | -5.58 | 0.322 | False |
| 2026-07-19 06:29 | 5000 | -7.78 | 0.68 | -5.15 | 0.346 | False |

# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-06-23 16:52_

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

- Current-params net profit (full sample): **-6.92%**, PF 0.675, 63 trades, max DD -787.74
- Optimizer out-of-sample: net **-5.0%**, PF 0.394, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-22 05:53 | 5000 | -7.66 | 0.644 | -5.55 | 0.39 | False |
| 2026-06-22 10:05 | 5000 | -7.96 | 0.629 | -5.97 | 0.341 | False |
| 2026-06-22 13:56 | 5000 | -7.99 | 0.629 | -6.96 | 0.254 | False |
| 2026-06-22 17:34 | 5000 | -8.17 | 0.623 | -6.85 | 0.257 | False |
| 2026-06-22 21:04 | 5000 | -8.17 | 0.623 | -6.84 | 0.257 | False |
| 2026-06-23 00:50 | 5000 | -8.17 | 0.623 | -6.85 | 0.257 | False |
| 2026-06-23 05:25 | 5000 | -8.17 | 0.623 | -5.87 | 0.289 | False |
| 2026-06-23 09:12 | 5000 | -8.19 | 0.623 | -5.91 | 0.289 | False |
| 2026-06-23 13:03 | 5000 | -6.99 | 0.673 | -5.0 | 0.394 | False |
| 2026-06-23 16:52 | 5000 | -6.92 | 0.675 | -5.0 | 0.394 | False |

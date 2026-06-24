# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-06-24 12:49_

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

- Current-params net profit (full sample): **-7.63%**, PF 0.652, 63 trades, max DD -787.17
- Optimizer out-of-sample: net **-5.69%**, PF 0.362, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-23 00:50 | 5000 | -8.17 | 0.623 | -6.85 | 0.257 | False |
| 2026-06-23 05:25 | 5000 | -8.17 | 0.623 | -5.87 | 0.289 | False |
| 2026-06-23 09:12 | 5000 | -8.19 | 0.623 | -5.91 | 0.289 | False |
| 2026-06-23 13:03 | 5000 | -6.99 | 0.673 | -5.0 | 0.394 | False |
| 2026-06-23 16:52 | 5000 | -6.92 | 0.675 | -5.0 | 0.394 | False |
| 2026-06-23 20:47 | 5000 | -6.92 | 0.675 | -5.04 | 0.392 | False |
| 2026-06-24 00:47 | 5000 | -6.95 | 0.675 | -5.08 | 0.392 | False |
| 2026-06-24 05:23 | 5000 | -7.56 | 0.656 | -5.66 | 0.366 | False |
| 2026-06-24 09:11 | 5000 | -7.63 | 0.652 | -5.66 | 0.366 | False |
| 2026-06-24 12:49 | 5000 | -7.63 | 0.652 | -5.69 | 0.362 | False |

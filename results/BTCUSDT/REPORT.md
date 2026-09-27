# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-27 12:16_

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

- Current-params net profit (full sample): **-8.45%**, PF 0.599, 66 trades, max DD -909.36
- Optimizer out-of-sample: net **-1.09%**, PF 0.856, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-26 00:30 | 5000 | -8.61 | 0.593 | -1.65 | 0.791 | False |
| 2026-09-26 04:12 | 5000 | -8.61 | 0.593 | -1.65 | 0.791 | False |
| 2026-09-26 08:14 | 5000 | -8.61 | 0.593 | -1.65 | 0.791 | False |
| 2026-09-26 12:15 | 5000 | -8.61 | 0.593 | -1.65 | 0.791 | False |
| 2026-09-26 16:11 | 5000 | -9.03 | 0.58 | -1.32 | 0.834 | False |
| 2026-09-26 20:10 | 5000 | -8.6 | 0.593 | -1.64 | 0.791 | False |
| 2026-09-27 00:35 | 5000 | -8.6 | 0.593 | -1.05 | 0.856 | False |
| 2026-09-27 04:13 | 5000 | -8.61 | 0.593 | -1.05 | 0.856 | False |
| 2026-09-27 08:14 | 5000 | -8.41 | 0.599 | -1.05 | 0.856 | False |
| 2026-09-27 12:16 | 5000 | -8.45 | 0.599 | -1.09 | 0.856 | False |

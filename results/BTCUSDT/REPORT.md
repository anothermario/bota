# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-26 20:10_

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

- Current-params net profit (full sample): **-8.6%**, PF 0.593, 67 trades, max DD -903.78
- Optimizer out-of-sample: net **-1.64%**, PF 0.791, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-25 08:16 | 5000 | -7.67 | 0.62 | -1.17 | 0.841 | False |
| 2026-09-25 12:17 | 5000 | -8.61 | 0.593 | -2.04 | 0.753 | False |
| 2026-09-25 16:13 | 5000 | -8.61 | 0.593 | -2.04 | 0.753 | False |
| 2026-09-25 20:10 | 5000 | -8.61 | 0.593 | -2.36 | 0.724 | False |
| 2026-09-26 00:30 | 5000 | -8.61 | 0.593 | -1.65 | 0.791 | False |
| 2026-09-26 04:12 | 5000 | -8.61 | 0.593 | -1.65 | 0.791 | False |
| 2026-09-26 08:14 | 5000 | -8.61 | 0.593 | -1.65 | 0.791 | False |
| 2026-09-26 12:15 | 5000 | -8.61 | 0.593 | -1.65 | 0.791 | False |
| 2026-09-26 16:11 | 5000 | -9.03 | 0.58 | -1.32 | 0.834 | False |
| 2026-09-26 20:10 | 5000 | -8.6 | 0.593 | -1.64 | 0.791 | False |

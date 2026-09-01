# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-01 20:11_

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

- Current-params net profit (full sample): **-11.1%**, PF 0.449, 71 trades, max DD -1109.89
- Optimizer out-of-sample: net **-2.79%**, PF 0.564, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-31 08:17 | 5000 | -10.51 | 0.461 | -1.89 | 0.661 | False |
| 2026-08-31 12:18 | 5000 | -10.51 | 0.461 | -2.01 | 0.647 | False |
| 2026-08-31 16:12 | 5000 | -10.51 | 0.461 | -2.01 | 0.647 | False |
| 2026-08-31 20:11 | 5000 | -10.54 | 0.461 | -1.92 | 0.661 | False |
| 2026-09-01 00:37 | 5000 | -10.82 | 0.454 | -2.15 | 0.626 | False |
| 2026-09-01 04:13 | 5000 | -10.82 | 0.454 | -2.14 | 0.627 | False |
| 2026-09-01 08:16 | 5000 | -10.66 | 0.458 | -2.01 | 0.642 | False |
| 2026-09-01 12:17 | 5000 | -10.66 | 0.458 | -2.45 | 0.594 | False |
| 2026-09-01 16:33 | 5000 | -10.66 | 0.458 | -1.93 | 0.651 | False |
| 2026-09-01 20:11 | 5000 | -11.1 | 0.449 | -2.79 | 0.564 | False |

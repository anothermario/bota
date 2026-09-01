# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-01 00:37_

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

- Current-params net profit (full sample): **-10.82%**, PF 0.454, 71 trades, max DD -1082.17
- Optimizer out-of-sample: net **-2.15%**, PF 0.626, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-30 12:15 | 5000 | -10.78 | 0.453 | -1.23 | 0.75 | False |
| 2026-08-30 16:10 | 5000 | -10.81 | 0.453 | -1.27 | 0.75 | False |
| 2026-08-30 20:09 | 5000 | -10.93 | 0.449 | -1.4 | 0.724 | False |
| 2026-08-31 00:34 | 5000 | -10.82 | 0.453 | -1.44 | 0.724 | False |
| 2026-08-31 04:14 | 5000 | -11.21 | 0.443 | -1.89 | 0.661 | False |
| 2026-08-31 08:17 | 5000 | -10.51 | 0.461 | -1.89 | 0.661 | False |
| 2026-08-31 12:18 | 5000 | -10.51 | 0.461 | -2.01 | 0.647 | False |
| 2026-08-31 16:12 | 5000 | -10.51 | 0.461 | -2.01 | 0.647 | False |
| 2026-08-31 20:11 | 5000 | -10.54 | 0.461 | -1.92 | 0.661 | False |
| 2026-09-01 00:37 | 5000 | -10.82 | 0.454 | -2.15 | 0.626 | False |

# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-22 21:05_

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

- Current-params net profit (full sample): **-10.84%**, PF 0.613, 72 trades, max DD -1715.47
- Optimizer out-of-sample: net **-8.08%**, PF 0.249, 24 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-21 10:24 | 5000 | -10.64 | 0.61 | -7.72 | 0.244 | False |
| 2026-07-21 13:46 | 5000 | -10.64 | 0.61 | -6.94 | 0.31 | False |
| 2026-07-21 17:18 | 5000 | -10.64 | 0.61 | -8.04 | 0.21 | False |
| 2026-07-21 21:07 | 5000 | -10.08 | 0.629 | -7.23 | 0.27 | False |
| 2026-07-22 02:32 | 5000 | -10.63 | 0.617 | -7.79 | 0.256 | False |
| 2026-07-22 06:27 | 5000 | -10.87 | 0.611 | -7.8 | 0.256 | False |
| 2026-07-22 10:24 | 5000 | -11.08 | 0.607 | -8.44 | 0.241 | False |
| 2026-07-22 13:50 | 5000 | -11.08 | 0.607 | -8.08 | 0.249 | False |
| 2026-07-22 17:17 | 5000 | -10.84 | 0.613 | -8.08 | 0.249 | False |
| 2026-07-22 21:05 | 5000 | -10.84 | 0.613 | -8.08 | 0.249 | False |

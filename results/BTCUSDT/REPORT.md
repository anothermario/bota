# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-21 21:07_

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

- Current-params net profit (full sample): **-10.08%**, PF 0.629, 71 trades, max DD -1664.83
- Optimizer out-of-sample: net **-7.23%**, PF 0.27, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-20 10:51 | 5000 | -9.38 | 0.638 | -6.88 | 0.264 | False |
| 2026-07-20 14:03 | 5000 | -10.21 | 0.619 | -7.73 | 0.242 | False |
| 2026-07-20 18:01 | 5000 | -10.23 | 0.619 | -7.75 | 0.242 | False |
| 2026-07-20 21:11 | 5000 | -10.74 | 0.607 | -8.28 | 0.23 | False |
| 2026-07-21 02:34 | 5000 | -10.5 | 0.614 | -8.09 | 0.248 | False |
| 2026-07-21 06:27 | 5000 | -10.51 | 0.614 | -8.64 | 0.221 | False |
| 2026-07-21 10:24 | 5000 | -10.64 | 0.61 | -7.72 | 0.244 | False |
| 2026-07-21 13:46 | 5000 | -10.64 | 0.61 | -6.94 | 0.31 | False |
| 2026-07-21 17:18 | 5000 | -10.64 | 0.61 | -8.04 | 0.21 | False |
| 2026-07-21 21:07 | 5000 | -10.08 | 0.629 | -7.23 | 0.27 | False |

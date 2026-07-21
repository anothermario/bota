# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-21 10:24_

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

- Current-params net profit (full sample): **-10.64%**, PF 0.61, 70 trades, max DD -1664.82
- Optimizer out-of-sample: net **-7.72%**, PF 0.244, 24 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-19 20:45 | 5000 | -8.26 | 0.667 | -5.65 | 0.326 | False |
| 2026-07-20 02:51 | 5000 | -8.98 | 0.648 | -6.63 | 0.27 | False |
| 2026-07-20 06:44 | 5000 | -8.97 | 0.648 | -6.63 | 0.27 | False |
| 2026-07-20 10:51 | 5000 | -9.38 | 0.638 | -6.88 | 0.264 | False |
| 2026-07-20 14:03 | 5000 | -10.21 | 0.619 | -7.73 | 0.242 | False |
| 2026-07-20 18:01 | 5000 | -10.23 | 0.619 | -7.75 | 0.242 | False |
| 2026-07-20 21:11 | 5000 | -10.74 | 0.607 | -8.28 | 0.23 | False |
| 2026-07-21 02:34 | 5000 | -10.5 | 0.614 | -8.09 | 0.248 | False |
| 2026-07-21 06:27 | 5000 | -10.51 | 0.614 | -8.64 | 0.221 | False |
| 2026-07-21 10:24 | 5000 | -10.64 | 0.61 | -7.72 | 0.244 | False |

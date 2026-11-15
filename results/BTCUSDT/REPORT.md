# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-11-15 12:09_

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
  "don_len": 15,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 26,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-7.72%**, PF 0.66, 69 trades, max DD -1393.1
- Optimizer out-of-sample: net **2.66%**, PF 1.379, 20 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-14 00:18 | 5000 | -18.37 | 0.288 | -2.08 | 0.764 | False |
| 2026-11-14 04:08 | 5000 | -18.41 | 0.288 | -1.72 | 0.8 | False |
| 2026-11-14 08:08 | 5000 | -18.14 | 0.292 | -1.19 | 0.851 | False |
| 2026-11-14 12:09 | 5000 | -18.53 | 0.273 | -1.12 | 0.859 | False |
| 2026-11-14 16:06 | 5000 | -18.56 | 0.273 | -0.37 | 0.953 | False |
| 2026-11-14 20:06 | 5000 | -18.24 | 0.284 | -0.41 | 0.948 | False |
| 2026-11-15 00:21 | 5000 | -18.24 | 0.284 | -0.16 | 0.982 | False |
| 2026-11-15 04:08 | 5000 | -18.69 | 0.28 | 2.66 | 1.379 | True |
| 2026-11-15 08:09 | 5000 | -8.69 | 0.631 | 2.66 | 1.379 | True |
| 2026-11-15 12:09 | 5000 | -7.72 | 0.66 | 2.66 | 1.379 | True |

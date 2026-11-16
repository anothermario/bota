# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-11-16 20:07_

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

- Current-params net profit (full sample): **-6.78%**, PF 0.691, 68 trades, max DD -1304.87
- Optimizer out-of-sample: net **2.81%**, PF 1.409, 19 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-15 08:09 | 5000 | -8.69 | 0.631 | 2.66 | 1.379 | True |
| 2026-11-15 12:09 | 5000 | -7.72 | 0.66 | 2.66 | 1.379 | True |
| 2026-11-15 16:07 | 5000 | -7.73 | 0.66 | 2.66 | 1.379 | True |
| 2026-11-15 20:07 | 5000 | -7.72 | 0.66 | 2.66 | 1.379 | True |
| 2026-11-16 00:24 | 5000 | -8.41 | 0.639 | 2.66 | 1.379 | True |
| 2026-11-16 04:09 | 5000 | -7.73 | 0.66 | 2.66 | 1.379 | True |
| 2026-11-16 08:22 | 5000 | -6.78 | 0.691 | 2.66 | 1.379 | True |
| 2026-11-16 12:14 | 5000 | -6.78 | 0.691 | 2.62 | 1.372 | True |
| 2026-11-16 16:08 | 5000 | -6.78 | 0.691 | 2.34 | 1.321 | True |
| 2026-11-16 20:07 | 5000 | -6.78 | 0.691 | 2.81 | 1.409 | True |

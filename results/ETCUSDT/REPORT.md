# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-22 00:14_

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
  "chand_len": 26,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-7.92%**, PF 0.597, 51 trades, max DD -1081.64
- Optimizer out-of-sample: net **1.62%**, PF 1.447, 16 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-20 12:10 | 5000 | -13.31 | 0.431 | -2.39 | 0.502 | False |
| 2026-08-20 16:09 | 5000 | -12.64 | 0.445 | -1.84 | 0.569 | False |
| 2026-08-20 20:08 | 5000 | -11.85 | 0.479 | -0.98 | 0.768 | False |
| 2026-08-21 00:15 | 5000 | -11.98 | 0.473 | -0.98 | 0.768 | False |
| 2026-08-21 04:16 | 5000 | -11.99 | 0.473 | -1.0 | 0.768 | False |
| 2026-08-21 08:14 | 5000 | -12.54 | 0.464 | -1.0 | 0.768 | False |
| 2026-08-21 12:10 | 5000 | -9.41 | 0.583 | 1.09 | 1.258 | True |
| 2026-08-21 16:09 | 5000 | -8.38 | 0.582 | 1.9 | 1.517 | True |
| 2026-08-21 20:06 | 5000 | -8.59 | 0.584 | 1.66 | 1.458 | True |
| 2026-08-22 00:14 | 5000 | -7.92 | 0.597 | 1.62 | 1.447 | True |

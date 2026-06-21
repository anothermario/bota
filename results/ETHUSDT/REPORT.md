# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-06-21 05:40_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.25,
  "use_adx": true,
  "adx_len": 14,
  "adx_thresh": 20.0,
  "don_len": 15,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-12.23%**, PF 0.572, 89 trades, max DD -1337.96
- Optimizer out-of-sample: net **-4.12%**, PF 0.584, 24 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-19 16:52 | 5000 | -10.51 | 0.62 | -1.22 | 0.856 | False |
| 2026-06-19 20:34 | 5000 | -10.55 | 0.619 | 0.0 | 1.0 | False |
| 2026-06-20 00:53 | 5000 | -9.78 | 0.639 | -0.0 | 1.0 | False |
| 2026-06-20 05:33 | 5000 | -10.82 | 0.613 | -0.02 | 1.004 | False |
| 2026-06-20 09:08 | 5000 | -10.13 | 0.631 | -0.73 | 0.913 | False |
| 2026-06-20 12:41 | 5000 | -11.24 | 0.591 | -0.93 | 0.888 | False |
| 2026-06-20 16:35 | 5000 | -12.52 | 0.564 | -2.84 | 0.594 | False |
| 2026-06-20 20:31 | 5000 | -12.51 | 0.564 | -2.85 | 0.593 | False |
| 2026-06-21 00:58 | 5000 | -11.84 | 0.58 | -3.99 | 0.593 | False |
| 2026-06-21 05:40 | 5000 | -12.23 | 0.572 | -4.12 | 0.584 | False |

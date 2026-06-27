# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-06-27 20:27_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.3,
  "use_adx": true,
  "adx_len": 14,
  "adx_thresh": 20.0,
  "don_len": 15,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 18,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-9.74%**, PF 0.66, 77 trades, max DD -1217.12
- Optimizer out-of-sample: net **1.76%**, PF 1.29, 16 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-26 09:10 | 5000 | -7.66 | 0.733 | 1.68 | 1.274 | True |
| 2026-06-26 12:48 | 5000 | -7.63 | 0.734 | 1.68 | 1.275 | True |
| 2026-06-26 16:44 | 5000 | -8.96 | 0.689 | 2.05 | 1.355 | True |
| 2026-06-26 20:37 | 5000 | -8.45 | 0.703 | 1.12 | 1.172 | True |
| 2026-06-27 00:50 | 5000 | -9.45 | 0.668 | 0.85 | 1.123 | True |
| 2026-06-27 05:21 | 5000 | -9.45 | 0.668 | 1.76 | 1.29 | True |
| 2026-06-27 08:59 | 5000 | -9.45 | 0.668 | 1.76 | 1.29 | True |
| 2026-06-27 12:32 | 5000 | -8.78 | 0.685 | 1.76 | 1.29 | True |
| 2026-06-27 16:27 | 5000 | -9.72 | 0.661 | 1.76 | 1.29 | True |
| 2026-06-27 20:27 | 5000 | -9.74 | 0.66 | 1.76 | 1.29 | True |

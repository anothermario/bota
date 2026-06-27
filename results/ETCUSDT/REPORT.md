# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-06-27 00:50_

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

- Current-params net profit (full sample): **-9.45%**, PF 0.668, 77 trades, max DD -1221.1
- Optimizer out-of-sample: net **0.85%**, PF 1.123, 17 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-25 12:52 | 5000 | -6.33 | 0.767 | 2.72 | 1.542 | True |
| 2026-06-25 16:49 | 5000 | -7.38 | 0.739 | 1.56 | 1.253 | True |
| 2026-06-25 20:43 | 5000 | -7.38 | 0.739 | 1.56 | 1.253 | True |
| 2026-06-26 00:53 | 5000 | -7.38 | 0.739 | 2.59 | 1.498 | True |
| 2026-06-26 05:30 | 5000 | -8.21 | 0.717 | 1.45 | 1.23 | True |
| 2026-06-26 09:10 | 5000 | -7.66 | 0.733 | 1.68 | 1.274 | True |
| 2026-06-26 12:48 | 5000 | -7.63 | 0.734 | 1.68 | 1.275 | True |
| 2026-06-26 16:44 | 5000 | -8.96 | 0.689 | 2.05 | 1.355 | True |
| 2026-06-26 20:37 | 5000 | -8.45 | 0.703 | 1.12 | 1.172 | True |
| 2026-06-27 00:50 | 5000 | -9.45 | 0.668 | 0.85 | 1.123 | True |

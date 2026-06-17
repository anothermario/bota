# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-06-17 05:43_

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

- Current-params net profit (full sample): **-7.37%**, PF 0.646, 64 trades, max DD -926.73
- Optimizer out-of-sample: net **0.6%**, PF 1.082, 19 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-15 17:41 | 5000 | -6.39 | 0.676 | 3.59 | 1.608 | True |
| 2026-06-15 21:05 | 5000 | -6.6 | 0.668 | 3.32 | 1.539 | True |
| 2026-06-16 01:04 | 5000 | -6.63 | 0.669 | 3.57 | 1.613 | True |
| 2026-06-16 05:54 | 5000 | -6.55 | 0.671 | 3.61 | 1.611 | True |
| 2026-06-16 09:51 | 5000 | -6.59 | 0.671 | 3.57 | 1.611 | True |
| 2026-06-16 13:53 | 5000 | -7.45 | 0.641 | 2.73 | 1.402 | True |
| 2026-06-16 17:45 | 5000 | -7.49 | 0.641 | 2.23 | 1.336 | True |
| 2026-06-16 21:05 | 5000 | -8.07 | 0.623 | -0.07 | 0.991 | False |
| 2026-06-17 00:58 | 5000 | -7.75 | 0.633 | 0.6 | 1.081 | True |
| 2026-06-17 05:43 | 5000 | -7.37 | 0.646 | 0.6 | 1.082 | True |

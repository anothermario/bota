# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-06-28 20:29_

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

- Current-params net profit (full sample): **-7.53%**, PF 0.722, 76 trades, max DD -1251.62
- Optimizer out-of-sample: net **1.38%**, PF 1.214, 17 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-27 08:59 | 5000 | -9.45 | 0.668 | 1.76 | 1.29 | True |
| 2026-06-27 12:32 | 5000 | -8.78 | 0.685 | 1.76 | 1.29 | True |
| 2026-06-27 16:27 | 5000 | -9.72 | 0.661 | 1.76 | 1.29 | True |
| 2026-06-27 20:27 | 5000 | -9.74 | 0.66 | 1.76 | 1.29 | True |
| 2026-06-28 00:53 | 5000 | -7.95 | 0.709 | 0.98 | 1.15 | True |
| 2026-06-28 05:34 | 5000 | -8.27 | 0.7 | 0.66 | 1.093 | True |
| 2026-06-28 09:07 | 5000 | -8.27 | 0.7 | 1.38 | 1.214 | True |
| 2026-06-28 12:33 | 5000 | -8.27 | 0.7 | 1.38 | 1.214 | True |
| 2026-06-28 16:30 | 5000 | -8.27 | 0.7 | 1.38 | 1.214 | True |
| 2026-06-28 20:29 | 5000 | -7.53 | 0.722 | 1.38 | 1.214 | True |

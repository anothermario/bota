# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-06-25 20:43_

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

- Current-params net profit (full sample): **-7.38%**, PF 0.739, 77 trades, max DD -1234.21
- Optimizer out-of-sample: net **1.56%**, PF 1.253, 17 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-24 09:11 | 5000 | -8.45 | 0.693 | 2.09 | 1.482 | True |
| 2026-06-24 12:50 | 5000 | -9.33 | 0.671 | 1.13 | 1.225 | False |
| 2026-06-24 16:48 | 5000 | -9.35 | 0.671 | 1.11 | 1.225 | False |
| 2026-06-24 20:38 | 5000 | -8.52 | 0.7 | 2.04 | 1.406 | True |
| 2026-06-25 00:52 | 5000 | -7.89 | 0.718 | 2.02 | 1.406 | True |
| 2026-06-25 05:24 | 5000 | -7.89 | 0.718 | 2.02 | 1.406 | True |
| 2026-06-25 09:11 | 5000 | -7.9 | 0.718 | 2.02 | 1.406 | True |
| 2026-06-25 12:52 | 5000 | -6.33 | 0.767 | 2.72 | 1.542 | True |
| 2026-06-25 16:49 | 5000 | -7.38 | 0.739 | 1.56 | 1.253 | True |
| 2026-06-25 20:43 | 5000 | -7.38 | 0.739 | 1.56 | 1.253 | True |

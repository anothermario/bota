# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-06-29 20:40_

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

- Current-params net profit (full sample): **-9.96%**, PF 0.658, 81 trades, max DD -1235.03
- Optimizer out-of-sample: net **2.38%**, PF 1.368, 17 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-28 09:07 | 5000 | -8.27 | 0.7 | 1.38 | 1.214 | True |
| 2026-06-28 12:33 | 5000 | -8.27 | 0.7 | 1.38 | 1.214 | True |
| 2026-06-28 16:30 | 5000 | -8.27 | 0.7 | 1.38 | 1.214 | True |
| 2026-06-28 20:29 | 5000 | -7.53 | 0.722 | 1.38 | 1.214 | True |
| 2026-06-29 00:54 | 5000 | -7.5 | 0.723 | 1.38 | 1.214 | True |
| 2026-06-29 05:39 | 5000 | -8.28 | 0.7 | 1.38 | 1.214 | True |
| 2026-06-29 09:40 | 5000 | -7.6 | 0.719 | 1.38 | 1.187 | True |
| 2026-06-29 13:34 | 5000 | -8.09 | 0.699 | 1.9 | 1.275 | True |
| 2026-06-29 17:04 | 5000 | -8.09 | 0.699 | 1.36 | 1.183 | True |
| 2026-06-29 20:40 | 5000 | -9.96 | 0.658 | 2.38 | 1.368 | True |

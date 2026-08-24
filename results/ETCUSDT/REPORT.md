# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-24 04:18_

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

- Current-params net profit (full sample): **-3.07%**, PF 0.842, 51 trades, max DD -1073.5
- Optimizer out-of-sample: net **7.3%**, PF 3.449, 15 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-22 16:05 | 5000 | -3.37 | 0.829 | 6.54 | 2.788 | True |
| 2026-08-22 20:05 | 5000 | -3.37 | 0.829 | 6.54 | 2.788 | True |
| 2026-08-23 00:15 | 5000 | -3.37 | 0.828 | 6.54 | 2.788 | True |
| 2026-08-23 04:15 | 5000 | -3.36 | 0.829 | 6.54 | 2.788 | True |
| 2026-08-23 08:08 | 5000 | -3.08 | 0.841 | 6.54 | 2.788 | True |
| 2026-08-23 12:07 | 5000 | -3.08 | 0.841 | 6.54 | 2.789 | True |
| 2026-08-23 16:05 | 5000 | -3.08 | 0.841 | 6.55 | 2.794 | True |
| 2026-08-23 20:04 | 5000 | -3.08 | 0.841 | 6.55 | 2.794 | True |
| 2026-08-24 00:15 | 5000 | -3.08 | 0.841 | 6.62 | 2.843 | True |
| 2026-08-24 04:18 | 5000 | -3.07 | 0.842 | 7.3 | 3.449 | True |

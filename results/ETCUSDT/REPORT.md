# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-23 08:08_

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

- Current-params net profit (full sample): **-3.08%**, PF 0.841, 51 trades, max DD -1073.43
- Optimizer out-of-sample: net **6.54%**, PF 2.788, 16 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-21 20:06 | 5000 | -8.59 | 0.584 | 1.66 | 1.458 | True |
| 2026-08-22 00:14 | 5000 | -7.92 | 0.597 | 1.62 | 1.447 | True |
| 2026-08-22 04:13 | 5000 | -8.27 | 0.586 | 1.52 | 1.42 | True |
| 2026-08-22 08:08 | 5000 | -3.56 | 0.82 | 6.54 | 2.788 | True |
| 2026-08-22 12:07 | 5000 | -3.37 | 0.829 | 6.54 | 2.788 | True |
| 2026-08-22 16:05 | 5000 | -3.37 | 0.829 | 6.54 | 2.788 | True |
| 2026-08-22 20:05 | 5000 | -3.37 | 0.829 | 6.54 | 2.788 | True |
| 2026-08-23 00:15 | 5000 | -3.37 | 0.828 | 6.54 | 2.788 | True |
| 2026-08-23 04:15 | 5000 | -3.36 | 0.829 | 6.54 | 2.788 | True |
| 2026-08-23 08:08 | 5000 | -3.08 | 0.841 | 6.54 | 2.788 | True |

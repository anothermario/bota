# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-28 04:15_

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

- Current-params net profit (full sample): **-2.01%**, PF 0.907, 54 trades, max DD -855.27
- Optimizer out-of-sample: net **-3.74%**, PF 0.535, 18 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-26 16:12 | 5000 | -0.89 | 0.956 | -3.54 | 0.546 | False |
| 2026-09-26 20:10 | 5000 | -0.89 | 0.956 | -2.61 | 0.622 | False |
| 2026-09-27 00:36 | 5000 | -0.77 | 0.963 | -2.46 | 0.638 | False |
| 2026-09-27 04:13 | 5000 | -1.56 | 0.926 | -2.77 | 0.609 | False |
| 2026-09-27 08:14 | 5000 | -0.99 | 0.952 | -2.53 | 0.641 | False |
| 2026-09-27 12:16 | 5000 | -0.95 | 0.954 | -2.51 | 0.642 | False |
| 2026-09-27 16:12 | 5000 | -1.13 | 0.945 | -2.22 | 0.67 | False |
| 2026-09-27 20:11 | 5000 | -1.13 | 0.945 | -2.22 | 0.671 | False |
| 2026-09-28 00:35 | 5000 | -2.01 | 0.907 | -2.72 | 0.625 | False |
| 2026-09-28 04:15 | 5000 | -2.01 | 0.907 | -3.74 | 0.535 | False |

# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-27 12:16_

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

- Current-params net profit (full sample): **-0.95%**, PF 0.954, 54 trades, max DD -821.06
- Optimizer out-of-sample: net **-2.51%**, PF 0.642, 18 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-26 00:30 | 5000 | -1.45 | 0.931 | -4.12 | 0.507 | False |
| 2026-09-26 04:13 | 5000 | -0.89 | 0.956 | -4.12 | 0.507 | False |
| 2026-09-26 08:15 | 5000 | -0.89 | 0.956 | -4.12 | 0.507 | False |
| 2026-09-26 12:15 | 5000 | -0.89 | 0.956 | -4.12 | 0.507 | False |
| 2026-09-26 16:12 | 5000 | -0.89 | 0.956 | -3.54 | 0.546 | False |
| 2026-09-26 20:10 | 5000 | -0.89 | 0.956 | -2.61 | 0.622 | False |
| 2026-09-27 00:36 | 5000 | -0.77 | 0.963 | -2.46 | 0.638 | False |
| 2026-09-27 04:13 | 5000 | -1.56 | 0.926 | -2.77 | 0.609 | False |
| 2026-09-27 08:14 | 5000 | -0.99 | 0.952 | -2.53 | 0.641 | False |
| 2026-09-27 12:16 | 5000 | -0.95 | 0.954 | -2.51 | 0.642 | False |

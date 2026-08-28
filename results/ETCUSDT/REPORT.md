# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-28 16:11_

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

- Current-params net profit (full sample): **-3.41%**, PF 0.824, 49 trades, max DD -944.37
- Optimizer out-of-sample: net **5.52%**, PF 2.195, 15 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-27 01:35 | 5000 | -2.55 | 0.863 | 6.27 | 2.571 | True |
| 2026-08-27 06:08 | 5000 | -2.55 | 0.863 | 6.27 | 2.571 | True |
| 2026-08-27 11:26 | 5000 | -2.86 | 0.848 | 5.93 | 2.36 | True |
| 2026-08-27 15:44 | 5000 | -2.27 | 0.878 | 5.94 | 2.362 | True |
| 2026-08-27 19:33 | 5000 | -2.25 | 0.879 | 6.62 | 2.769 | True |
| 2026-08-27 23:09 | 5000 | -2.85 | 0.848 | 6.62 | 2.769 | True |
| 2026-08-28 02:57 | 5000 | -2.76 | 0.856 | 6.67 | 2.81 | True |
| 2026-08-28 06:36 | 5000 | -2.55 | 0.862 | 6.46 | 2.757 | False |
| 2026-08-28 11:54 | 5000 | -2.55 | 0.862 | 5.47 | 2.197 | True |
| 2026-08-28 16:11 | 5000 | -3.41 | 0.824 | 5.52 | 2.195 | True |

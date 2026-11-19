# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-11-19 00:19_

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

- Current-params net profit (full sample): **-13.81%**, PF 0.466, 66 trades, max DD -1422.26
- Optimizer out-of-sample: net **-3.34%**, PF 0.66, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-17 12:10 | 5000 | -14.08 | 0.457 | -4.09 | 0.609 | False |
| 2026-11-17 16:08 | 5000 | -13.5 | 0.47 | -4.09 | 0.609 | False |
| 2026-11-17 20:07 | 5000 | -13.5 | 0.47 | -3.57 | 0.642 | False |
| 2026-11-18 00:19 | 5000 | -13.51 | 0.47 | -3.6 | 0.642 | False |
| 2026-11-18 04:08 | 5000 | -14.02 | 0.46 | -2.83 | 0.694 | False |
| 2026-11-18 08:10 | 5000 | -14.02 | 0.46 | -3.23 | 0.667 | False |
| 2026-11-18 12:10 | 5000 | -14.03 | 0.46 | -3.23 | 0.667 | False |
| 2026-11-18 16:07 | 5000 | -13.25 | 0.477 | -3.25 | 0.667 | False |
| 2026-11-18 20:07 | 5000 | -13.81 | 0.466 | -3.55 | 0.646 | False |
| 2026-11-19 00:19 | 5000 | -13.81 | 0.466 | -3.34 | 0.66 | False |

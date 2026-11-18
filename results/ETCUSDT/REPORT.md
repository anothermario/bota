# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-11-18 04:08_

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

- Current-params net profit (full sample): **-14.02%**, PF 0.46, 66 trades, max DD -1498.48
- Optimizer out-of-sample: net **-2.83%**, PF 0.694, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-16 16:08 | 5000 | -13.36 | 0.471 | -3.0 | 0.681 | False |
| 2026-11-16 20:07 | 5000 | -13.36 | 0.471 | -3.0 | 0.681 | False |
| 2026-11-17 00:19 | 5000 | -14.02 | 0.457 | -4.07 | 0.609 | False |
| 2026-11-17 04:08 | 5000 | -14.02 | 0.457 | -4.06 | 0.609 | False |
| 2026-11-17 08:09 | 5000 | -13.36 | 0.471 | -3.51 | 0.645 | False |
| 2026-11-17 12:10 | 5000 | -14.08 | 0.457 | -4.09 | 0.609 | False |
| 2026-11-17 16:08 | 5000 | -13.5 | 0.47 | -4.09 | 0.609 | False |
| 2026-11-17 20:07 | 5000 | -13.5 | 0.47 | -3.57 | 0.642 | False |
| 2026-11-18 00:19 | 5000 | -13.51 | 0.47 | -3.6 | 0.642 | False |
| 2026-11-18 04:08 | 5000 | -14.02 | 0.46 | -2.83 | 0.694 | False |

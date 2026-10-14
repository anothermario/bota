# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-14 04:14_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.25,
  "use_adx": true,
  "adx_len": 14,
  "adx_thresh": 20.0,
  "don_len": 15,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-13.84%**, PF 0.556, 102 trades, max DD -1576.51
- Optimizer out-of-sample: net **-2.74%**, PF 0.621, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-12 16:12 | 5000 | -15.36 | 0.506 | -6.66 | 0.216 | False |
| 2026-10-12 20:12 | 5000 | -16.06 | 0.479 | -5.95 | 0.204 | False |
| 2026-10-13 00:35 | 5000 | -16.07 | 0.479 | -5.95 | 0.204 | False |
| 2026-10-13 04:18 | 5000 | -14.51 | 0.54 | -2.98 | 0.599 | False |
| 2026-10-13 08:21 | 5000 | -14.09 | 0.549 | -3.01 | 0.599 | False |
| 2026-10-13 12:19 | 5000 | -14.85 | 0.536 | -3.47 | 0.562 | False |
| 2026-10-13 16:13 | 5000 | -14.84 | 0.536 | -3.47 | 0.562 | False |
| 2026-10-13 20:12 | 5000 | -14.28 | 0.547 | -3.75 | 0.542 | False |
| 2026-10-14 00:28 | 5000 | -14.28 | 0.547 | -2.74 | 0.621 | False |
| 2026-10-14 04:14 | 5000 | -13.84 | 0.556 | -2.74 | 0.621 | False |

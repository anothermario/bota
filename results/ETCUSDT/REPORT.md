# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-28 04:10_

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

- Current-params net profit (full sample): **-12.63%**, PF 0.498, 64 trades, max DD -1577.35
- Optimizer out-of-sample: net **-3.87%**, PF 0.559, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-26 16:15 | 5000 | -12.07 | 0.539 | -4.33 | 0.529 | False |
| 2026-10-26 20:11 | 5000 | -12.42 | 0.524 | -2.89 | 0.724 | False |
| 2026-10-27 00:29 | 5000 | -13.34 | 0.483 | -4.02 | 0.549 | False |
| 2026-10-27 04:12 | 5000 | -13.42 | 0.479 | -4.02 | 0.549 | False |
| 2026-10-27 08:15 | 5000 | -13.43 | 0.479 | -4.02 | 0.549 | False |
| 2026-10-27 12:17 | 5000 | -13.43 | 0.479 | -4.02 | 0.549 | False |
| 2026-10-27 16:10 | 5000 | -12.6 | 0.498 | -4.02 | 0.549 | False |
| 2026-10-27 20:09 | 5000 | -12.6 | 0.498 | -4.01 | 0.549 | False |
| 2026-10-28 00:22 | 5000 | -12.6 | 0.498 | -3.58 | 0.578 | False |
| 2026-10-28 04:10 | 5000 | -12.63 | 0.498 | -3.87 | 0.559 | False |

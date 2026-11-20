# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-11-20 16:08_

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

- Current-params net profit (full sample): **-12.64%**, PF 0.494, 64 trades, max DD -1264.17
- Optimizer out-of-sample: net **-4.76%**, PF 0.535, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-19 04:08 | 5000 | -13.44 | 0.474 | -3.37 | 0.657 | False |
| 2026-11-19 08:10 | 5000 | -13.44 | 0.474 | -3.41 | 0.652 | False |
| 2026-11-19 12:10 | 5000 | -13.2 | 0.479 | -4.25 | 0.58 | False |
| 2026-11-19 16:08 | 5000 | -13.22 | 0.479 | -3.88 | 0.604 | False |
| 2026-11-19 20:08 | 5000 | -13.46 | 0.474 | -3.46 | 0.633 | False |
| 2026-11-20 00:18 | 5000 | -13.37 | 0.476 | -3.75 | 0.614 | False |
| 2026-11-20 04:08 | 5000 | -13.37 | 0.476 | -4.86 | 0.527 | False |
| 2026-11-20 08:10 | 5000 | -12.72 | 0.491 | -4.88 | 0.527 | False |
| 2026-11-20 12:10 | 5000 | -12.63 | 0.494 | -4.75 | 0.535 | False |
| 2026-11-20 16:08 | 5000 | -12.64 | 0.494 | -4.76 | 0.535 | False |

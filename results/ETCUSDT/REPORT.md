# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-29 12:13_

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

- Current-params net profit (full sample): **-13.33%**, PF 0.493, 67 trades, max DD -1584.29
- Optimizer out-of-sample: net **-3.51%**, PF 0.6, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-28 00:22 | 5000 | -12.6 | 0.498 | -3.58 | 0.578 | False |
| 2026-10-28 04:10 | 5000 | -12.63 | 0.498 | -3.87 | 0.559 | False |
| 2026-10-28 08:11 | 5000 | -13.0 | 0.49 | -5.29 | 0.437 | False |
| 2026-10-28 12:12 | 5000 | -13.0 | 0.49 | -4.59 | 0.474 | False |
| 2026-10-28 16:10 | 5000 | -13.04 | 0.49 | -4.57 | 0.517 | False |
| 2026-10-28 20:09 | 5000 | -13.28 | 0.486 | -3.44 | 0.535 | False |
| 2026-10-29 00:22 | 5000 | -14.63 | 0.459 | -4.53 | 0.483 | False |
| 2026-10-29 04:10 | 5000 | -14.65 | 0.459 | -4.03 | 0.495 | False |
| 2026-10-29 08:11 | 5000 | -13.33 | 0.493 | -3.5 | 0.559 | False |
| 2026-10-29 12:13 | 5000 | -13.33 | 0.493 | -3.51 | 0.6 | False |

# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-23 16:12_

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

- Current-params net profit (full sample): **-11.45%**, PF 0.557, 65 trades, max DD -1593.1
- Optimizer out-of-sample: net **-3.44%**, PF 0.595, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-22 04:13 | 5000 | -13.54 | 0.477 | -5.82 | 0.347 | False |
| 2026-10-22 08:15 | 5000 | -13.54 | 0.477 | -5.82 | 0.347 | False |
| 2026-10-22 12:17 | 5000 | -13.54 | 0.477 | -5.45 | 0.363 | False |
| 2026-10-22 16:13 | 5000 | -13.54 | 0.477 | -5.45 | 0.363 | False |
| 2026-10-22 20:11 | 5000 | -13.54 | 0.477 | -5.45 | 0.363 | False |
| 2026-10-23 00:30 | 5000 | -11.76 | 0.545 | -3.51 | 0.588 | False |
| 2026-10-23 04:13 | 5000 | -11.79 | 0.545 | -3.87 | 0.551 | False |
| 2026-10-23 08:15 | 5000 | -11.79 | 0.545 | -4.81 | 0.494 | False |
| 2026-10-23 12:15 | 5000 | -11.79 | 0.545 | -3.81 | 0.555 | False |
| 2026-10-23 16:12 | 5000 | -11.45 | 0.557 | -3.44 | 0.595 | False |

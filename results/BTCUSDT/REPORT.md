# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-12 12:19_

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
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-11.48%**, PF 0.479, 71 trades, max DD -1304.69
- Optimizer out-of-sample: net **-4.78%**, PF 0.344, 30 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-11 00:20 | 5000 | -12.72 | 0.44 | -5.29 | 0.282 | False |
| 2026-08-11 04:31 | 5000 | -12.34 | 0.456 | -4.87 | 0.333 | False |
| 2026-08-11 08:23 | 5000 | -12.34 | 0.456 | -4.75 | 0.34 | False |
| 2026-08-11 12:18 | 5000 | -12.37 | 0.456 | -4.78 | 0.34 | False |
| 2026-08-11 16:19 | 5000 | -12.76 | 0.448 | -5.41 | 0.311 | False |
| 2026-08-11 20:15 | 5000 | -12.66 | 0.451 | -5.02 | 0.331 | False |
| 2026-08-12 00:24 | 5000 | -12.25 | 0.46 | -3.87 | 0.421 | False |
| 2026-08-12 04:36 | 5000 | -11.88 | 0.469 | -3.26 | 0.515 | False |
| 2026-08-12 08:31 | 5000 | -11.88 | 0.469 | -4.15 | 0.376 | False |
| 2026-08-12 12:19 | 5000 | -11.48 | 0.479 | -4.78 | 0.344 | False |

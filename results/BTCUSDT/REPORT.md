# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-10-18 04:12_

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

- Current-params net profit (full sample): **-12.78%**, PF 0.455, 63 trades, max DD -1277.65
- Optimizer out-of-sample: net **-3.01%**, PF 0.369, 16 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-16 16:12 | 5000 | -11.42 | 0.482 | -3.17 | 0.389 | False |
| 2026-10-16 20:10 | 5000 | -12.06 | 0.469 | -3.83 | 0.345 | False |
| 2026-10-17 00:28 | 5000 | -12.06 | 0.469 | -3.83 | 0.345 | False |
| 2026-10-17 04:12 | 5000 | -12.06 | 0.469 | -3.25 | 0.384 | False |
| 2026-10-17 08:12 | 5000 | -12.06 | 0.469 | -3.27 | 0.383 | False |
| 2026-10-17 12:14 | 5000 | -12.06 | 0.469 | -2.24 | 0.478 | False |
| 2026-10-17 16:10 | 5000 | -12.64 | 0.456 | -2.24 | 0.478 | False |
| 2026-10-17 20:10 | 5000 | -12.06 | 0.469 | -2.24 | 0.478 | False |
| 2026-10-18 00:31 | 5000 | -12.85 | 0.452 | -3.0 | 0.366 | False |
| 2026-10-18 04:12 | 5000 | -12.78 | 0.455 | -3.01 | 0.369 | False |

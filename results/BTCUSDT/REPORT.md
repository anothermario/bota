# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-11 16:19_

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

- Current-params net profit (full sample): **-12.76%**, PF 0.448, 72 trades, max DD -1286.48
- Optimizer out-of-sample: net **-5.41%**, PF 0.311, 31 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-10 04:33 | 5000 | -13.02 | 0.433 | -6.3 | 0.244 | False |
| 2026-08-10 08:34 | 5000 | -13.02 | 0.433 | -6.3 | 0.244 | False |
| 2026-08-10 12:18 | 5000 | -13.02 | 0.433 | -6.0 | 0.254 | False |
| 2026-08-10 16:18 | 5000 | -13.06 | 0.433 | -5.67 | 0.267 | False |
| 2026-08-10 20:14 | 5000 | -12.72 | 0.44 | -5.41 | 0.277 | False |
| 2026-08-11 00:20 | 5000 | -12.72 | 0.44 | -5.29 | 0.282 | False |
| 2026-08-11 04:31 | 5000 | -12.34 | 0.456 | -4.87 | 0.333 | False |
| 2026-08-11 08:23 | 5000 | -12.34 | 0.456 | -4.75 | 0.34 | False |
| 2026-08-11 12:18 | 5000 | -12.37 | 0.456 | -4.78 | 0.34 | False |
| 2026-08-11 16:19 | 5000 | -12.76 | 0.448 | -5.41 | 0.311 | False |

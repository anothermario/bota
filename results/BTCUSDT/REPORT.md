# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-13 08:33_

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

- Current-params net profit (full sample): **-11.5%**, PF 0.48, 71 trades, max DD -1375.27
- Optimizer out-of-sample: net **-1.68%**, PF 0.592, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-11 20:15 | 5000 | -12.66 | 0.451 | -5.02 | 0.331 | False |
| 2026-08-12 00:24 | 5000 | -12.25 | 0.46 | -3.87 | 0.421 | False |
| 2026-08-12 04:36 | 5000 | -11.88 | 0.469 | -3.26 | 0.515 | False |
| 2026-08-12 08:31 | 5000 | -11.88 | 0.469 | -4.15 | 0.376 | False |
| 2026-08-12 12:19 | 5000 | -11.48 | 0.479 | -4.78 | 0.344 | False |
| 2026-08-12 16:20 | 5000 | -12.14 | 0.464 | -5.65 | 0.306 | False |
| 2026-08-12 20:15 | 5000 | -11.28 | 0.485 | -5.64 | 0.306 | False |
| 2026-08-13 00:25 | 5000 | -11.7 | 0.475 | -4.9 | 0.338 | False |
| 2026-08-13 04:37 | 5000 | -11.27 | 0.491 | -4.83 | 0.342 | False |
| 2026-08-13 08:33 | 5000 | -11.5 | 0.48 | -1.68 | 0.592 | False |

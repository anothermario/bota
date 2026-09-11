# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-11 00:30_

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

- Current-params net profit (full sample): **-7.13%**, PF 0.586, 64 trades, max DD -771.69
- Optimizer out-of-sample: net **-3.71%**, PF 0.448, 15 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-09 12:16 | 5000 | -8.64 | 0.532 | -3.91 | 0.432 | False |
| 2026-09-09 16:12 | 5000 | -8.65 | 0.531 | -3.91 | 0.432 | False |
| 2026-09-09 20:10 | 5000 | -7.92 | 0.555 | -2.44 | 0.553 | False |
| 2026-09-10 00:29 | 5000 | -7.95 | 0.555 | -3.94 | 0.432 | False |
| 2026-09-10 04:13 | 5000 | -8.02 | 0.554 | -4.64 | 0.391 | False |
| 2026-09-10 08:15 | 5000 | -7.16 | 0.584 | -3.18 | 0.487 | False |
| 2026-09-10 12:16 | 5000 | -7.47 | 0.573 | -3.98 | 0.429 | False |
| 2026-09-10 16:11 | 5000 | -6.65 | 0.604 | -4.02 | 0.429 | False |
| 2026-09-10 20:10 | 5000 | -7.13 | 0.586 | -3.71 | 0.448 | False |
| 2026-09-11 00:30 | 5000 | -7.13 | 0.586 | -3.71 | 0.448 | False |

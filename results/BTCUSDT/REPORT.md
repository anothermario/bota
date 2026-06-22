# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-06-22 10:05_

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

- Current-params net profit (full sample): **-7.96%**, PF 0.629, 63 trades, max DD -795.74
- Optimizer out-of-sample: net **-5.97%**, PF 0.341, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-20 20:31 | 5000 | -5.92 | 0.7 | -4.45 | 0.406 | False |
| 2026-06-21 00:58 | 5000 | -5.92 | 0.7 | -4.22 | 0.42 | False |
| 2026-06-21 05:40 | 5000 | -6.37 | 0.685 | -4.67 | 0.395 | False |
| 2026-06-21 09:19 | 5000 | -6.4 | 0.685 | -5.29 | 0.366 | False |
| 2026-06-21 12:44 | 5000 | -6.77 | 0.672 | -5.08 | 0.375 | False |
| 2026-06-21 16:36 | 5000 | -7.22 | 0.656 | -5.08 | 0.375 | False |
| 2026-06-21 20:35 | 5000 | -7.21 | 0.656 | -5.08 | 0.375 | False |
| 2026-06-22 00:58 | 5000 | -7.67 | 0.643 | -6.0 | 0.338 | False |
| 2026-06-22 05:53 | 5000 | -7.66 | 0.644 | -5.55 | 0.39 | False |
| 2026-06-22 10:05 | 5000 | -7.96 | 0.629 | -5.97 | 0.341 | False |

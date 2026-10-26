# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-10-26 08:21_

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
  "atr_mult": 3.0,
  "chand_len": 18,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-11.71%**, PF 0.481, 70 trades, max DD -1171.44
- Optimizer out-of-sample: net **-5.03%**, PF 0.44, 29 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-24 20:09 | 5000 | -7.86 | 0.647 | -1.79 | 0.664 | False |
| 2026-10-25 00:31 | 5000 | -7.86 | 0.647 | -1.79 | 0.664 | False |
| 2026-10-25 04:12 | 5000 | -7.86 | 0.647 | -3.91 | 0.502 | False |
| 2026-10-25 08:13 | 5000 | -9.34 | 0.581 | -4.08 | 0.492 | False |
| 2026-10-25 12:14 | 5000 | -11.7 | 0.478 | -4.18 | 0.485 | False |
| 2026-10-25 16:10 | 5000 | -11.03 | 0.494 | -2.25 | 0.61 | False |
| 2026-10-25 20:09 | 5000 | -11.23 | 0.489 | -3.98 | 0.498 | False |
| 2026-10-26 00:30 | 5000 | -10.98 | 0.497 | -4.45 | 0.47 | False |
| 2026-10-26 04:14 | 5000 | -11.01 | 0.497 | -2.91 | 0.55 | False |
| 2026-10-26 08:21 | 5000 | -11.71 | 0.481 | -5.03 | 0.44 | False |

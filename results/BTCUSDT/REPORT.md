# Finetune report -- BTCUSDT 15m

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
  "atr_mult": 3.0,
  "chand_len": 18,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-12.33%**, PF 0.474, 73 trades, max DD -1233.32
- Optimizer out-of-sample: net **-4.24%**, PF 0.468, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-28 00:22 | 5000 | -11.52 | 0.489 | -3.14 | 0.542 | False |
| 2026-10-28 04:10 | 5000 | -11.52 | 0.489 | -3.14 | 0.542 | False |
| 2026-10-28 08:11 | 5000 | -11.52 | 0.489 | -3.14 | 0.542 | False |
| 2026-10-28 12:12 | 5000 | -11.52 | 0.489 | -3.13 | 0.543 | False |
| 2026-10-28 16:09 | 5000 | -11.55 | 0.489 | -2.85 | 0.57 | False |
| 2026-10-28 20:09 | 5000 | -11.87 | 0.483 | -3.19 | 0.541 | False |
| 2026-10-29 00:22 | 5000 | -12.78 | 0.463 | -3.86 | 0.491 | False |
| 2026-10-29 04:10 | 5000 | -12.51 | 0.47 | -3.89 | 0.491 | False |
| 2026-10-29 08:11 | 5000 | -12.81 | 0.463 | -4.24 | 0.468 | False |
| 2026-10-29 12:13 | 5000 | -12.33 | 0.474 | -4.24 | 0.468 | False |

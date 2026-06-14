# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-06-14 12:44_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.3,
  "use_adx": true,
  "adx_len": 14,
  "adx_thresh": 20.0,
  "don_len": 20,
  "atr_len": 14,
  "atr_mult": 3.0,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-14.88%**, PF 0.403, 83 trades, max DD -1488.22
- Optimizer out-of-sample: net **-2.79%**, PF 0.591, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-13 00:57 | 5000 | -16.55 | 0.374 | -5.64 | 0.428 | False |
| 2026-06-13 05:35 | 5000 | -16.4 | 0.376 | -6.03 | 0.411 | False |
| 2026-06-13 09:08 | 5000 | -16.48 | 0.375 | -4.13 | 0.491 | False |
| 2026-06-13 12:41 | 5000 | -15.96 | 0.384 | -3.44 | 0.538 | False |
| 2026-06-13 16:34 | 5000 | -16.46 | 0.375 | -4.76 | 0.472 | False |
| 2026-06-13 20:32 | 5000 | -16.45 | 0.375 | -4.76 | 0.472 | False |
| 2026-06-14 00:57 | 5000 | -15.52 | 0.392 | -4.69 | 0.476 | False |
| 2026-06-14 05:38 | 5000 | -15.63 | 0.39 | -2.79 | 0.591 | False |
| 2026-06-14 09:10 | 5000 | -14.9 | 0.403 | -5.42 | 0.438 | False |
| 2026-06-14 12:44 | 5000 | -14.88 | 0.403 | -2.79 | 0.591 | False |

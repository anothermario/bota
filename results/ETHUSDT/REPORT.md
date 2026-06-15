# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-06-15 10:12_

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

- Current-params net profit (full sample): **-15.49%**, PF 0.395, 85 trades, max DD -1549.18
- Optimizer out-of-sample: net **-2.74%**, PF 0.629, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-13 20:32 | 5000 | -16.45 | 0.375 | -4.76 | 0.472 | False |
| 2026-06-14 00:57 | 5000 | -15.52 | 0.392 | -4.69 | 0.476 | False |
| 2026-06-14 05:38 | 5000 | -15.63 | 0.39 | -2.79 | 0.591 | False |
| 2026-06-14 09:10 | 5000 | -14.9 | 0.403 | -5.42 | 0.438 | False |
| 2026-06-14 12:44 | 5000 | -14.88 | 0.403 | -2.79 | 0.591 | False |
| 2026-06-14 16:35 | 5000 | -15.64 | 0.391 | -3.55 | 0.532 | False |
| 2026-06-14 20:32 | 5000 | -15.64 | 0.391 | -3.54 | 0.533 | False |
| 2026-06-15 00:59 | 5000 | -15.93 | 0.387 | -3.36 | 0.548 | False |
| 2026-06-15 05:52 | 5000 | -16.18 | 0.383 | -3.36 | 0.548 | False |
| 2026-06-15 10:12 | 5000 | -15.49 | 0.395 | -2.74 | 0.629 | False |

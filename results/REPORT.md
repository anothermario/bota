# Finetune report — BTCUSDT 4h

_Last run (UTC): 2026-06-07 09:06_

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

- Current-params net profit (full sample): **-9.88%**, PF 0.351, 35 trades, max DD -988.21
- Optimizer out-of-sample: net **-5.06%**, PF 0.006, 9 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-05 20:39 | 1500 | -8.64 | 0.419 | -5.34 | 0.006 | False |
| 2026-06-06 00:51 | 1500 | -8.56 | 0.426 | -5.34 | 0.006 | False |
| 2026-06-06 05:21 | 1500 | -8.91 | 0.398 | -5.34 | 0.006 | False |
| 2026-06-06 08:57 | 1500 | -9.27 | 0.37 | -5.34 | 0.006 | False |
| 2026-06-06 12:32 | 1500 | -9.23 | 0.374 | -5.34 | 0.006 | False |
| 2026-06-06 16:27 | 1500 | -9.3 | 0.368 | -5.33 | 0.006 | False |
| 2026-06-06 20:28 | 1500 | -9.33 | 0.366 | -5.34 | 0.006 | False |
| 2026-06-07 00:55 | 1500 | -9.34 | 0.366 | -5.5 | 0.005 | False |
| 2026-06-07 05:35 | 1500 | -9.34 | 0.365 | -5.06 | 0.006 | False |
| 2026-06-07 09:06 | 1500 | -9.88 | 0.351 | -5.06 | 0.006 | False |

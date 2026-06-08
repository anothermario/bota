# Finetune report — BTCUSDT 4h

_Last run (UTC): 2026-06-08 20:55_

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

- Current-params net profit (full sample): **-5.94%**, PF 0.604, 35 trades, max DD -940.92
- Optimizer out-of-sample: net **-0.76%**, PF 0.847, 9 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-07 09:06 | 1500 | -9.88 | 0.351 | -5.06 | 0.006 | False |
| 2026-06-07 12:37 | 1500 | -9.86 | 0.351 | -5.06 | 0.006 | False |
| 2026-06-07 16:33 | 1500 | -9.88 | 0.351 | -5.06 | 0.006 | False |
| 2026-06-07 20:30 | 1500 | -9.89 | 0.35 | -5.06 | 0.006 | False |
| 2026-06-08 00:56 | 1500 | -6.54 | 0.579 | -1.53 | 0.716 | False |
| 2026-06-08 05:39 | 1500 | -6.49 | 0.581 | -1.53 | 0.716 | False |
| 2026-06-08 09:40 | 1500 | -6.52 | 0.58 | -1.53 | 0.716 | False |
| 2026-06-08 13:32 | 1500 | -6.51 | 0.58 | -1.53 | 0.716 | False |
| 2026-06-08 17:10 | 1500 | -6.51 | 0.58 | -0.76 | 0.847 | False |
| 2026-06-08 20:55 | 1500 | -5.94 | 0.604 | -0.76 | 0.847 | False |

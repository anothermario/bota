# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-14 13:40_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.25,
  "use_adx": true,
  "adx_len": 14,
  "adx_thresh": 20.0,
  "don_len": 15,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-16.43%**, PF 0.507, 97 trades, max DD -1645.42
- Optimizer out-of-sample: net **-9.07%**, PF 0.231, 35 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-13 02:40 | 5000 | -13.04 | 0.612 | -7.64 | 0.262 | False |
| 2026-07-13 06:52 | 5000 | -12.67 | 0.62 | -7.64 | 0.262 | False |
| 2026-07-13 11:09 | 5000 | -12.67 | 0.62 | -7.64 | 0.262 | False |
| 2026-07-13 14:32 | 5000 | -12.7 | 0.62 | -7.1 | 0.367 | False |
| 2026-07-13 17:54 | 5000 | -14.45 | 0.564 | -8.22 | 0.248 | False |
| 2026-07-13 20:56 | 5000 | -15.18 | 0.552 | -9.42 | 0.222 | False |
| 2026-07-14 02:24 | 5000 | -15.18 | 0.552 | -8.98 | 0.232 | False |
| 2026-07-14 06:10 | 5000 | -15.07 | 0.554 | -8.98 | 0.232 | False |
| 2026-07-14 09:57 | 5000 | -15.07 | 0.554 | -7.18 | 0.273 | False |
| 2026-07-14 13:40 | 5000 | -16.43 | 0.507 | -9.07 | 0.231 | False |

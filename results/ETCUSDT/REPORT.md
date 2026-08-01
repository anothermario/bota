# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-01 16:58_

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
  "chand_len": 18,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-10.96%**, PF 0.577, 63 trades, max DD -1544.57
- Optimizer out-of-sample: net **-5.27%**, PF 0.449, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-31 06:42 | 5000 | -11.53 | 0.561 | -8.27 | 0.347 | False |
| 2026-07-31 10:37 | 5000 | -11.53 | 0.561 | -7.56 | 0.369 | False |
| 2026-07-31 14:03 | 5000 | -11.53 | 0.561 | -7.56 | 0.369 | False |
| 2026-07-31 17:27 | 5000 | -11.53 | 0.561 | -7.56 | 0.369 | False |
| 2026-07-31 21:02 | 5000 | -11.53 | 0.561 | -6.9 | 0.392 | False |
| 2026-08-01 02:41 | 5000 | -11.57 | 0.56 | -7.0 | 0.39 | False |
| 2026-08-01 06:28 | 5000 | -11.32 | 0.569 | -6.29 | 0.428 | False |
| 2026-08-01 09:58 | 5000 | -11.32 | 0.569 | -5.99 | 0.441 | False |
| 2026-08-01 13:17 | 5000 | -10.63 | 0.586 | -5.14 | 0.484 | False |
| 2026-08-01 16:58 | 5000 | -10.96 | 0.577 | -5.27 | 0.449 | False |

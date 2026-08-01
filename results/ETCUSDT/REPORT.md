# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-01 02:41_

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

- Current-params net profit (full sample): **-11.57%**, PF 0.56, 63 trades, max DD -1538.29
- Optimizer out-of-sample: net **-7.0%**, PF 0.39, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-30 13:57 | 5000 | -10.63 | 0.599 | -7.51 | 0.353 | False |
| 2026-07-30 17:25 | 5000 | -11.02 | 0.583 | -6.64 | 0.384 | False |
| 2026-07-30 21:08 | 5000 | -11.85 | 0.553 | -6.66 | 0.384 | False |
| 2026-07-31 02:42 | 5000 | -11.53 | 0.561 | -6.9 | 0.392 | False |
| 2026-07-31 06:42 | 5000 | -11.53 | 0.561 | -8.27 | 0.347 | False |
| 2026-07-31 10:37 | 5000 | -11.53 | 0.561 | -7.56 | 0.369 | False |
| 2026-07-31 14:03 | 5000 | -11.53 | 0.561 | -7.56 | 0.369 | False |
| 2026-07-31 17:27 | 5000 | -11.53 | 0.561 | -7.56 | 0.369 | False |
| 2026-07-31 21:02 | 5000 | -11.53 | 0.561 | -6.9 | 0.392 | False |
| 2026-08-01 02:41 | 5000 | -11.57 | 0.56 | -7.0 | 0.39 | False |

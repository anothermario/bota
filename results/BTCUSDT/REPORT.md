# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-07 08:26_

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

- Current-params net profit (full sample): **-14.18%**, PF 0.408, 72 trades, max DD -1451.9
- Optimizer out-of-sample: net **-5.75%**, PF 0.315, 31 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-05 16:34 | 5000 | -15.09 | 0.404 | -5.36 | 0.328 | False |
| 2026-08-05 20:31 | 5000 | -15.9 | 0.375 | -6.01 | 0.303 | False |
| 2026-08-06 00:31 | 5000 | -15.9 | 0.375 | -5.94 | 0.306 | False |
| 2026-08-06 05:05 | 5000 | -15.87 | 0.375 | -5.67 | 0.316 | False |
| 2026-08-06 08:58 | 5000 | -15.6 | 0.38 | -5.1 | 0.343 | False |
| 2026-08-06 12:41 | 5000 | -14.79 | 0.396 | -5.51 | 0.325 | False |
| 2026-08-06 21:58 | 5000 | -14.69 | 0.398 | -5.5 | 0.325 | False |
| 2026-08-07 01:16 | 5000 | -14.73 | 0.398 | -5.54 | 0.325 | False |
| 2026-08-07 04:40 | 5000 | -14.19 | 0.408 | -5.75 | 0.315 | False |
| 2026-08-07 08:26 | 5000 | -14.18 | 0.408 | -5.75 | 0.315 | False |

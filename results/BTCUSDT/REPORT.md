# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-06 08:58_

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

- Current-params net profit (full sample): **-15.6%**, PF 0.38, 73 trades, max DD -1632.53
- Optimizer out-of-sample: net **-5.1%**, PF 0.343, 29 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-04 20:32 | 5000 | -15.27 | 0.417 | -4.83 | 0.401 | False |
| 2026-08-05 00:34 | 5000 | -15.26 | 0.418 | -5.68 | 0.359 | False |
| 2026-08-05 05:05 | 5000 | -14.81 | 0.426 | -4.79 | 0.402 | False |
| 2026-08-05 08:58 | 5000 | -14.81 | 0.426 | -4.79 | 0.402 | False |
| 2026-08-05 12:38 | 5000 | -14.6 | 0.43 | -4.79 | 0.402 | False |
| 2026-08-05 16:34 | 5000 | -15.09 | 0.404 | -5.36 | 0.328 | False |
| 2026-08-05 20:31 | 5000 | -15.9 | 0.375 | -6.01 | 0.303 | False |
| 2026-08-06 00:31 | 5000 | -15.9 | 0.375 | -5.94 | 0.306 | False |
| 2026-08-06 05:05 | 5000 | -15.87 | 0.375 | -5.67 | 0.316 | False |
| 2026-08-06 08:58 | 5000 | -15.6 | 0.38 | -5.1 | 0.343 | False |

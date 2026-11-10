# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-11-10 00:18_

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

- Current-params net profit (full sample): **-18.34%**, PF 0.32, 78 trades, max DD -1919.2
- Optimizer out-of-sample: net **-8.26%**, PF 0.2, 27 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-08 12:09 | 5000 | -15.17 | 0.411 | -10.68 | 0.058 | False |
| 2026-11-08 16:07 | 5000 | -15.66 | 0.402 | -10.67 | 0.058 | False |
| 2026-11-08 20:06 | 5000 | -15.17 | 0.411 | -10.5 | 0.059 | False |
| 2026-11-09 00:21 | 5000 | -16.02 | 0.382 | -10.94 | 0.057 | False |
| 2026-11-09 04:09 | 5000 | -16.16 | 0.376 | -10.7 | 0.058 | False |
| 2026-11-09 08:11 | 5000 | -16.13 | 0.377 | -10.72 | 0.059 | False |
| 2026-11-09 12:11 | 5000 | -17.5 | 0.33 | -11.17 | 0.056 | False |
| 2026-11-09 16:08 | 5000 | -17.53 | 0.33 | -11.17 | 0.056 | False |
| 2026-11-09 20:07 | 5000 | -18.34 | 0.32 | -11.66 | 0.054 | False |
| 2026-11-10 00:18 | 5000 | -18.34 | 0.32 | -8.26 | 0.2 | False |

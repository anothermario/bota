# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-11-09 04:09_

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

- Current-params net profit (full sample): **-16.16%**, PF 0.376, 78 trades, max DD -1794.7
- Optimizer out-of-sample: net **-10.7%**, PF 0.058, 32 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-07 16:07 | 5000 | -15.17 | 0.411 | -11.08 | 0.056 | False |
| 2026-11-07 20:06 | 5000 | -15.17 | 0.411 | -11.08 | 0.056 | False |
| 2026-11-08 00:21 | 5000 | -15.17 | 0.411 | -11.08 | 0.056 | False |
| 2026-11-08 04:08 | 5000 | -15.17 | 0.411 | -11.11 | 0.056 | False |
| 2026-11-08 08:08 | 5000 | -15.17 | 0.411 | -10.74 | 0.058 | False |
| 2026-11-08 12:09 | 5000 | -15.17 | 0.411 | -10.68 | 0.058 | False |
| 2026-11-08 16:07 | 5000 | -15.66 | 0.402 | -10.67 | 0.058 | False |
| 2026-11-08 20:06 | 5000 | -15.17 | 0.411 | -10.5 | 0.059 | False |
| 2026-11-09 00:21 | 5000 | -16.02 | 0.382 | -10.94 | 0.057 | False |
| 2026-11-09 04:09 | 5000 | -16.16 | 0.376 | -10.7 | 0.058 | False |

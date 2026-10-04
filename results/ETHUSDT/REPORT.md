# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-04 20:47_

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

- Current-params net profit (full sample): **-14.68%**, PF 0.496, 97 trades, max DD -1502.35
- Optimizer out-of-sample: net **-5.99%**, PF 0.213, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-03 08:15 | 5000 | -15.71 | 0.469 | -3.74 | 0.577 | False |
| 2026-10-03 13:44 | 5000 | -15.33 | 0.476 | -2.41 | 0.757 | False |
| 2026-10-03 17:22 | 5000 | -15.1 | 0.48 | -3.64 | 0.626 | False |
| 2026-10-03 21:01 | 5000 | -15.1 | 0.48 | -5.44 | 0.44 | False |
| 2026-10-04 01:10 | 5000 | -15.09 | 0.48 | -6.03 | 0.211 | False |
| 2026-10-04 05:30 | 5000 | -14.96 | 0.483 | -6.41 | 0.32 | False |
| 2026-10-04 10:10 | 5000 | -13.98 | 0.509 | -5.96 | 0.368 | False |
| 2026-10-04 13:58 | 5000 | -14.33 | 0.503 | -6.31 | 0.353 | False |
| 2026-10-04 17:28 | 5000 | -14.67 | 0.496 | -5.99 | 0.213 | False |
| 2026-10-04 20:47 | 5000 | -14.68 | 0.496 | -5.99 | 0.213 | False |

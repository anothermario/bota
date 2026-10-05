# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-05 08:24_

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

- Current-params net profit (full sample): **-14.86%**, PF 0.494, 98 trades, max DD -1485.64
- Optimizer out-of-sample: net **-5.53%**, PF 0.29, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-03 21:01 | 5000 | -15.1 | 0.48 | -5.44 | 0.44 | False |
| 2026-10-04 01:10 | 5000 | -15.09 | 0.48 | -6.03 | 0.211 | False |
| 2026-10-04 05:30 | 5000 | -14.96 | 0.483 | -6.41 | 0.32 | False |
| 2026-10-04 10:10 | 5000 | -13.98 | 0.509 | -5.96 | 0.368 | False |
| 2026-10-04 13:58 | 5000 | -14.33 | 0.503 | -6.31 | 0.353 | False |
| 2026-10-04 17:28 | 5000 | -14.67 | 0.496 | -5.99 | 0.213 | False |
| 2026-10-04 20:47 | 5000 | -14.68 | 0.496 | -5.99 | 0.213 | False |
| 2026-10-05 00:36 | 5000 | -14.7 | 0.496 | -4.8 | 0.38 | False |
| 2026-10-05 04:19 | 5000 | -15.08 | 0.489 | -4.93 | 0.368 | False |
| 2026-10-05 08:24 | 5000 | -14.86 | 0.494 | -5.53 | 0.29 | False |

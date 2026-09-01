# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-01 00:37_

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

- Current-params net profit (full sample): **-19.19%**, PF 0.32, 100 trades, max DD -1954.15
- Optimizer out-of-sample: net **-7.13%**, PF 0.129, 30 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-30 12:15 | 5000 | -18.55 | 0.335 | -5.62 | 0.06 | False |
| 2026-08-30 16:10 | 5000 | -18.6 | 0.335 | -5.39 | 0.063 | False |
| 2026-08-30 20:10 | 5000 | -18.75 | 0.335 | -5.54 | 0.064 | False |
| 2026-08-31 00:34 | 5000 | -19.66 | 0.299 | -6.34 | 0.143 | False |
| 2026-08-31 04:14 | 5000 | -18.99 | 0.322 | -6.45 | 0.141 | False |
| 2026-08-31 08:18 | 5000 | -19.48 | 0.315 | -6.45 | 0.141 | False |
| 2026-08-31 12:18 | 5000 | -18.88 | 0.324 | -6.45 | 0.141 | False |
| 2026-08-31 16:12 | 5000 | -18.9 | 0.324 | -6.45 | 0.141 | False |
| 2026-08-31 20:11 | 5000 | -18.9 | 0.324 | -6.48 | 0.141 | False |
| 2026-09-01 00:37 | 5000 | -19.19 | 0.32 | -7.13 | 0.129 | False |

# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-20 16:13_

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
  "chand_len": 26,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-14.7%**, PF 0.453, 66 trades, max DD -1569.1
- Optimizer out-of-sample: net **-6.45%**, PF 0.322, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-19 04:13 | 5000 | -14.57 | 0.45 | -5.61 | 0.35 | False |
| 2026-10-19 08:19 | 5000 | -14.6 | 0.45 | -5.64 | 0.35 | False |
| 2026-10-19 12:18 | 5000 | -14.28 | 0.458 | -6.3 | 0.324 | False |
| 2026-10-19 16:13 | 5000 | -14.28 | 0.458 | -6.3 | 0.324 | False |
| 2026-10-19 20:12 | 5000 | -14.28 | 0.458 | -6.29 | 0.324 | False |
| 2026-10-20 00:29 | 5000 | -14.28 | 0.458 | -5.64 | 0.35 | False |
| 2026-10-20 04:13 | 5000 | -14.28 | 0.458 | -5.64 | 0.35 | False |
| 2026-10-20 08:15 | 5000 | -14.28 | 0.458 | -5.79 | 0.344 | False |
| 2026-10-20 12:17 | 5000 | -13.44 | 0.476 | -5.08 | 0.377 | False |
| 2026-10-20 16:13 | 5000 | -14.7 | 0.453 | -6.45 | 0.322 | False |

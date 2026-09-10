# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-10 04:13_

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

- Current-params net profit (full sample): **-1.47%**, PF 0.926, 52 trades, max DD -640.17
- Optimizer out-of-sample: net **-3.86%**, PF 0.413, 15 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-08 16:13 | 5000 | -2.88 | 0.86 | -4.94 | 0.377 | False |
| 2026-09-08 20:11 | 5000 | -3.07 | 0.852 | -5.29 | 0.361 | False |
| 2026-09-09 00:31 | 5000 | -3.07 | 0.852 | -4.37 | 0.408 | False |
| 2026-09-09 04:13 | 5000 | -2.51 | 0.88 | -4.5 | 0.374 | False |
| 2026-09-09 08:16 | 5000 | -3.08 | 0.852 | -5.1 | 0.346 | False |
| 2026-09-09 12:17 | 5000 | -3.08 | 0.852 | -3.84 | 0.415 | False |
| 2026-09-09 16:12 | 5000 | -2.22 | 0.89 | -3.84 | 0.415 | False |
| 2026-09-09 20:11 | 5000 | -1.92 | 0.904 | -3.84 | 0.415 | False |
| 2026-09-10 00:29 | 5000 | -1.92 | 0.904 | -3.84 | 0.415 | False |
| 2026-09-10 04:13 | 5000 | -1.47 | 0.926 | -3.86 | 0.413 | False |

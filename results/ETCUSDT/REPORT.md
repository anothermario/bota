# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-09 04:13_

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

- Current-params net profit (full sample): **-2.51%**, PF 0.88, 54 trades, max DD -636.29
- Optimizer out-of-sample: net **-4.5%**, PF 0.374, 16 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-07 16:12 | 5000 | -2.86 | 0.86 | -4.3 | 0.385 | False |
| 2026-09-07 20:11 | 5000 | -2.86 | 0.86 | -4.3 | 0.385 | False |
| 2026-09-08 00:31 | 5000 | -2.86 | 0.86 | -5.24 | 0.337 | False |
| 2026-09-08 04:13 | 5000 | -2.86 | 0.86 | -5.21 | 0.339 | False |
| 2026-09-08 08:16 | 5000 | -2.86 | 0.86 | -4.3 | 0.385 | False |
| 2026-09-08 12:17 | 5000 | -2.86 | 0.86 | -4.3 | 0.385 | False |
| 2026-09-08 16:13 | 5000 | -2.88 | 0.86 | -4.94 | 0.377 | False |
| 2026-09-08 20:11 | 5000 | -3.07 | 0.852 | -5.29 | 0.361 | False |
| 2026-09-09 00:31 | 5000 | -3.07 | 0.852 | -4.37 | 0.408 | False |
| 2026-09-09 04:13 | 5000 | -2.51 | 0.88 | -4.5 | 0.374 | False |

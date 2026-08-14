# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-08-14 00:26_

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

- Current-params net profit (full sample): **-20.68%**, PF 0.379, 104 trades, max DD -2218.29
- Optimizer out-of-sample: net **-5.03%**, PF 0.31, 27 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-12 12:19 | 5000 | -21.52 | 0.356 | -4.67 | 0.294 | False |
| 2026-08-12 16:20 | 5000 | -20.29 | 0.385 | -4.32 | 0.342 | False |
| 2026-08-12 20:15 | 5000 | -19.72 | 0.394 | -4.36 | 0.342 | False |
| 2026-08-13 00:25 | 5000 | -19.72 | 0.394 | -4.35 | 0.342 | False |
| 2026-08-13 04:38 | 5000 | -19.88 | 0.392 | -4.03 | 0.358 | False |
| 2026-08-13 08:33 | 5000 | -20.5 | 0.38 | -3.46 | 0.391 | False |
| 2026-08-13 12:19 | 5000 | -20.18 | 0.386 | -4.53 | 0.334 | False |
| 2026-08-13 16:20 | 5000 | -20.67 | 0.38 | -5.03 | 0.31 | False |
| 2026-08-13 20:13 | 5000 | -20.67 | 0.38 | -5.03 | 0.31 | False |
| 2026-08-14 00:26 | 5000 | -20.68 | 0.379 | -5.03 | 0.31 | False |

# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-08-22 04:13_

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

- Current-params net profit (full sample): **-19.07%**, PF 0.372, 106 trades, max DD -2121.07
- Optimizer out-of-sample: net **-5.06%**, PF 0.346, 32 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-20 16:09 | 5000 | -19.61 | 0.37 | -5.14 | 0.231 | False |
| 2026-08-20 20:08 | 5000 | -19.58 | 0.371 | -5.18 | 0.229 | False |
| 2026-08-21 00:15 | 5000 | -19.85 | 0.36 | -4.5 | 0.257 | False |
| 2026-08-21 04:16 | 5000 | -19.84 | 0.361 | -4.12 | 0.275 | False |
| 2026-08-21 08:14 | 5000 | -19.88 | 0.36 | -4.12 | 0.275 | False |
| 2026-08-21 12:10 | 5000 | -19.67 | 0.363 | -5.71 | 0.317 | False |
| 2026-08-21 16:09 | 5000 | -20.16 | 0.356 | -4.45 | 0.259 | False |
| 2026-08-21 20:06 | 5000 | -19.82 | 0.361 | -4.45 | 0.259 | False |
| 2026-08-22 00:14 | 5000 | -19.68 | 0.363 | -5.06 | 0.346 | False |
| 2026-08-22 04:13 | 5000 | -19.07 | 0.372 | -5.06 | 0.346 | False |

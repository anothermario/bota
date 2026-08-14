# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-08-14 20:11_

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

- Current-params net profit (full sample): **-21.24%**, PF 0.364, 102 trades, max DD -2228.48
- Optimizer out-of-sample: net **-5.17%**, PF 0.304, 28 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-13 08:33 | 5000 | -20.5 | 0.38 | -3.46 | 0.391 | False |
| 2026-08-13 12:19 | 5000 | -20.18 | 0.386 | -4.53 | 0.334 | False |
| 2026-08-13 16:20 | 5000 | -20.67 | 0.38 | -5.03 | 0.31 | False |
| 2026-08-13 20:13 | 5000 | -20.67 | 0.38 | -5.03 | 0.31 | False |
| 2026-08-14 00:26 | 5000 | -20.68 | 0.379 | -5.03 | 0.31 | False |
| 2026-08-14 04:36 | 5000 | -21.37 | 0.362 | -6.65 | 0.222 | False |
| 2026-08-14 08:30 | 5000 | -21.56 | 0.36 | -5.07 | 0.309 | False |
| 2026-08-14 12:18 | 5000 | -21.73 | 0.358 | -5.18 | 0.303 | False |
| 2026-08-14 16:18 | 5000 | -21.7 | 0.358 | -5.2 | 0.302 | False |
| 2026-08-14 20:11 | 5000 | -21.24 | 0.364 | -5.17 | 0.304 | False |

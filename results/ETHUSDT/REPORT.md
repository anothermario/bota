# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-08-11 08:23_

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

- Current-params net profit (full sample): **-20.78%**, PF 0.363, 101 trades, max DD -2177.57
- Optimizer out-of-sample: net **-5.35%**, PF 0.278, 27 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-09 20:09 | 5000 | -22.24 | 0.329 | -4.57 | 0.365 | False |
| 2026-08-10 00:21 | 5000 | -22.1 | 0.332 | -5.65 | 0.293 | False |
| 2026-08-10 04:33 | 5000 | -22.1 | 0.332 | -5.37 | 0.305 | False |
| 2026-08-10 08:34 | 5000 | -22.1 | 0.332 | -5.36 | 0.305 | False |
| 2026-08-10 12:18 | 5000 | -22.1 | 0.332 | -5.36 | 0.305 | False |
| 2026-08-10 16:18 | 5000 | -22.13 | 0.332 | -5.18 | 0.315 | False |
| 2026-08-10 20:15 | 5000 | -22.12 | 0.332 | -5.18 | 0.315 | False |
| 2026-08-11 00:20 | 5000 | -22.12 | 0.332 | -4.77 | 0.36 | False |
| 2026-08-11 04:31 | 5000 | -20.8 | 0.363 | -4.93 | 0.337 | False |
| 2026-08-11 08:23 | 5000 | -20.78 | 0.363 | -5.35 | 0.278 | False |

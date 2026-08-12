# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-08-12 04:36_

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

- Current-params net profit (full sample): **-21.85%**, PF 0.352, 104 trades, max DD -2185.01
- Optimizer out-of-sample: net **-3.57%**, PF 0.462, 25 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-10 16:18 | 5000 | -22.13 | 0.332 | -5.18 | 0.315 | False |
| 2026-08-10 20:15 | 5000 | -22.12 | 0.332 | -5.18 | 0.315 | False |
| 2026-08-11 00:20 | 5000 | -22.12 | 0.332 | -4.77 | 0.36 | False |
| 2026-08-11 04:31 | 5000 | -20.8 | 0.363 | -4.93 | 0.337 | False |
| 2026-08-11 08:23 | 5000 | -20.78 | 0.363 | -5.35 | 0.278 | False |
| 2026-08-11 12:18 | 5000 | -20.06 | 0.374 | -5.38 | 0.278 | False |
| 2026-08-11 16:19 | 5000 | -20.61 | 0.367 | -5.48 | 0.275 | False |
| 2026-08-11 20:15 | 5000 | -20.59 | 0.369 | -5.92 | 0.259 | False |
| 2026-08-12 00:24 | 5000 | -21.21 | 0.36 | -5.08 | 0.301 | False |
| 2026-08-12 04:36 | 5000 | -21.85 | 0.352 | -3.57 | 0.462 | False |

# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-21 00:15_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.3,
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

- Current-params net profit (full sample): **-11.98%**, PF 0.473, 60 trades, max DD -1366.68
- Optimizer out-of-sample: net **-0.98%**, PF 0.768, 16 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-19 12:09 | 5000 | -13.08 | 0.423 | -1.67 | 0.579 | False |
| 2026-08-19 16:08 | 5000 | -12.72 | 0.44 | -1.74 | 0.572 | False |
| 2026-08-19 20:06 | 5000 | -13.37 | 0.427 | -2.47 | 0.482 | False |
| 2026-08-20 00:14 | 5000 | -13.29 | 0.431 | -2.38 | 0.501 | False |
| 2026-08-20 04:15 | 5000 | -13.29 | 0.431 | -2.38 | 0.501 | False |
| 2026-08-20 08:13 | 5000 | -13.29 | 0.431 | -3.14 | 0.43 | False |
| 2026-08-20 12:10 | 5000 | -13.31 | 0.431 | -2.39 | 0.502 | False |
| 2026-08-20 16:09 | 5000 | -12.64 | 0.445 | -1.84 | 0.569 | False |
| 2026-08-20 20:08 | 5000 | -11.85 | 0.479 | -0.98 | 0.768 | False |
| 2026-08-21 00:15 | 5000 | -11.98 | 0.473 | -0.98 | 0.768 | False |

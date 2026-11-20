# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-11-20 00:17_

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

- Current-params net profit (full sample): **-10.83%**, PF 0.531, 75 trades, max DD -1205.83
- Optimizer out-of-sample: net **-4.36%**, PF 0.543, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-18 12:10 | 5000 | -11.21 | 0.517 | -2.71 | 0.711 | False |
| 2026-11-18 16:07 | 5000 | -11.23 | 0.517 | -2.73 | 0.711 | False |
| 2026-11-18 20:07 | 5000 | -11.47 | 0.512 | -3.84 | 0.619 | False |
| 2026-11-19 00:19 | 5000 | -11.47 | 0.512 | -3.35 | 0.651 | False |
| 2026-11-19 04:08 | 5000 | -11.47 | 0.512 | -3.41 | 0.645 | False |
| 2026-11-19 08:10 | 5000 | -10.81 | 0.528 | -3.97 | 0.588 | False |
| 2026-11-19 12:10 | 5000 | -10.81 | 0.528 | -3.89 | 0.593 | False |
| 2026-11-19 16:08 | 5000 | -10.82 | 0.529 | -4.45 | 0.56 | False |
| 2026-11-19 20:07 | 5000 | -10.83 | 0.531 | -4.2 | 0.576 | False |
| 2026-11-20 00:17 | 5000 | -10.83 | 0.531 | -4.36 | 0.543 | False |

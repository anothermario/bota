# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-20 20:10_

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

- Current-params net profit (full sample): **-12.23%**, PF 0.547, 100 trades, max DD -1662.89
- Optimizer out-of-sample: net **-7.65%**, PF 0.404, 37 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-19 08:13 | 5000 | -12.46 | 0.54 | -3.64 | 0.673 | False |
| 2026-09-19 12:15 | 5000 | -12.49 | 0.54 | -3.65 | 0.674 | False |
| 2026-09-19 16:10 | 5000 | -12.69 | 0.536 | -7.45 | 0.396 | False |
| 2026-09-19 20:10 | 5000 | -13.07 | 0.527 | -7.53 | 0.38 | False |
| 2026-09-20 00:34 | 5000 | -12.4 | 0.542 | -7.53 | 0.38 | False |
| 2026-09-20 04:13 | 5000 | -12.42 | 0.543 | -7.88 | 0.37 | False |
| 2026-09-20 08:14 | 5000 | -12.7 | 0.536 | -7.88 | 0.37 | False |
| 2026-09-20 12:15 | 5000 | -12.2 | 0.548 | -8.46 | 0.352 | False |
| 2026-09-20 16:11 | 5000 | -12.23 | 0.547 | -7.94 | 0.38 | False |
| 2026-09-20 20:10 | 5000 | -12.23 | 0.547 | -7.65 | 0.404 | False |

# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-11-13 00:19_

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

- Current-params net profit (full sample): **-14.46%**, PF 0.384, 75 trades, max DD -1496.06
- Optimizer out-of-sample: net **-6.57%**, PF 0.184, 25 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-11 12:11 | 5000 | -13.82 | 0.41 | -6.81 | 0.138 | False |
| 2026-11-11 16:07 | 5000 | -13.82 | 0.41 | -5.96 | 0.156 | False |
| 2026-11-11 20:07 | 5000 | -13.41 | 0.418 | -5.98 | 0.156 | False |
| 2026-11-12 00:19 | 5000 | -13.79 | 0.412 | -6.34 | 0.149 | False |
| 2026-11-12 04:08 | 5000 | -15.26 | 0.36 | -6.34 | 0.149 | False |
| 2026-11-12 08:10 | 5000 | -15.26 | 0.36 | -6.34 | 0.149 | False |
| 2026-11-12 12:11 | 5000 | -15.27 | 0.36 | -6.34 | 0.149 | False |
| 2026-11-12 16:08 | 5000 | -14.78 | 0.378 | -6.57 | 0.184 | False |
| 2026-11-12 20:07 | 5000 | -14.79 | 0.378 | -6.56 | 0.184 | False |
| 2026-11-13 00:19 | 5000 | -14.46 | 0.384 | -6.57 | 0.184 | False |

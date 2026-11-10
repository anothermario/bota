# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-11-10 00:18_

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

- Current-params net profit (full sample): **-13.16%**, PF 0.422, 75 trades, max DD -1369.84
- Optimizer out-of-sample: net **-5.24%**, PF 0.174, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-08 12:09 | 5000 | -8.17 | 0.65 | -5.54 | 0.17 | False |
| 2026-11-08 16:07 | 5000 | -7.89 | 0.662 | -5.63 | 0.167 | False |
| 2026-11-08 20:07 | 5000 | -7.28 | 0.681 | -5.26 | 0.177 | False |
| 2026-11-09 00:21 | 5000 | -9.62 | 0.57 | -5.07 | 0.183 | False |
| 2026-11-09 04:09 | 5000 | -10.46 | 0.529 | -4.7 | 0.196 | False |
| 2026-11-09 08:11 | 5000 | -11.1 | 0.497 | -5.06 | 0.185 | False |
| 2026-11-09 12:11 | 5000 | -12.67 | 0.431 | -5.12 | 0.183 | False |
| 2026-11-09 16:08 | 5000 | -12.65 | 0.432 | -5.11 | 0.177 | False |
| 2026-11-09 20:07 | 5000 | -13.16 | 0.422 | -5.24 | 0.174 | False |
| 2026-11-10 00:18 | 5000 | -13.16 | 0.422 | -5.24 | 0.174 | False |

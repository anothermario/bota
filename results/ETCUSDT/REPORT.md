# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-26 13:19_

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
  "chand_len": 18,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-7.89%**, PF 0.684, 62 trades, max DD -1546.9
- Optimizer out-of-sample: net **-5.34%**, PF 0.52, 25 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-25 02:33 | 5000 | -13.45 | 0.492 | -7.82 | 0.268 | False |
| 2026-07-25 06:17 | 5000 | -12.61 | 0.511 | -8.61 | 0.248 | False |
| 2026-07-25 09:46 | 5000 | -12.61 | 0.511 | -8.57 | 0.249 | False |
| 2026-07-25 13:23 | 5000 | -13.22 | 0.497 | -7.4 | 0.258 | False |
| 2026-07-25 16:55 | 5000 | -13.22 | 0.497 | -7.4 | 0.258 | False |
| 2026-07-25 20:51 | 5000 | -12.39 | 0.517 | -7.94 | 0.266 | False |
| 2026-07-26 02:40 | 5000 | -12.44 | 0.515 | -7.94 | 0.266 | False |
| 2026-07-26 06:35 | 5000 | -12.19 | 0.521 | -9.07 | 0.238 | False |
| 2026-07-26 09:58 | 5000 | -12.17 | 0.521 | -9.15 | 0.237 | False |
| 2026-07-26 13:19 | 5000 | -7.89 | 0.684 | -5.34 | 0.52 | False |

# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-07 21:23_

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

- Current-params net profit (full sample): **-14.04%**, PF 0.499, 76 trades, max DD -1404.23
- Optimizer out-of-sample: net **-6.59%**, PF 0.324, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-06 08:19 | 5000 | -11.28 | 0.59 | -3.93 | 0.524 | False |
| 2026-07-06 15:30 | 5000 | -11.83 | 0.576 | -6.72 | 0.303 | False |
| 2026-07-06 18:10 | 5000 | -11.8 | 0.577 | -6.72 | 0.303 | False |
| 2026-07-06 21:28 | 5000 | -11.46 | 0.591 | -6.72 | 0.303 | False |
| 2026-07-07 03:17 | 5000 | -13.02 | 0.528 | -6.72 | 0.303 | False |
| 2026-07-07 07:37 | 5000 | -13.11 | 0.524 | -6.75 | 0.303 | False |
| 2026-07-07 10:54 | 5000 | -13.01 | 0.528 | -6.75 | 0.303 | False |
| 2026-07-07 14:31 | 5000 | -13.36 | 0.513 | -6.75 | 0.303 | False |
| 2026-07-07 17:58 | 5000 | -13.65 | 0.507 | -6.89 | 0.298 | False |
| 2026-07-07 21:23 | 5000 | -14.04 | 0.499 | -6.59 | 0.324 | False |

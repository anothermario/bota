# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-07 07:37_

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

- Current-params net profit (full sample): **-13.11%**, PF 0.524, 76 trades, max DD -1356.51
- Optimizer out-of-sample: net **-6.75%**, PF 0.303, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-05 13:37 | 5000 | -12.36 | 0.561 | -6.24 | 0.318 | False |
| 2026-07-05 17:09 | 5000 | -11.77 | 0.574 | -6.24 | 0.318 | False |
| 2026-07-05 20:59 | 5000 | -11.78 | 0.574 | -6.24 | 0.318 | False |
| 2026-07-06 03:26 | 5000 | -11.27 | 0.589 | -4.71 | 0.474 | False |
| 2026-07-06 08:19 | 5000 | -11.28 | 0.59 | -3.93 | 0.524 | False |
| 2026-07-06 15:30 | 5000 | -11.83 | 0.576 | -6.72 | 0.303 | False |
| 2026-07-06 18:10 | 5000 | -11.8 | 0.577 | -6.72 | 0.303 | False |
| 2026-07-06 21:28 | 5000 | -11.46 | 0.591 | -6.72 | 0.303 | False |
| 2026-07-07 03:17 | 5000 | -13.02 | 0.528 | -6.72 | 0.303 | False |
| 2026-07-07 07:37 | 5000 | -13.11 | 0.524 | -6.75 | 0.303 | False |

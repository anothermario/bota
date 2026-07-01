# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-01 05:36_

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

- Current-params net profit (full sample): **-9.79%**, PF 0.665, 80 trades, max DD -1331.23
- Optimizer out-of-sample: net **-5.13%**, PF 0.443, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-29 17:04 | 5000 | -8.09 | 0.699 | 1.36 | 1.183 | True |
| 2026-06-29 20:40 | 5000 | -9.96 | 0.658 | 2.38 | 1.368 | True |
| 2026-06-30 00:52 | 5000 | -8.41 | 0.694 | 0.06 | 1.012 | True |
| 2026-06-30 05:27 | 5000 | -8.13 | 0.709 | -0.2 | 0.977 | False |
| 2026-06-30 09:11 | 5000 | -8.8 | 0.686 | -0.9 | 0.876 | False |
| 2026-06-30 12:46 | 5000 | -8.41 | 0.697 | -1.53 | 0.787 | False |
| 2026-06-30 16:47 | 5000 | -9.64 | 0.665 | -2.56 | 0.689 | False |
| 2026-06-30 20:42 | 5000 | -9.5 | 0.669 | -2.26 | 0.728 | False |
| 2026-07-01 00:54 | 5000 | -9.5 | 0.669 | -4.56 | 0.472 | False |
| 2026-07-01 05:36 | 5000 | -9.79 | 0.665 | -5.13 | 0.443 | False |

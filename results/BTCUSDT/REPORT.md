# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-06-18 05:39_

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
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-7.51%**, PF 0.643, 65 trades, max DD -878.62
- Optimizer out-of-sample: net **-3.54%**, PF 0.539, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-16 17:45 | 5000 | -7.49 | 0.641 | 2.23 | 1.336 | True |
| 2026-06-16 21:05 | 5000 | -8.07 | 0.623 | -0.07 | 0.991 | False |
| 2026-06-17 00:58 | 5000 | -7.75 | 0.633 | 0.6 | 1.081 | True |
| 2026-06-17 05:43 | 5000 | -7.37 | 0.646 | 0.6 | 1.082 | True |
| 2026-06-17 09:43 | 5000 | -7.16 | 0.654 | 0.57 | 1.083 | True |
| 2026-06-17 13:21 | 5000 | -7.41 | 0.646 | 0.54 | 1.078 | True |
| 2026-06-17 17:06 | 5000 | -7.28 | 0.651 | -0.09 | 0.993 | False |
| 2026-06-17 20:46 | 5000 | -7.51 | 0.643 | -1.09 | 0.863 | False |
| 2026-06-18 00:57 | 5000 | -7.51 | 0.643 | -2.11 | 0.732 | False |
| 2026-06-18 05:39 | 5000 | -7.51 | 0.643 | -3.54 | 0.539 | False |

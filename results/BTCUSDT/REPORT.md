# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-05 03:18_

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

- Current-params net profit (full sample): **-5.5%**, PF 0.758, 66 trades, max DD -853.61
- Optimizer out-of-sample: net **-2.85%**, PF 0.623, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-03 14:01 | 5000 | -3.96 | 0.824 | -2.88 | 0.606 | False |
| 2026-07-03 17:24 | 5000 | -4.21 | 0.813 | -3.14 | 0.582 | False |
| 2026-07-03 21:05 | 5000 | -4.25 | 0.813 | -3.18 | 0.582 | False |
| 2026-07-04 02:49 | 5000 | -4.51 | 0.803 | -3.07 | 0.589 | False |
| 2026-07-04 06:46 | 5000 | -4.97 | 0.781 | -3.07 | 0.589 | False |
| 2026-07-04 10:08 | 5000 | -6.54 | 0.719 | -3.07 | 0.589 | False |
| 2026-07-04 13:23 | 5000 | -5.71 | 0.747 | -3.07 | 0.589 | False |
| 2026-07-04 17:04 | 5000 | -5.75 | 0.747 | -3.1 | 0.589 | False |
| 2026-07-04 20:56 | 5000 | -5.75 | 0.747 | -3.1 | 0.589 | False |
| 2026-07-05 03:18 | 5000 | -5.5 | 0.758 | -2.85 | 0.623 | False |

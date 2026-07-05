# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-05 20:58_

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

- Current-params net profit (full sample): **-5.99%**, PF 0.739, 66 trades, max DD -852.26
- Optimizer out-of-sample: net **-2.81%**, PF 0.624, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-04 10:08 | 5000 | -6.54 | 0.719 | -3.07 | 0.589 | False |
| 2026-07-04 13:23 | 5000 | -5.71 | 0.747 | -3.07 | 0.589 | False |
| 2026-07-04 17:04 | 5000 | -5.75 | 0.747 | -3.1 | 0.589 | False |
| 2026-07-04 20:56 | 5000 | -5.75 | 0.747 | -3.1 | 0.589 | False |
| 2026-07-05 03:18 | 5000 | -5.5 | 0.758 | -2.85 | 0.623 | False |
| 2026-07-05 07:24 | 5000 | -5.5 | 0.758 | -2.47 | 0.658 | False |
| 2026-07-05 10:11 | 5000 | -6.18 | 0.732 | -2.82 | 0.624 | False |
| 2026-07-05 13:36 | 5000 | -5.99 | 0.739 | -2.82 | 0.624 | False |
| 2026-07-05 17:09 | 5000 | -5.99 | 0.739 | -2.82 | 0.624 | False |
| 2026-07-05 20:58 | 5000 | -5.99 | 0.739 | -2.81 | 0.624 | False |

# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-06 15:30_

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

- Current-params net profit (full sample): **-6.56%**, PF 0.718, 67 trades, max DD -888.02
- Optimizer out-of-sample: net **-2.88%**, PF 0.636, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-04 20:56 | 5000 | -5.75 | 0.747 | -3.1 | 0.589 | False |
| 2026-07-05 03:18 | 5000 | -5.5 | 0.758 | -2.85 | 0.623 | False |
| 2026-07-05 07:24 | 5000 | -5.5 | 0.758 | -2.47 | 0.658 | False |
| 2026-07-05 10:11 | 5000 | -6.18 | 0.732 | -2.82 | 0.624 | False |
| 2026-07-05 13:36 | 5000 | -5.99 | 0.739 | -2.82 | 0.624 | False |
| 2026-07-05 17:09 | 5000 | -5.99 | 0.739 | -2.82 | 0.624 | False |
| 2026-07-05 20:58 | 5000 | -5.99 | 0.739 | -2.81 | 0.624 | False |
| 2026-07-06 03:26 | 5000 | -7.06 | 0.698 | -3.44 | 0.575 | False |
| 2026-07-06 08:19 | 5000 | -6.64 | 0.712 | -3.48 | 0.573 | False |
| 2026-07-06 15:30 | 5000 | -6.56 | 0.718 | -2.88 | 0.636 | False |

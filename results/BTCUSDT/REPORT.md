# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-06-15 21:05_

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

- Current-params net profit (full sample): **-6.6%**, PF 0.668, 64 trades, max DD -1013.36
- Optimizer out-of-sample: net **3.32%**, PF 1.539, 19 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-14 09:10 | 5000 | -8.15 | 0.602 | 4.03 | 2.011 | False |
| 2026-06-14 12:44 | 5000 | -7.95 | 0.609 | 3.51 | 1.766 | True |
| 2026-06-14 16:35 | 5000 | -6.36 | 0.656 | 3.74 | 1.852 | True |
| 2026-06-14 20:32 | 5000 | -6.36 | 0.656 | 3.37 | 1.729 | True |
| 2026-06-15 00:59 | 5000 | -6.73 | 0.643 | 3.21 | 1.668 | True |
| 2026-06-15 05:52 | 5000 | -6.73 | 0.643 | 3.21 | 1.668 | True |
| 2026-06-15 10:12 | 5000 | -6.73 | 0.643 | 3.21 | 1.668 | True |
| 2026-06-15 14:12 | 5000 | -5.44 | 0.71 | 4.64 | 1.954 | True |
| 2026-06-15 17:41 | 5000 | -6.39 | 0.676 | 3.59 | 1.608 | True |
| 2026-06-15 21:05 | 5000 | -6.6 | 0.668 | 3.32 | 1.539 | True |

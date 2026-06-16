# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-06-16 01:04_

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

- Current-params net profit (full sample): **-6.63%**, PF 0.669, 64 trades, max DD -1012.93
- Optimizer out-of-sample: net **3.57%**, PF 1.613, 18 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-14 12:44 | 5000 | -7.95 | 0.609 | 3.51 | 1.766 | True |
| 2026-06-14 16:35 | 5000 | -6.36 | 0.656 | 3.74 | 1.852 | True |
| 2026-06-14 20:32 | 5000 | -6.36 | 0.656 | 3.37 | 1.729 | True |
| 2026-06-15 00:59 | 5000 | -6.73 | 0.643 | 3.21 | 1.668 | True |
| 2026-06-15 05:52 | 5000 | -6.73 | 0.643 | 3.21 | 1.668 | True |
| 2026-06-15 10:12 | 5000 | -6.73 | 0.643 | 3.21 | 1.668 | True |
| 2026-06-15 14:12 | 5000 | -5.44 | 0.71 | 4.64 | 1.954 | True |
| 2026-06-15 17:41 | 5000 | -6.39 | 0.676 | 3.59 | 1.608 | True |
| 2026-06-15 21:05 | 5000 | -6.6 | 0.668 | 3.32 | 1.539 | True |
| 2026-06-16 01:04 | 5000 | -6.63 | 0.669 | 3.57 | 1.613 | True |

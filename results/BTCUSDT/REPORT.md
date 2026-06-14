# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-06-14 20:32_

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

- Current-params net profit (full sample): **-6.36%**, PF 0.656, 59 trades, max DD -993.29
- Optimizer out-of-sample: net **3.37%**, PF 1.729, 15 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-13 09:08 | 5000 | -8.08 | 0.601 | 3.86 | 1.899 | False |
| 2026-06-13 12:41 | 5000 | -8.06 | 0.603 | 4.09 | 2.069 | False |
| 2026-06-13 16:34 | 5000 | -7.97 | 0.606 | 4.21 | 2.089 | False |
| 2026-06-13 20:31 | 5000 | -8.58 | 0.587 | 4.1 | 2.036 | False |
| 2026-06-14 00:57 | 5000 | -8.11 | 0.602 | 4.07 | 2.011 | False |
| 2026-06-14 05:38 | 5000 | -8.11 | 0.602 | 4.07 | 2.011 | False |
| 2026-06-14 09:10 | 5000 | -8.15 | 0.602 | 4.03 | 2.011 | False |
| 2026-06-14 12:44 | 5000 | -7.95 | 0.609 | 3.51 | 1.766 | True |
| 2026-06-14 16:35 | 5000 | -6.36 | 0.656 | 3.74 | 1.852 | True |
| 2026-06-14 20:32 | 5000 | -6.36 | 0.656 | 3.37 | 1.729 | True |

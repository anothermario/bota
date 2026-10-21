# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-21 08:15_

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
  "chand_len": 26,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-8.91%**, PF 0.632, 75 trades, max DD -1018.25
- Optimizer out-of-sample: net **-0.23%**, PF 0.964, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-19 20:12 | 5000 | -8.08 | 0.655 | -0.0 | 0.999 | False |
| 2026-10-20 00:29 | 5000 | -8.08 | 0.655 | -2.31 | 0.75 | False |
| 2026-10-20 04:13 | 5000 | -8.08 | 0.655 | -0.0 | 1.0 | False |
| 2026-10-20 08:15 | 5000 | -8.08 | 0.655 | -2.2 | 0.762 | False |
| 2026-10-20 12:17 | 5000 | -8.08 | 0.655 | 0.14 | 1.023 | True |
| 2026-10-20 16:13 | 5000 | -8.91 | 0.633 | -0.76 | 0.889 | False |
| 2026-10-20 20:11 | 5000 | -8.91 | 0.633 | -1.4 | 0.813 | False |
| 2026-10-21 00:28 | 5000 | -8.91 | 0.633 | -0.76 | 0.89 | False |
| 2026-10-21 04:13 | 5000 | -8.91 | 0.632 | -0.77 | 0.889 | False |
| 2026-10-21 08:15 | 5000 | -8.91 | 0.632 | -0.23 | 0.964 | False |

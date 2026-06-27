# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-06-27 00:50_

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
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-10.54%**, PF 0.642, 92 trades, max DD -1149.95
- Optimizer out-of-sample: net **-1.08%**, PF 0.841, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-25 12:51 | 5000 | -10.15 | 0.647 | -0.9 | 0.857 | False |
| 2026-06-25 16:49 | 5000 | -11.93 | 0.607 | -1.25 | 0.813 | False |
| 2026-06-25 20:43 | 5000 | -11.14 | 0.625 | -1.89 | 0.741 | False |
| 2026-06-26 00:53 | 5000 | -10.48 | 0.641 | -0.65 | 0.894 | False |
| 2026-06-26 05:30 | 5000 | -10.48 | 0.641 | -0.22 | 0.962 | False |
| 2026-06-26 09:10 | 5000 | -11.15 | 0.625 | -0.22 | 0.962 | False |
| 2026-06-26 12:48 | 5000 | -11.17 | 0.625 | -0.99 | 0.847 | False |
| 2026-06-26 16:44 | 5000 | -11.25 | 0.625 | -1.75 | 0.754 | False |
| 2026-06-26 20:37 | 5000 | -10.55 | 0.642 | -1.08 | 0.841 | False |
| 2026-06-27 00:50 | 5000 | -10.54 | 0.642 | -1.08 | 0.841 | False |

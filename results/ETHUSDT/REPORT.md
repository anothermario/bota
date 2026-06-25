# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-06-25 05:24_

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

- Current-params net profit (full sample): **-9.48%**, PF 0.662, 89 trades, max DD -1209.18
- Optimizer out-of-sample: net **-0.89%**, PF 0.863, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-23 16:52 | 5000 | -11.46 | 0.598 | -3.35 | 0.62 | False |
| 2026-06-23 20:47 | 5000 | -11.39 | 0.599 | -3.34 | 0.621 | False |
| 2026-06-24 00:47 | 5000 | -11.39 | 0.599 | -3.2 | 0.528 | False |
| 2026-06-24 05:23 | 5000 | -11.63 | 0.594 | -3.8 | 0.426 | False |
| 2026-06-24 09:11 | 5000 | -11.97 | 0.58 | -3.8 | 0.426 | False |
| 2026-06-24 12:50 | 5000 | -11.97 | 0.58 | -3.8 | 0.426 | False |
| 2026-06-24 16:48 | 5000 | -11.99 | 0.58 | -3.04 | 0.519 | False |
| 2026-06-24 20:38 | 5000 | -9.87 | 0.651 | -0.43 | 0.932 | False |
| 2026-06-25 00:51 | 5000 | -9.5 | 0.661 | -0.86 | 0.863 | False |
| 2026-06-25 05:24 | 5000 | -9.48 | 0.662 | -0.89 | 0.863 | False |

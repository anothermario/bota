# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-06-25 16:49_

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

- Current-params net profit (full sample): **-11.93%**, PF 0.607, 93 trades, max DD -1242.52
- Optimizer out-of-sample: net **-1.25%**, PF 0.813, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-24 05:23 | 5000 | -11.63 | 0.594 | -3.8 | 0.426 | False |
| 2026-06-24 09:11 | 5000 | -11.97 | 0.58 | -3.8 | 0.426 | False |
| 2026-06-24 12:50 | 5000 | -11.97 | 0.58 | -3.8 | 0.426 | False |
| 2026-06-24 16:48 | 5000 | -11.99 | 0.58 | -3.04 | 0.519 | False |
| 2026-06-24 20:38 | 5000 | -9.87 | 0.651 | -0.43 | 0.932 | False |
| 2026-06-25 00:51 | 5000 | -9.5 | 0.661 | -0.86 | 0.863 | False |
| 2026-06-25 05:24 | 5000 | -9.48 | 0.662 | -0.89 | 0.863 | False |
| 2026-06-25 09:10 | 5000 | -8.99 | 0.675 | -0.89 | 0.863 | False |
| 2026-06-25 12:51 | 5000 | -10.15 | 0.647 | -0.9 | 0.857 | False |
| 2026-06-25 16:49 | 5000 | -11.93 | 0.607 | -1.25 | 0.813 | False |

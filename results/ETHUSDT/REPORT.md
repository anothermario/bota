# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-06-27 16:27_

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

- Current-params net profit (full sample): **-11.32%**, PF 0.617, 91 trades, max DD -1143.98
- Optimizer out-of-sample: net **-0.92%**, PF 0.859, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-26 05:30 | 5000 | -10.48 | 0.641 | -0.22 | 0.962 | False |
| 2026-06-26 09:10 | 5000 | -11.15 | 0.625 | -0.22 | 0.962 | False |
| 2026-06-26 12:48 | 5000 | -11.17 | 0.625 | -0.99 | 0.847 | False |
| 2026-06-26 16:44 | 5000 | -11.25 | 0.625 | -1.75 | 0.754 | False |
| 2026-06-26 20:37 | 5000 | -10.55 | 0.642 | -1.08 | 0.841 | False |
| 2026-06-27 00:50 | 5000 | -10.54 | 0.642 | -1.08 | 0.841 | False |
| 2026-06-27 05:21 | 5000 | -11.49 | 0.619 | -0.88 | 0.859 | False |
| 2026-06-27 08:59 | 5000 | -10.52 | 0.642 | -0.88 | 0.859 | False |
| 2026-06-27 12:32 | 5000 | -11.29 | 0.616 | -0.88 | 0.859 | False |
| 2026-06-27 16:27 | 5000 | -11.32 | 0.617 | -0.92 | 0.859 | False |

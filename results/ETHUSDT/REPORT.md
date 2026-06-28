# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-06-28 05:34_

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

- Current-params net profit (full sample): **-11.02%**, PF 0.625, 90 trades, max DD -1226.75
- Optimizer out-of-sample: net **-1.52%**, PF 0.78, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-26 16:44 | 5000 | -11.25 | 0.625 | -1.75 | 0.754 | False |
| 2026-06-26 20:37 | 5000 | -10.55 | 0.642 | -1.08 | 0.841 | False |
| 2026-06-27 00:50 | 5000 | -10.54 | 0.642 | -1.08 | 0.841 | False |
| 2026-06-27 05:21 | 5000 | -11.49 | 0.619 | -0.88 | 0.859 | False |
| 2026-06-27 08:59 | 5000 | -10.52 | 0.642 | -0.88 | 0.859 | False |
| 2026-06-27 12:32 | 5000 | -11.29 | 0.616 | -0.88 | 0.859 | False |
| 2026-06-27 16:27 | 5000 | -11.32 | 0.617 | -0.92 | 0.859 | False |
| 2026-06-27 20:27 | 5000 | -11.96 | 0.603 | -1.52 | 0.78 | False |
| 2026-06-28 00:53 | 5000 | -11.76 | 0.607 | -1.52 | 0.78 | False |
| 2026-06-28 05:34 | 5000 | -11.02 | 0.625 | -1.52 | 0.78 | False |

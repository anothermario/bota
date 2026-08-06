# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-06 00:32_

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
  "chand_len": 18,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-13.9%**, PF 0.494, 66 trades, max DD -1545.49
- Optimizer out-of-sample: net **-3.34%**, PF 0.648, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-04 14:08 | 5000 | -11.66 | 0.577 | -2.96 | 0.655 | False |
| 2026-08-04 17:47 | 5000 | -11.66 | 0.577 | -2.52 | 0.701 | False |
| 2026-08-04 20:33 | 5000 | -11.66 | 0.591 | -2.51 | 0.701 | False |
| 2026-08-05 00:35 | 5000 | -11.21 | 0.602 | -2.51 | 0.702 | False |
| 2026-08-05 05:05 | 5000 | -10.78 | 0.612 | -3.67 | 0.602 | False |
| 2026-08-05 08:58 | 5000 | -10.82 | 0.612 | -3.71 | 0.602 | False |
| 2026-08-05 12:39 | 5000 | -12.33 | 0.563 | -3.31 | 0.629 | False |
| 2026-08-05 16:35 | 5000 | -12.31 | 0.56 | -3.31 | 0.629 | False |
| 2026-08-05 20:32 | 5000 | -13.27 | 0.521 | -3.11 | 0.644 | False |
| 2026-08-06 00:32 | 5000 | -13.9 | 0.494 | -3.34 | 0.648 | False |

# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-16 00:28_

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

- Current-params net profit (full sample): **-12.04%**, PF 0.606, 102 trades, max DD -1438.89
- Optimizer out-of-sample: net **-1.01%**, PF 0.845, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-14 12:17 | 5000 | -14.48 | 0.542 | -2.28 | 0.67 | False |
| 2026-10-14 16:12 | 5000 | -14.26 | 0.547 | -2.4 | 0.654 | False |
| 2026-10-14 20:11 | 5000 | -13.68 | 0.559 | -2.4 | 0.654 | False |
| 2026-10-15 00:28 | 5000 | -13.68 | 0.559 | -2.3 | 0.664 | False |
| 2026-10-15 04:13 | 5000 | -13.37 | 0.575 | -1.99 | 0.732 | False |
| 2026-10-15 08:15 | 5000 | -13.37 | 0.575 | -1.98 | 0.732 | False |
| 2026-10-15 12:17 | 5000 | -12.75 | 0.589 | -1.98 | 0.733 | False |
| 2026-10-15 16:12 | 5000 | -13.57 | 0.571 | -2.0 | 0.733 | False |
| 2026-10-15 20:10 | 5000 | -12.33 | 0.598 | -0.99 | 0.849 | False |
| 2026-10-16 00:28 | 5000 | -12.04 | 0.606 | -1.01 | 0.845 | False |

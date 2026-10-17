# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-17 04:12_

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

- Current-params net profit (full sample): **-12.82%**, PF 0.592, 102 trades, max DD -1410.62
- Optimizer out-of-sample: net **-1.93%**, PF 0.74, 24 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-15 16:12 | 5000 | -13.57 | 0.571 | -2.0 | 0.733 | False |
| 2026-10-15 20:10 | 5000 | -12.33 | 0.598 | -0.99 | 0.849 | False |
| 2026-10-16 00:28 | 5000 | -12.04 | 0.606 | -1.01 | 0.845 | False |
| 2026-10-16 04:13 | 5000 | -12.01 | 0.607 | -0.97 | 0.85 | False |
| 2026-10-16 08:15 | 5000 | -12.53 | 0.595 | -0.75 | 0.88 | False |
| 2026-10-16 12:17 | 5000 | -12.71 | 0.594 | -1.85 | 0.748 | False |
| 2026-10-16 16:12 | 5000 | -12.73 | 0.593 | -1.35 | 0.803 | False |
| 2026-10-16 20:10 | 5000 | -12.59 | 0.597 | -1.37 | 0.803 | False |
| 2026-10-17 00:28 | 5000 | -12.82 | 0.592 | -1.63 | 0.772 | False |
| 2026-10-17 04:12 | 5000 | -12.82 | 0.592 | -1.93 | 0.74 | False |

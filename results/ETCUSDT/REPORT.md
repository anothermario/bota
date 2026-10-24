# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-24 16:10_

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

- Current-params net profit (full sample): **-10.85%**, PF 0.573, 65 trades, max DD -1606.04
- Optimizer out-of-sample: net **-4.08%**, PF 0.514, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-23 04:13 | 5000 | -11.79 | 0.545 | -3.87 | 0.551 | False |
| 2026-10-23 08:15 | 5000 | -11.79 | 0.545 | -4.81 | 0.494 | False |
| 2026-10-23 12:15 | 5000 | -11.79 | 0.545 | -3.81 | 0.555 | False |
| 2026-10-23 16:12 | 5000 | -11.45 | 0.557 | -3.44 | 0.595 | False |
| 2026-10-23 20:11 | 5000 | -11.36 | 0.559 | -3.44 | 0.595 | False |
| 2026-10-24 00:28 | 5000 | -10.82 | 0.573 | -3.32 | 0.604 | False |
| 2026-10-24 04:12 | 5000 | -10.82 | 0.573 | -3.34 | 0.601 | False |
| 2026-10-24 08:13 | 5000 | -10.85 | 0.573 | -4.13 | 0.511 | False |
| 2026-10-24 12:14 | 5000 | -10.85 | 0.573 | -4.5 | 0.488 | False |
| 2026-10-24 16:10 | 5000 | -10.85 | 0.573 | -4.08 | 0.514 | False |

# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-09 12:17_

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

- Current-params net profit (full sample): **-5.88%**, PF 0.761, 62 trades, max DD -1393.86
- Optimizer out-of-sample: net **-7.0%**, PF 0.156, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-08 00:33 | 5000 | -5.76 | 0.768 | -6.64 | 0.213 | False |
| 2026-10-08 04:15 | 5000 | -5.47 | 0.778 | -6.35 | 0.244 | False |
| 2026-10-08 08:18 | 5000 | -5.47 | 0.778 | -6.35 | 0.244 | False |
| 2026-10-08 12:18 | 5000 | -5.47 | 0.778 | -6.35 | 0.244 | False |
| 2026-10-08 16:14 | 5000 | -5.51 | 0.777 | -6.25 | 0.247 | False |
| 2026-10-08 20:12 | 5000 | -5.68 | 0.772 | -6.11 | 0.275 | False |
| 2026-10-09 00:35 | 5000 | -6.61 | 0.733 | -6.38 | 0.244 | False |
| 2026-10-09 04:17 | 5000 | -6.61 | 0.733 | -7.1 | 0.152 | False |
| 2026-10-09 08:18 | 5000 | -6.61 | 0.733 | -6.24 | 0.261 | False |
| 2026-10-09 12:17 | 5000 | -5.88 | 0.761 | -7.0 | 0.156 | False |

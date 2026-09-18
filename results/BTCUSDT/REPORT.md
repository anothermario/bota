# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-18 12:16_

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
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-7.66%**, PF 0.578, 65 trades, max DD -903.62
- Optimizer out-of-sample: net **-2.24%**, PF 0.68, 17 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-17 00:30 | 5000 | -8.35 | 0.553 | -3.72 | 0.553 | False |
| 2026-09-17 04:14 | 5000 | -7.78 | 0.572 | -2.87 | 0.618 | False |
| 2026-09-17 08:16 | 5000 | -7.35 | 0.594 | -2.87 | 0.618 | False |
| 2026-09-17 12:17 | 5000 | -7.34 | 0.594 | -2.86 | 0.618 | False |
| 2026-09-17 16:13 | 5000 | -6.76 | 0.629 | -3.0 | 0.608 | False |
| 2026-09-17 20:12 | 5000 | -7.62 | 0.578 | -2.2 | 0.68 | False |
| 2026-09-18 00:30 | 5000 | -7.62 | 0.578 | -2.2 | 0.68 | False |
| 2026-09-18 04:13 | 5000 | -7.66 | 0.578 | -2.24 | 0.68 | False |
| 2026-09-18 08:15 | 5000 | -7.66 | 0.578 | -2.24 | 0.68 | False |
| 2026-09-18 12:16 | 5000 | -7.66 | 0.578 | -2.24 | 0.68 | False |

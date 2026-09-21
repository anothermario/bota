# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-21 12:16_

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

- Current-params net profit (full sample): **-7.62%**, PF 0.599, 68 trades, max DD -904.89
- Optimizer out-of-sample: net **-4.57%**, PF 0.402, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-20 00:34 | 5000 | -6.64 | 0.649 | -3.89 | 0.468 | False |
| 2026-09-20 04:12 | 5000 | -6.96 | 0.638 | -3.93 | 0.468 | False |
| 2026-09-20 08:14 | 5000 | -6.73 | 0.646 | -3.93 | 0.468 | False |
| 2026-09-20 12:15 | 5000 | -6.73 | 0.646 | -3.93 | 0.468 | False |
| 2026-09-20 16:11 | 5000 | -7.06 | 0.633 | -4.56 | 0.428 | False |
| 2026-09-20 20:10 | 5000 | -7.1 | 0.633 | -4.46 | 0.436 | False |
| 2026-09-21 00:33 | 5000 | -8.54 | 0.568 | -4.54 | 0.402 | False |
| 2026-09-21 04:14 | 5000 | -8.23 | 0.578 | -4.54 | 0.402 | False |
| 2026-09-21 08:18 | 5000 | -8.15 | 0.581 | -4.54 | 0.402 | False |
| 2026-09-21 12:16 | 5000 | -7.62 | 0.599 | -4.57 | 0.402 | False |

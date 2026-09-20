# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-20 20:10_

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

- Current-params net profit (full sample): **-7.1%**, PF 0.633, 69 trades, max DD -906.78
- Optimizer out-of-sample: net **-4.46%**, PF 0.436, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-19 08:13 | 5000 | -5.53 | 0.689 | -3.35 | 0.503 | False |
| 2026-09-19 12:15 | 5000 | -5.53 | 0.689 | -2.73 | 0.556 | False |
| 2026-09-19 16:10 | 5000 | -5.56 | 0.689 | -2.77 | 0.556 | False |
| 2026-09-19 20:10 | 5000 | -6.19 | 0.665 | -3.41 | 0.501 | False |
| 2026-09-20 00:34 | 5000 | -6.64 | 0.649 | -3.89 | 0.468 | False |
| 2026-09-20 04:12 | 5000 | -6.96 | 0.638 | -3.93 | 0.468 | False |
| 2026-09-20 08:14 | 5000 | -6.73 | 0.646 | -3.93 | 0.468 | False |
| 2026-09-20 12:15 | 5000 | -6.73 | 0.646 | -3.93 | 0.468 | False |
| 2026-09-20 16:11 | 5000 | -7.06 | 0.633 | -4.56 | 0.428 | False |
| 2026-09-20 20:10 | 5000 | -7.1 | 0.633 | -4.46 | 0.436 | False |

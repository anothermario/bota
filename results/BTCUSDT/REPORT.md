# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-06-19 09:39_

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

- Current-params net profit (full sample): **-7.08%**, PF 0.658, 64 trades, max DD -800.82
- Optimizer out-of-sample: net **-5.03%**, PF 0.375, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-17 20:46 | 5000 | -7.51 | 0.643 | -1.09 | 0.863 | False |
| 2026-06-18 00:57 | 5000 | -7.51 | 0.643 | -2.11 | 0.732 | False |
| 2026-06-18 05:39 | 5000 | -7.51 | 0.643 | -3.54 | 0.539 | False |
| 2026-06-18 09:34 | 5000 | -7.51 | 0.643 | -2.11 | 0.732 | False |
| 2026-06-18 13:15 | 5000 | -7.29 | 0.65 | -2.12 | 0.731 | False |
| 2026-06-18 17:07 | 5000 | -7.31 | 0.65 | -1.5 | 0.814 | False |
| 2026-06-18 20:53 | 5000 | -7.65 | 0.639 | -1.78 | 0.786 | False |
| 2026-06-19 01:03 | 5000 | -7.65 | 0.639 | -3.1 | 0.622 | False |
| 2026-06-19 05:47 | 5000 | -7.67 | 0.638 | -4.08 | 0.498 | False |
| 2026-06-19 09:39 | 5000 | -7.08 | 0.658 | -5.03 | 0.375 | False |

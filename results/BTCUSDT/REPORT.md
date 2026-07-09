# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-09 10:53_

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

- Current-params net profit (full sample): **-6.02%**, PF 0.737, 65 trades, max DD -954.83
- Optimizer out-of-sample: net **-2.21%**, PF 0.658, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-07 21:23 | 5000 | -6.28 | 0.727 | -1.5 | 0.773 | False |
| 2026-07-08 02:35 | 5000 | -6.31 | 0.727 | -1.53 | 0.773 | False |
| 2026-07-08 06:27 | 5000 | -6.31 | 0.727 | -1.53 | 0.774 | False |
| 2026-07-08 10:16 | 5000 | -6.3 | 0.728 | -2.41 | 0.648 | False |
| 2026-07-08 14:03 | 5000 | -6.72 | 0.714 | -3.54 | 0.538 | False |
| 2026-07-08 17:28 | 5000 | -6.71 | 0.714 | -2.86 | 0.592 | False |
| 2026-07-08 21:06 | 5000 | -6.82 | 0.709 | -2.87 | 0.592 | False |
| 2026-07-09 02:53 | 5000 | -6.82 | 0.709 | -2.86 | 0.593 | False |
| 2026-07-09 07:41 | 5000 | -6.02 | 0.737 | -2.86 | 0.595 | False |
| 2026-07-09 10:53 | 5000 | -6.02 | 0.737 | -2.21 | 0.658 | False |

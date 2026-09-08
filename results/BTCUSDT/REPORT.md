# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-08 00:31_

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

- Current-params net profit (full sample): **-8.28%**, PF 0.543, 66 trades, max DD -1004.81
- Optimizer out-of-sample: net **-4.28%**, PF 0.407, 15 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-06 12:14 | 5000 | -7.67 | 0.576 | -3.77 | 0.438 | False |
| 2026-09-06 16:10 | 5000 | -7.67 | 0.576 | -3.77 | 0.438 | False |
| 2026-09-06 20:10 | 5000 | -7.66 | 0.576 | -3.77 | 0.438 | False |
| 2026-09-07 00:33 | 5000 | -8.19 | 0.545 | -3.77 | 0.438 | False |
| 2026-09-07 04:14 | 5000 | -8.19 | 0.545 | -3.77 | 0.438 | False |
| 2026-09-07 08:17 | 5000 | -8.19 | 0.545 | -3.77 | 0.438 | False |
| 2026-09-07 12:17 | 5000 | -8.19 | 0.545 | -3.76 | 0.439 | False |
| 2026-09-07 16:11 | 5000 | -7.78 | 0.56 | -3.14 | 0.488 | False |
| 2026-09-07 20:10 | 5000 | -8.28 | 0.543 | -4.03 | 0.422 | False |
| 2026-09-08 00:31 | 5000 | -8.28 | 0.543 | -4.28 | 0.407 | False |

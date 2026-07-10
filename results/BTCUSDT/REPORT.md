# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-10 21:05_

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

- Current-params net profit (full sample): **-7.33%**, PF 0.696, 68 trades, max DD -1086.02
- Optimizer out-of-sample: net **-4.7%**, PF 0.313, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-09 10:53 | 5000 | -6.02 | 0.737 | -2.21 | 0.658 | False |
| 2026-07-09 14:56 | 5000 | -6.43 | 0.723 | -3.21 | 0.564 | False |
| 2026-07-09 17:54 | 5000 | -6.43 | 0.723 | -3.15 | 0.57 | False |
| 2026-07-09 21:22 | 5000 | -6.43 | 0.723 | -3.57 | 0.472 | False |
| 2026-07-10 02:56 | 5000 | -6.43 | 0.723 | -4.57 | 0.317 | False |
| 2026-07-10 07:34 | 5000 | -6.46 | 0.723 | -4.6 | 0.317 | False |
| 2026-07-10 10:52 | 5000 | -6.46 | 0.723 | -4.58 | 0.319 | False |
| 2026-07-10 14:24 | 5000 | -7.33 | 0.696 | -5.49 | 0.279 | False |
| 2026-07-10 17:47 | 5000 | -7.33 | 0.696 | -4.75 | 0.31 | False |
| 2026-07-10 21:05 | 5000 | -7.33 | 0.696 | -4.7 | 0.313 | False |

# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-06 18:10_

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

- Current-params net profit (full sample): **-12.19%**, PF 0.611, 93 trades, max DD -1249.92
- Optimizer out-of-sample: net **-7.76%**, PF 0.302, 31 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-05 03:19 | 5000 | -10.47 | 0.647 | -4.61 | 0.536 | False |
| 2026-07-05 07:25 | 5000 | -10.13 | 0.656 | -4.59 | 0.536 | False |
| 2026-07-05 10:12 | 5000 | -10.08 | 0.658 | -4.54 | 0.541 | False |
| 2026-07-05 13:37 | 5000 | -11.23 | 0.633 | -4.73 | 0.388 | False |
| 2026-07-05 17:09 | 5000 | -10.28 | 0.661 | -4.76 | 0.388 | False |
| 2026-07-05 20:59 | 5000 | -10.56 | 0.65 | -4.66 | 0.537 | False |
| 2026-07-06 03:26 | 5000 | -11.34 | 0.627 | -5.39 | 0.369 | False |
| 2026-07-06 08:19 | 5000 | -11.47 | 0.624 | -5.56 | 0.379 | False |
| 2026-07-06 15:30 | 5000 | -12.17 | 0.611 | -7.65 | 0.305 | False |
| 2026-07-06 18:10 | 5000 | -12.19 | 0.611 | -7.76 | 0.302 | False |

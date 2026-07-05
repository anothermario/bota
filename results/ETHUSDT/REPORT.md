# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-05 20:59_

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

- Current-params net profit (full sample): **-10.56%**, PF 0.65, 91 trades, max DD -1136.06
- Optimizer out-of-sample: net **-4.66%**, PF 0.537, 27 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-04 10:09 | 5000 | -10.65 | 0.641 | -4.21 | 0.411 | False |
| 2026-07-04 13:23 | 5000 | -10.01 | 0.657 | -4.12 | 0.562 | False |
| 2026-07-04 17:04 | 5000 | -10.37 | 0.649 | -4.5 | 0.541 | False |
| 2026-07-04 20:56 | 5000 | -11.06 | 0.632 | -5.76 | 0.346 | False |
| 2026-07-05 03:19 | 5000 | -10.47 | 0.647 | -4.61 | 0.536 | False |
| 2026-07-05 07:25 | 5000 | -10.13 | 0.656 | -4.59 | 0.536 | False |
| 2026-07-05 10:12 | 5000 | -10.08 | 0.658 | -4.54 | 0.541 | False |
| 2026-07-05 13:37 | 5000 | -11.23 | 0.633 | -4.73 | 0.388 | False |
| 2026-07-05 17:09 | 5000 | -10.28 | 0.661 | -4.76 | 0.388 | False |
| 2026-07-05 20:59 | 5000 | -10.56 | 0.65 | -4.66 | 0.537 | False |

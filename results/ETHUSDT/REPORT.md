# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-05 13:37_

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

- Current-params net profit (full sample): **-11.23%**, PF 0.633, 92 trades, max DD -1160.46
- Optimizer out-of-sample: net **-4.73%**, PF 0.388, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-04 02:49 | 5000 | -11.2 | 0.628 | -4.21 | 0.411 | False |
| 2026-07-04 06:46 | 5000 | -10.65 | 0.641 | -4.21 | 0.411 | False |
| 2026-07-04 10:09 | 5000 | -10.65 | 0.641 | -4.21 | 0.411 | False |
| 2026-07-04 13:23 | 5000 | -10.01 | 0.657 | -4.12 | 0.562 | False |
| 2026-07-04 17:04 | 5000 | -10.37 | 0.649 | -4.5 | 0.541 | False |
| 2026-07-04 20:56 | 5000 | -11.06 | 0.632 | -5.76 | 0.346 | False |
| 2026-07-05 03:19 | 5000 | -10.47 | 0.647 | -4.61 | 0.536 | False |
| 2026-07-05 07:25 | 5000 | -10.13 | 0.656 | -4.59 | 0.536 | False |
| 2026-07-05 10:12 | 5000 | -10.08 | 0.658 | -4.54 | 0.541 | False |
| 2026-07-05 13:37 | 5000 | -11.23 | 0.633 | -4.73 | 0.388 | False |

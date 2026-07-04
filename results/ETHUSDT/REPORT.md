# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-04 17:04_

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

- Current-params net profit (full sample): **-10.37%**, PF 0.649, 89 trades, max DD -1144.86
- Optimizer out-of-sample: net **-4.5%**, PF 0.541, 25 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-03 07:19 | 5000 | -11.15 | 0.626 | -4.2 | 0.41 | False |
| 2026-07-03 10:34 | 5000 | -11.17 | 0.626 | -4.22 | 0.41 | False |
| 2026-07-03 14:01 | 5000 | -10.8 | 0.635 | -4.22 | 0.41 | False |
| 2026-07-03 17:25 | 5000 | -10.94 | 0.631 | -4.38 | 0.399 | False |
| 2026-07-03 21:05 | 5000 | -10.97 | 0.631 | -4.41 | 0.399 | False |
| 2026-07-04 02:49 | 5000 | -11.2 | 0.628 | -4.21 | 0.411 | False |
| 2026-07-04 06:46 | 5000 | -10.65 | 0.641 | -4.21 | 0.411 | False |
| 2026-07-04 10:09 | 5000 | -10.65 | 0.641 | -4.21 | 0.411 | False |
| 2026-07-04 13:23 | 5000 | -10.01 | 0.657 | -4.12 | 0.562 | False |
| 2026-07-04 17:04 | 5000 | -10.37 | 0.649 | -4.5 | 0.541 | False |

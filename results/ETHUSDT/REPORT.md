# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-21 02:34_

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

- Current-params net profit (full sample): **-17.51%**, PF 0.49, 95 trades, max DD -1964.55
- Optimizer out-of-sample: net **-11.54%**, PF 0.118, 30 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-19 13:15 | 5000 | -16.66 | 0.5 | -11.06 | 0.124 | False |
| 2026-07-19 16:57 | 5000 | -17.0 | 0.494 | -11.05 | 0.124 | False |
| 2026-07-19 20:45 | 5000 | -16.99 | 0.494 | -10.71 | 0.128 | False |
| 2026-07-20 02:51 | 5000 | -17.2 | 0.493 | -11.49 | 0.121 | False |
| 2026-07-20 06:44 | 5000 | -16.68 | 0.502 | -11.77 | 0.115 | False |
| 2026-07-20 10:51 | 5000 | -17.75 | 0.485 | -12.1 | 0.112 | False |
| 2026-07-20 14:03 | 5000 | -17.18 | 0.494 | -12.1 | 0.112 | False |
| 2026-07-20 18:01 | 5000 | -17.88 | 0.483 | -11.45 | 0.119 | False |
| 2026-07-20 21:11 | 5000 | -17.84 | 0.483 | -11.44 | 0.119 | False |
| 2026-07-21 02:34 | 5000 | -17.51 | 0.49 | -11.54 | 0.118 | False |

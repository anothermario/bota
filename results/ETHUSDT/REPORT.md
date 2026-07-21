# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-21 13:46_

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

- Current-params net profit (full sample): **-16.5%**, PF 0.517, 95 trades, max DD -1968.99
- Optimizer out-of-sample: net **-10.96%**, PF 0.147, 30 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-20 02:51 | 5000 | -17.2 | 0.493 | -11.49 | 0.121 | False |
| 2026-07-20 06:44 | 5000 | -16.68 | 0.502 | -11.77 | 0.115 | False |
| 2026-07-20 10:51 | 5000 | -17.75 | 0.485 | -12.1 | 0.112 | False |
| 2026-07-20 14:03 | 5000 | -17.18 | 0.494 | -12.1 | 0.112 | False |
| 2026-07-20 18:01 | 5000 | -17.88 | 0.483 | -11.45 | 0.119 | False |
| 2026-07-20 21:11 | 5000 | -17.84 | 0.483 | -11.44 | 0.119 | False |
| 2026-07-21 02:34 | 5000 | -17.51 | 0.49 | -11.54 | 0.118 | False |
| 2026-07-21 06:27 | 5000 | -17.52 | 0.49 | -11.32 | 0.121 | False |
| 2026-07-21 10:24 | 5000 | -17.49 | 0.49 | -11.32 | 0.121 | False |
| 2026-07-21 13:46 | 5000 | -16.5 | 0.517 | -10.96 | 0.147 | False |

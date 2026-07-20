# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-20 06:44_

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

- Current-params net profit (full sample): **-16.68%**, PF 0.502, 94 trades, max DD -1876.27
- Optimizer out-of-sample: net **-11.77%**, PF 0.115, 31 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-18 16:57 | 5000 | -16.63 | 0.508 | -11.59 | 0.12 | False |
| 2026-07-18 20:45 | 5000 | -17.09 | 0.491 | -10.99 | 0.127 | False |
| 2026-07-19 02:36 | 5000 | -17.0 | 0.492 | -11.01 | 0.127 | False |
| 2026-07-19 06:29 | 5000 | -17.02 | 0.492 | -11.04 | 0.125 | False |
| 2026-07-19 09:52 | 5000 | -16.98 | 0.493 | -11.06 | 0.124 | False |
| 2026-07-19 13:15 | 5000 | -16.66 | 0.5 | -11.06 | 0.124 | False |
| 2026-07-19 16:57 | 5000 | -17.0 | 0.494 | -11.05 | 0.124 | False |
| 2026-07-19 20:45 | 5000 | -16.99 | 0.494 | -10.71 | 0.128 | False |
| 2026-07-20 02:51 | 5000 | -17.2 | 0.493 | -11.49 | 0.121 | False |
| 2026-07-20 06:44 | 5000 | -16.68 | 0.502 | -11.77 | 0.115 | False |

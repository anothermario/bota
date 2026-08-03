# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-03 21:01_

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
  "chand_len": 18,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-9.54%**, PF 0.626, 63 trades, max DD -1550.61
- Optimizer out-of-sample: net **-2.21%**, PF 0.738, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-02 09:55 | 5000 | -10.75 | 0.589 | -3.78 | 0.575 | False |
| 2026-08-02 13:17 | 5000 | -10.76 | 0.589 | -3.78 | 0.575 | False |
| 2026-08-02 16:57 | 5000 | -10.36 | 0.604 | -3.32 | 0.624 | False |
| 2026-08-02 20:54 | 5000 | -10.37 | 0.603 | -3.32 | 0.624 | False |
| 2026-08-03 02:41 | 5000 | -9.51 | 0.626 | -3.32 | 0.624 | False |
| 2026-08-03 06:59 | 5000 | -9.51 | 0.626 | -1.89 | 0.773 | False |
| 2026-08-03 11:21 | 5000 | -10.16 | 0.609 | -1.89 | 0.773 | False |
| 2026-08-03 14:36 | 5000 | -10.22 | 0.608 | -1.92 | 0.774 | False |
| 2026-08-03 17:49 | 5000 | -9.95 | 0.615 | -2.2 | 0.739 | False |
| 2026-08-03 21:01 | 5000 | -9.54 | 0.626 | -2.21 | 0.738 | False |

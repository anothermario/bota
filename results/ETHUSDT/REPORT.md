# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-02 07:31_

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

- Current-params net profit (full sample): **-12.54%**, PF 0.585, 91 trades, max DD -1279.37
- Optimizer out-of-sample: net **-5.06%**, PF 0.29, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-30 16:47 | 5000 | -10.98 | 0.615 | -1.32 | 0.781 | False |
| 2026-06-30 20:41 | 5000 | -11.28 | 0.608 | -2.72 | 0.54 | False |
| 2026-07-01 00:54 | 5000 | -10.98 | 0.615 | -2.82 | 0.524 | False |
| 2026-07-01 05:36 | 5000 | -11.0 | 0.616 | -2.82 | 0.528 | False |
| 2026-07-01 09:12 | 5000 | -11.64 | 0.602 | -4.2 | 0.377 | False |
| 2026-07-01 13:01 | 5000 | -12.46 | 0.576 | -5.63 | 0.233 | False |
| 2026-07-01 16:50 | 5000 | -12.07 | 0.586 | -5.86 | 0.215 | False |
| 2026-07-01 20:37 | 5000 | -12.07 | 0.586 | -5.75 | 0.219 | False |
| 2026-07-02 00:51 | 5000 | -11.8 | 0.601 | -5.57 | 0.244 | False |
| 2026-07-02 07:31 | 5000 | -12.54 | 0.585 | -5.06 | 0.29 | False |

# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-02 13:58_

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

- Current-params net profit (full sample): **-11.9%**, PF 0.6, 90 trades, max DD -1212.42
- Optimizer out-of-sample: net **-5.08%**, PF 0.291, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-01 00:54 | 5000 | -10.98 | 0.615 | -2.82 | 0.524 | False |
| 2026-07-01 05:36 | 5000 | -11.0 | 0.616 | -2.82 | 0.528 | False |
| 2026-07-01 09:12 | 5000 | -11.64 | 0.602 | -4.2 | 0.377 | False |
| 2026-07-01 13:01 | 5000 | -12.46 | 0.576 | -5.63 | 0.233 | False |
| 2026-07-01 16:50 | 5000 | -12.07 | 0.586 | -5.86 | 0.215 | False |
| 2026-07-01 20:37 | 5000 | -12.07 | 0.586 | -5.75 | 0.219 | False |
| 2026-07-02 00:51 | 5000 | -11.8 | 0.601 | -5.57 | 0.244 | False |
| 2026-07-02 07:31 | 5000 | -12.54 | 0.585 | -5.06 | 0.29 | False |
| 2026-07-02 10:38 | 5000 | -12.54 | 0.585 | -5.06 | 0.29 | False |
| 2026-07-02 13:58 | 5000 | -11.9 | 0.6 | -5.08 | 0.291 | False |

# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-11 20:45_

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

- Current-params net profit (full sample): **-12.52%**, PF 0.617, 95 trades, max DD -1431.92
- Optimizer out-of-sample: net **-5.88%**, PF 0.315, 28 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-10 10:52 | 5000 | -13.73 | 0.582 | -9.3 | 0.134 | False |
| 2026-07-10 14:24 | 5000 | -13.55 | 0.593 | -6.91 | 0.277 | False |
| 2026-07-10 17:47 | 5000 | -13.51 | 0.594 | -6.91 | 0.277 | False |
| 2026-07-10 21:05 | 5000 | -12.49 | 0.616 | -6.87 | 0.278 | False |
| 2026-07-11 02:33 | 5000 | -12.84 | 0.608 | -7.31 | 0.264 | False |
| 2026-07-11 06:12 | 5000 | -11.72 | 0.632 | -6.69 | 0.284 | False |
| 2026-07-11 09:28 | 5000 | -12.34 | 0.619 | -6.7 | 0.284 | False |
| 2026-07-11 13:16 | 5000 | -11.72 | 0.632 | -5.9 | 0.312 | False |
| 2026-07-11 16:57 | 5000 | -13.18 | 0.603 | -6.64 | 0.287 | False |
| 2026-07-11 20:45 | 5000 | -12.52 | 0.617 | -5.88 | 0.315 | False |

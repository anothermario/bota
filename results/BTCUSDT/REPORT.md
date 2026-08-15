# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-15 00:14_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.35,
  "use_adx": true,
  "adx_len": 14,
  "adx_thresh": 20.0,
  "don_len": 30,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-11.85%**, PF 0.449, 70 trades, max DD -1386.62
- Optimizer out-of-sample: net **-2.51%**, PF 0.412, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-13 12:19 | 5000 | -11.5 | 0.48 | -4.78 | 0.346 | False |
| 2026-08-13 16:20 | 5000 | -11.5 | 0.48 | -6.29 | 0.283 | False |
| 2026-08-13 20:13 | 5000 | -11.5 | 0.48 | -1.08 | 0.694 | False |
| 2026-08-14 00:26 | 5000 | -11.52 | 0.479 | -1.08 | 0.694 | False |
| 2026-08-14 04:36 | 5000 | -12.31 | 0.438 | -2.27 | 0.458 | False |
| 2026-08-14 08:30 | 5000 | -12.35 | 0.438 | -2.31 | 0.458 | False |
| 2026-08-14 12:18 | 5000 | -12.35 | 0.438 | -2.3 | 0.46 | False |
| 2026-08-14 16:18 | 5000 | -12.47 | 0.434 | -2.36 | 0.449 | False |
| 2026-08-14 20:11 | 5000 | -11.84 | 0.449 | -2.51 | 0.412 | False |
| 2026-08-15 00:14 | 5000 | -11.85 | 0.449 | -2.51 | 0.412 | False |

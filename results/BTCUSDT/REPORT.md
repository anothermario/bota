# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-15 12:16_

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

- Current-params net profit (full sample): **-9.41%**, PF 0.485, 67 trades, max DD -940.88
- Optimizer out-of-sample: net **-5.44%**, PF 0.356, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-14 00:33 | 5000 | -8.12 | 0.541 | -4.68 | 0.39 | False |
| 2026-09-14 04:14 | 5000 | -8.18 | 0.541 | -4.98 | 0.376 | False |
| 2026-09-14 08:17 | 5000 | -9.44 | 0.482 | -6.39 | 0.318 | False |
| 2026-09-14 12:17 | 5000 | -8.93 | 0.497 | -5.06 | 0.371 | False |
| 2026-09-14 16:11 | 5000 | -8.93 | 0.497 | -5.06 | 0.371 | False |
| 2026-09-14 20:11 | 5000 | -8.73 | 0.505 | -5.09 | 0.371 | False |
| 2026-09-15 00:32 | 5000 | -9.19 | 0.493 | -5.4 | 0.358 | False |
| 2026-09-15 04:13 | 5000 | -9.19 | 0.493 | -5.4 | 0.358 | False |
| 2026-09-15 08:16 | 5000 | -9.41 | 0.485 | -5.45 | 0.356 | False |
| 2026-09-15 12:16 | 5000 | -9.41 | 0.485 | -5.44 | 0.356 | False |

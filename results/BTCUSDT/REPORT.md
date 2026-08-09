# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-09 12:11_

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

- Current-params net profit (full sample): **-12.92%**, PF 0.435, 70 trades, max DD -1303.55
- Optimizer out-of-sample: net **-5.8%**, PF 0.256, 31 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-08 00:19 | 5000 | -13.7 | 0.418 | -5.63 | 0.32 | False |
| 2026-08-08 04:25 | 5000 | -13.91 | 0.414 | -4.89 | 0.353 | False |
| 2026-08-08 08:14 | 5000 | -13.37 | 0.425 | -5.55 | 0.323 | False |
| 2026-08-08 12:10 | 5000 | -13.12 | 0.43 | -5.55 | 0.323 | False |
| 2026-08-08 16:08 | 5000 | -13.12 | 0.43 | -4.93 | 0.354 | False |
| 2026-08-08 20:08 | 5000 | -13.12 | 0.43 | -5.06 | 0.346 | False |
| 2026-08-09 00:19 | 5000 | -13.12 | 0.43 | -5.75 | 0.251 | False |
| 2026-08-09 04:29 | 5000 | -13.16 | 0.43 | -5.79 | 0.251 | False |
| 2026-08-09 08:15 | 5000 | -13.26 | 0.428 | -6.01 | 0.229 | False |
| 2026-08-09 12:11 | 5000 | -12.92 | 0.435 | -5.8 | 0.256 | False |

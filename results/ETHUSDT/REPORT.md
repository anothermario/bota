# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-15 04:13_

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

- Current-params net profit (full sample): **-15.92%**, PF 0.434, 103 trades, max DD -1717.29
- Optimizer out-of-sample: net **-5.85%**, PF 0.477, 33 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-13 16:11 | 5000 | -16.21 | 0.418 | -5.33 | 0.477 | False |
| 2026-09-13 20:10 | 5000 | -16.18 | 0.419 | -5.08 | 0.507 | False |
| 2026-09-14 00:33 | 5000 | -15.83 | 0.437 | -5.41 | 0.475 | False |
| 2026-09-14 04:14 | 5000 | -15.06 | 0.452 | -5.68 | 0.462 | False |
| 2026-09-14 08:18 | 5000 | -15.07 | 0.452 | -5.68 | 0.462 | False |
| 2026-09-14 12:18 | 5000 | -15.85 | 0.424 | -5.96 | 0.449 | False |
| 2026-09-14 16:11 | 5000 | -15.85 | 0.424 | -5.75 | 0.47 | False |
| 2026-09-14 20:11 | 5000 | -15.87 | 0.424 | -6.46 | 0.429 | False |
| 2026-09-15 00:32 | 5000 | -16.15 | 0.43 | -6.17 | 0.463 | False |
| 2026-09-15 04:13 | 5000 | -15.92 | 0.434 | -5.85 | 0.477 | False |

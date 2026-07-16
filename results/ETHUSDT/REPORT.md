# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-16 10:07_

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

- Current-params net profit (full sample): **-16.11%**, PF 0.514, 96 trades, max DD -1632.45
- Optimizer out-of-sample: net **-9.41%**, PF 0.215, 36 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-14 20:59 | 5000 | -15.92 | 0.516 | -9.07 | 0.231 | False |
| 2026-07-15 02:22 | 5000 | -15.6 | 0.526 | -8.57 | 0.272 | False |
| 2026-07-15 06:12 | 5000 | -15.59 | 0.526 | -8.61 | 0.27 | False |
| 2026-07-15 10:01 | 5000 | -15.59 | 0.526 | -8.43 | 0.275 | False |
| 2026-07-15 13:41 | 5000 | -16.21 | 0.515 | -8.53 | 0.274 | False |
| 2026-07-15 17:16 | 5000 | -16.57 | 0.509 | -8.84 | 0.267 | False |
| 2026-07-15 20:59 | 5000 | -15.75 | 0.524 | -9.41 | 0.215 | False |
| 2026-07-16 02:30 | 5000 | -15.75 | 0.524 | -9.41 | 0.215 | False |
| 2026-07-16 06:16 | 5000 | -16.13 | 0.514 | -9.42 | 0.215 | False |
| 2026-07-16 10:07 | 5000 | -16.11 | 0.514 | -9.41 | 0.215 | False |

# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-17 09:56_

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

- Current-params net profit (full sample): **-17.23%**, PF 0.492, 95 trades, max DD -1722.85
- Optimizer out-of-sample: net **-9.15%**, PF 0.223, 34 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-15 20:59 | 5000 | -15.75 | 0.524 | -9.41 | 0.215 | False |
| 2026-07-16 02:30 | 5000 | -15.75 | 0.524 | -9.41 | 0.215 | False |
| 2026-07-16 06:16 | 5000 | -16.13 | 0.514 | -9.42 | 0.215 | False |
| 2026-07-16 10:07 | 5000 | -16.11 | 0.514 | -9.41 | 0.215 | False |
| 2026-07-16 13:47 | 5000 | -15.97 | 0.517 | -9.6 | 0.213 | False |
| 2026-07-16 17:14 | 5000 | -16.74 | 0.505 | -9.6 | 0.213 | False |
| 2026-07-16 20:56 | 5000 | -17.38 | 0.488 | -9.62 | 0.212 | False |
| 2026-07-17 02:32 | 5000 | -17.53 | 0.486 | -10.13 | 0.203 | False |
| 2026-07-17 06:14 | 5000 | -17.54 | 0.487 | -9.75 | 0.21 | False |
| 2026-07-17 09:56 | 5000 | -17.23 | 0.492 | -9.15 | 0.223 | False |

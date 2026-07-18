# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-18 06:04_

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

- Current-params net profit (full sample): **-17.4%**, PF 0.488, 97 trades, max DD -1739.91
- Optimizer out-of-sample: net **-11.12%**, PF 0.125, 33 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-16 17:14 | 5000 | -16.74 | 0.505 | -9.6 | 0.213 | False |
| 2026-07-16 20:56 | 5000 | -17.38 | 0.488 | -9.62 | 0.212 | False |
| 2026-07-17 02:32 | 5000 | -17.53 | 0.486 | -10.13 | 0.203 | False |
| 2026-07-17 06:14 | 5000 | -17.54 | 0.487 | -9.75 | 0.21 | False |
| 2026-07-17 09:56 | 5000 | -17.23 | 0.492 | -9.15 | 0.223 | False |
| 2026-07-17 13:25 | 5000 | -17.0 | 0.491 | -9.18 | 0.223 | False |
| 2026-07-17 17:10 | 5000 | -17.14 | 0.489 | -10.07 | 0.217 | False |
| 2026-07-17 20:53 | 5000 | -17.14 | 0.489 | -11.5 | 0.121 | False |
| 2026-07-18 02:24 | 5000 | -17.79 | 0.478 | -11.12 | 0.125 | False |
| 2026-07-18 06:04 | 5000 | -17.4 | 0.488 | -11.12 | 0.125 | False |

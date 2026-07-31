# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-31 06:42_

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

- Current-params net profit (full sample): **-16.43%**, PF 0.365, 73 trades, max DD -1667.18
- Optimizer out-of-sample: net **-8.93%**, PF 0.177, 28 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-29 17:13 | 5000 | -15.79 | 0.395 | -5.79 | 0.376 | False |
| 2026-07-29 20:54 | 5000 | -15.79 | 0.395 | -6.95 | 0.241 | False |
| 2026-07-30 02:13 | 5000 | -15.79 | 0.395 | -7.24 | 0.207 | False |
| 2026-07-30 06:26 | 5000 | -15.79 | 0.395 | -7.58 | 0.216 | False |
| 2026-07-30 10:23 | 5000 | -15.86 | 0.394 | -7.62 | 0.216 | False |
| 2026-07-30 13:57 | 5000 | -15.83 | 0.395 | -8.51 | 0.194 | False |
| 2026-07-30 17:25 | 5000 | -15.75 | 0.397 | -7.18 | 0.212 | False |
| 2026-07-30 21:08 | 5000 | -15.75 | 0.397 | -6.5 | 0.231 | False |
| 2026-07-31 02:42 | 5000 | -15.76 | 0.396 | -6.5 | 0.231 | False |
| 2026-07-31 06:42 | 5000 | -16.43 | 0.365 | -8.93 | 0.177 | False |

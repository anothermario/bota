# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-01 13:17_

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

- Current-params net profit (full sample): **-15.79%**, PF 0.389, 73 trades, max DD -1609.18
- Optimizer out-of-sample: net **-7.04%**, PF 0.251, 27 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-31 02:42 | 5000 | -15.76 | 0.396 | -6.5 | 0.231 | False |
| 2026-07-31 06:42 | 5000 | -16.43 | 0.365 | -8.93 | 0.177 | False |
| 2026-07-31 10:37 | 5000 | -16.6 | 0.359 | -6.99 | 0.237 | False |
| 2026-07-31 14:02 | 5000 | -16.6 | 0.359 | -6.99 | 0.237 | False |
| 2026-07-31 17:27 | 5000 | -15.91 | 0.386 | -5.98 | 0.331 | False |
| 2026-07-31 21:02 | 5000 | -16.4 | 0.378 | -6.52 | 0.311 | False |
| 2026-08-01 02:41 | 5000 | -16.39 | 0.378 | -6.52 | 0.311 | False |
| 2026-08-01 06:28 | 5000 | -16.39 | 0.378 | -6.95 | 0.296 | False |
| 2026-08-01 09:57 | 5000 | -15.79 | 0.389 | -7.01 | 0.255 | False |
| 2026-08-01 13:17 | 5000 | -15.79 | 0.389 | -7.04 | 0.251 | False |

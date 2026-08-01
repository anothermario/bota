# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-01 06:28_

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

- Current-params net profit (full sample): **-16.39%**, PF 0.378, 74 trades, max DD -1663.72
- Optimizer out-of-sample: net **-6.95%**, PF 0.296, 29 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-30 17:25 | 5000 | -15.75 | 0.397 | -7.18 | 0.212 | False |
| 2026-07-30 21:08 | 5000 | -15.75 | 0.397 | -6.5 | 0.231 | False |
| 2026-07-31 02:42 | 5000 | -15.76 | 0.396 | -6.5 | 0.231 | False |
| 2026-07-31 06:42 | 5000 | -16.43 | 0.365 | -8.93 | 0.177 | False |
| 2026-07-31 10:37 | 5000 | -16.6 | 0.359 | -6.99 | 0.237 | False |
| 2026-07-31 14:02 | 5000 | -16.6 | 0.359 | -6.99 | 0.237 | False |
| 2026-07-31 17:27 | 5000 | -15.91 | 0.386 | -5.98 | 0.331 | False |
| 2026-07-31 21:02 | 5000 | -16.4 | 0.378 | -6.52 | 0.311 | False |
| 2026-08-01 02:41 | 5000 | -16.39 | 0.378 | -6.52 | 0.311 | False |
| 2026-08-01 06:28 | 5000 | -16.39 | 0.378 | -6.95 | 0.296 | False |

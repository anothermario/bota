# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-11-12 08:10_

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
  "atr_mult": 3.0,
  "chand_len": 18,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-19.76%**, PF 0.236, 75 trades, max DD -1986.89
- Optimizer out-of-sample: net **-7.76%**, PF 0.193, 24 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-10 20:07 | 5000 | -17.49 | 0.333 | -7.51 | 0.218 | False |
| 2026-11-11 00:19 | 5000 | -17.1 | 0.339 | -7.51 | 0.218 | False |
| 2026-11-11 04:08 | 5000 | -17.1 | 0.339 | -8.09 | 0.204 | False |
| 2026-11-11 08:09 | 5000 | -17.1 | 0.339 | -8.09 | 0.204 | False |
| 2026-11-11 12:11 | 5000 | -16.89 | 0.342 | -7.64 | 0.215 | False |
| 2026-11-11 16:07 | 5000 | -16.89 | 0.342 | -8.11 | 0.204 | False |
| 2026-11-11 20:07 | 5000 | -16.88 | 0.342 | -8.08 | 0.204 | False |
| 2026-11-12 00:19 | 5000 | -16.91 | 0.343 | -7.54 | 0.218 | False |
| 2026-11-12 04:08 | 5000 | -19.76 | 0.236 | -7.76 | 0.193 | False |
| 2026-11-12 08:10 | 5000 | -19.76 | 0.236 | -7.76 | 0.193 | False |

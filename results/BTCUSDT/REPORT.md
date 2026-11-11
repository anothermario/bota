# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-11-11 20:07_

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

- Current-params net profit (full sample): **-16.88%**, PF 0.342, 74 trades, max DD -1953.48
- Optimizer out-of-sample: net **-8.08%**, PF 0.204, 26 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-10 08:10 | 5000 | -18.34 | 0.32 | -7.74 | 0.212 | False |
| 2026-11-10 12:10 | 5000 | -17.85 | 0.327 | -7.06 | 0.229 | False |
| 2026-11-10 16:08 | 5000 | -17.5 | 0.333 | -7.06 | 0.229 | False |
| 2026-11-10 20:07 | 5000 | -17.49 | 0.333 | -7.51 | 0.218 | False |
| 2026-11-11 00:19 | 5000 | -17.1 | 0.339 | -7.51 | 0.218 | False |
| 2026-11-11 04:08 | 5000 | -17.1 | 0.339 | -8.09 | 0.204 | False |
| 2026-11-11 08:09 | 5000 | -17.1 | 0.339 | -8.09 | 0.204 | False |
| 2026-11-11 12:11 | 5000 | -16.89 | 0.342 | -7.64 | 0.215 | False |
| 2026-11-11 16:07 | 5000 | -16.89 | 0.342 | -8.11 | 0.204 | False |
| 2026-11-11 20:07 | 5000 | -16.88 | 0.342 | -8.08 | 0.204 | False |

# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-11-13 12:10_

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

- Current-params net profit (full sample): **-17.86%**, PF 0.294, 75 trades, max DD -1931.41
- Optimizer out-of-sample: net **-2.62%**, PF 0.718, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-12 00:19 | 5000 | -16.91 | 0.343 | -7.54 | 0.218 | False |
| 2026-11-12 04:08 | 5000 | -19.76 | 0.236 | -7.76 | 0.193 | False |
| 2026-11-12 08:10 | 5000 | -19.76 | 0.236 | -7.76 | 0.193 | False |
| 2026-11-12 12:10 | 5000 | -20.53 | 0.224 | -7.76 | 0.193 | False |
| 2026-11-12 16:08 | 5000 | -19.88 | 0.232 | -7.31 | 0.203 | False |
| 2026-11-12 20:07 | 5000 | -19.65 | 0.239 | -7.75 | 0.193 | False |
| 2026-11-13 00:19 | 5000 | -19.09 | 0.246 | -6.89 | 0.214 | False |
| 2026-11-13 04:08 | 5000 | -19.11 | 0.246 | -7.34 | 0.202 | False |
| 2026-11-13 08:09 | 5000 | -17.86 | 0.294 | -2.24 | 0.749 | False |
| 2026-11-13 12:10 | 5000 | -17.86 | 0.294 | -2.62 | 0.718 | False |

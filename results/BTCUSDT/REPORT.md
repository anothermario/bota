# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-11-14 12:09_

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

- Current-params net profit (full sample): **-18.53%**, PF 0.273, 75 trades, max DD -1931.29
- Optimizer out-of-sample: net **-1.12%**, PF 0.859, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-13 00:19 | 5000 | -19.09 | 0.246 | -6.89 | 0.214 | False |
| 2026-11-13 04:08 | 5000 | -19.11 | 0.246 | -7.34 | 0.202 | False |
| 2026-11-13 08:09 | 5000 | -17.86 | 0.294 | -2.24 | 0.749 | False |
| 2026-11-13 12:10 | 5000 | -17.86 | 0.294 | -2.62 | 0.718 | False |
| 2026-11-13 16:07 | 5000 | -18.37 | 0.288 | -2.38 | 0.738 | False |
| 2026-11-13 20:07 | 5000 | -18.37 | 0.288 | -2.09 | 0.763 | False |
| 2026-11-14 00:18 | 5000 | -18.37 | 0.288 | -2.08 | 0.764 | False |
| 2026-11-14 04:08 | 5000 | -18.41 | 0.288 | -1.72 | 0.8 | False |
| 2026-11-14 08:08 | 5000 | -18.14 | 0.292 | -1.19 | 0.851 | False |
| 2026-11-14 12:09 | 5000 | -18.53 | 0.273 | -1.12 | 0.859 | False |

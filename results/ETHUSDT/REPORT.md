# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-03 20:10_

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

- Current-params net profit (full sample): **-17.37%**, PF 0.345, 97 trades, max DD -1767.15
- Optimizer out-of-sample: net **-6.82%**, PF 0.05, 24 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-02 08:16 | 5000 | -19.5 | 0.313 | -6.27 | 0.053 | False |
| 2026-09-02 12:18 | 5000 | -19.2 | 0.317 | -6.77 | 0.05 | False |
| 2026-09-02 16:13 | 5000 | -19.67 | 0.311 | -7.15 | 0.047 | False |
| 2026-09-02 20:11 | 5000 | -19.09 | 0.319 | -7.15 | 0.047 | False |
| 2026-09-03 00:32 | 5000 | -18.38 | 0.329 | -6.79 | 0.05 | False |
| 2026-09-03 05:15 | 5000 | -18.42 | 0.328 | -6.79 | 0.049 | False |
| 2026-09-03 08:16 | 5000 | -18.31 | 0.33 | -6.79 | 0.05 | False |
| 2026-09-03 12:18 | 5000 | -18.04 | 0.334 | -6.79 | 0.05 | False |
| 2026-09-03 16:12 | 5000 | -17.37 | 0.345 | -6.83 | 0.049 | False |
| 2026-09-03 20:10 | 5000 | -17.37 | 0.345 | -6.82 | 0.05 | False |

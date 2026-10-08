# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-10-08 08:18_

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

- Current-params net profit (full sample): **-10.75%**, PF 0.552, 67 trades, max DD -1349.8
- Optimizer out-of-sample: net **-8.85%**, PF 0.178, 32 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-06 20:12 | 5000 | -10.27 | 0.564 | -8.66 | 0.192 | False |
| 2026-10-07 00:34 | 5000 | -10.38 | 0.561 | -8.7 | 0.187 | False |
| 2026-10-07 04:14 | 5000 | -10.56 | 0.557 | -9.01 | 0.191 | False |
| 2026-10-07 08:17 | 5000 | -10.73 | 0.553 | -9.0 | 0.191 | False |
| 2026-10-07 12:19 | 5000 | -10.65 | 0.553 | -9.0 | 0.191 | False |
| 2026-10-07 16:13 | 5000 | -10.82 | 0.55 | -7.96 | 0.213 | False |
| 2026-10-07 20:13 | 5000 | -10.82 | 0.55 | -7.96 | 0.213 | False |
| 2026-10-08 00:33 | 5000 | -11.2 | 0.54 | -8.2 | 0.211 | False |
| 2026-10-08 04:15 | 5000 | -10.75 | 0.552 | -8.21 | 0.211 | False |
| 2026-10-08 08:18 | 5000 | -10.75 | 0.552 | -8.85 | 0.178 | False |

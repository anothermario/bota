# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-10-09 08:18_

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

- Current-params net profit (full sample): **-11.95%**, PF 0.514, 68 trades, max DD -1363.13
- Optimizer out-of-sample: net **-8.05%**, PF 0.178, 33 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-07 20:13 | 5000 | -10.82 | 0.55 | -7.96 | 0.213 | False |
| 2026-10-08 00:33 | 5000 | -11.2 | 0.54 | -8.2 | 0.211 | False |
| 2026-10-08 04:15 | 5000 | -10.75 | 0.552 | -8.21 | 0.211 | False |
| 2026-10-08 08:18 | 5000 | -10.75 | 0.552 | -8.85 | 0.178 | False |
| 2026-10-08 12:18 | 5000 | -11.57 | 0.521 | -8.84 | 0.178 | False |
| 2026-10-08 16:14 | 5000 | -11.23 | 0.53 | -8.39 | 0.188 | False |
| 2026-10-08 20:12 | 5000 | -11.45 | 0.525 | -9.01 | 0.176 | False |
| 2026-10-09 00:35 | 5000 | -11.45 | 0.525 | -8.07 | 0.178 | False |
| 2026-10-09 04:16 | 5000 | -11.95 | 0.514 | -7.99 | 0.179 | False |
| 2026-10-09 08:18 | 5000 | -11.95 | 0.514 | -8.05 | 0.178 | False |

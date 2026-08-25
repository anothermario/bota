# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-25 08:16_

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

- Current-params net profit (full sample): **-11.61%**, PF 0.446, 76 trades, max DD -1187.3
- Optimizer out-of-sample: net **-1.24%**, PF 0.777, 24 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-23 20:04 | 5000 | -10.58 | 0.468 | -0.0 | 1.0 | False |
| 2026-08-24 00:14 | 5000 | -10.57 | 0.468 | -0.0 | 1.0 | False |
| 2026-08-24 04:17 | 5000 | -10.3 | 0.475 | -0.09 | 0.978 | False |
| 2026-08-24 08:17 | 5000 | -10.31 | 0.475 | 0.13 | 1.033 | True |
| 2026-08-24 12:10 | 5000 | -10.3 | 0.475 | 0.15 | 1.039 | True |
| 2026-08-24 16:11 | 5000 | -10.51 | 0.471 | -0.39 | 0.916 | False |
| 2026-08-24 20:08 | 5000 | -11.11 | 0.457 | -0.8 | 0.844 | False |
| 2026-08-25 00:14 | 5000 | -11.11 | 0.457 | -0.68 | 0.864 | False |
| 2026-08-25 04:15 | 5000 | -11.13 | 0.457 | -0.7 | 0.864 | False |
| 2026-08-25 08:16 | 5000 | -11.61 | 0.446 | -1.24 | 0.777 | False |

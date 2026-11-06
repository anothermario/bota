# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-11-06 12:10_

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

- Current-params net profit (full sample): **-15.17%**, PF 0.411, 77 trades, max DD -1775.78
- Optimizer out-of-sample: net **-10.89%**, PF 0.123, 35 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-05 00:19 | 5000 | -12.87 | 0.483 | -9.31 | 0.253 | False |
| 2026-11-05 04:08 | 5000 | -12.88 | 0.483 | -9.31 | 0.253 | False |
| 2026-11-05 08:11 | 5000 | -12.87 | 0.483 | -9.31 | 0.253 | False |
| 2026-11-05 12:10 | 5000 | -12.86 | 0.483 | -8.04 | 0.239 | False |
| 2026-11-05 16:09 | 5000 | -13.41 | 0.474 | -8.6 | 0.227 | False |
| 2026-11-05 20:07 | 5000 | -14.44 | 0.437 | -9.37 | 0.212 | False |
| 2026-11-06 00:20 | 5000 | -14.9 | 0.416 | -9.38 | 0.212 | False |
| 2026-11-06 04:08 | 5000 | -14.99 | 0.412 | -9.37 | 0.212 | False |
| 2026-11-06 08:10 | 5000 | -15.03 | 0.412 | -9.4 | 0.212 | False |
| 2026-11-06 12:10 | 5000 | -15.17 | 0.411 | -10.89 | 0.123 | False |

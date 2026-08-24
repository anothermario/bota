# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-24 16:11_

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

- Current-params net profit (full sample): **-10.51%**, PF 0.471, 74 trades, max DD -1184.43
- Optimizer out-of-sample: net **-0.39%**, PF 0.916, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-23 04:15 | 5000 | -10.17 | 0.476 | 1.01 | 1.336 | True |
| 2026-08-23 08:08 | 5000 | -10.64 | 0.464 | 0.97 | 1.336 | True |
| 2026-08-23 12:07 | 5000 | -10.33 | 0.474 | 0.28 | 1.087 | True |
| 2026-08-23 16:05 | 5000 | -10.58 | 0.468 | -0.0 | 1.0 | False |
| 2026-08-23 20:04 | 5000 | -10.58 | 0.468 | -0.0 | 1.0 | False |
| 2026-08-24 00:14 | 5000 | -10.57 | 0.468 | -0.0 | 1.0 | False |
| 2026-08-24 04:17 | 5000 | -10.3 | 0.475 | -0.09 | 0.978 | False |
| 2026-08-24 08:17 | 5000 | -10.31 | 0.475 | 0.13 | 1.033 | True |
| 2026-08-24 12:10 | 5000 | -10.3 | 0.475 | 0.15 | 1.039 | True |
| 2026-08-24 16:11 | 5000 | -10.51 | 0.471 | -0.39 | 0.916 | False |

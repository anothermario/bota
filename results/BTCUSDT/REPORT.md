# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-23 12:07_

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

- Current-params net profit (full sample): **-10.33%**, PF 0.474, 74 trades, max DD -1212.29
- Optimizer out-of-sample: net **0.28%**, PF 1.087, 22 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-22 00:14 | 5000 | -9.72 | 0.502 | 0.64 | 1.19 | True |
| 2026-08-22 04:13 | 5000 | -9.72 | 0.502 | 0.64 | 1.19 | True |
| 2026-08-22 08:07 | 5000 | -9.73 | 0.501 | 1.02 | 1.338 | True |
| 2026-08-22 12:07 | 5000 | -10.18 | 0.476 | 1.18 | 1.39 | True |
| 2026-08-22 16:04 | 5000 | -10.18 | 0.476 | 1.17 | 1.388 | True |
| 2026-08-22 20:05 | 5000 | -10.18 | 0.476 | 1.01 | 1.336 | True |
| 2026-08-23 00:14 | 5000 | -10.18 | 0.476 | 1.01 | 1.336 | True |
| 2026-08-23 04:15 | 5000 | -10.17 | 0.476 | 1.01 | 1.336 | True |
| 2026-08-23 08:08 | 5000 | -10.64 | 0.464 | 0.97 | 1.336 | True |
| 2026-08-23 12:07 | 5000 | -10.33 | 0.474 | 0.28 | 1.087 | True |

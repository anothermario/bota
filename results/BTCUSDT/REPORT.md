# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-11-01 00:23_

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

- Current-params net profit (full sample): **-11.58%**, PF 0.497, 72 trades, max DD -1227.84
- Optimizer out-of-sample: net **-5.14%**, PF 0.388, 24 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-30 12:13 | 5000 | -12.95 | 0.465 | -5.92 | 0.353 | False |
| 2026-10-30 16:08 | 5000 | -13.31 | 0.457 | -6.72 | 0.358 | False |
| 2026-10-30 20:06 | 5000 | -13.28 | 0.458 | -6.67 | 0.36 | False |
| 2026-10-31 00:18 | 5000 | -12.43 | 0.476 | -5.15 | 0.387 | False |
| 2026-10-31 04:08 | 5000 | -12.2 | 0.482 | -5.15 | 0.387 | False |
| 2026-10-31 08:08 | 5000 | -12.2 | 0.482 | -5.15 | 0.387 | False |
| 2026-10-31 12:09 | 5000 | -12.2 | 0.482 | -5.15 | 0.387 | False |
| 2026-10-31 16:07 | 5000 | -12.23 | 0.481 | -5.6 | 0.366 | False |
| 2026-10-31 20:06 | 5000 | -11.58 | 0.497 | -5.15 | 0.388 | False |
| 2026-11-01 00:23 | 5000 | -11.58 | 0.497 | -5.14 | 0.388 | False |

# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-10-30 20:06_

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

- Current-params net profit (full sample): **-13.28%**, PF 0.458, 76 trades, max DD -1339.56
- Optimizer out-of-sample: net **-6.67%**, PF 0.36, 34 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-29 08:11 | 5000 | -12.81 | 0.463 | -4.24 | 0.468 | False |
| 2026-10-29 12:13 | 5000 | -12.33 | 0.474 | -4.24 | 0.468 | False |
| 2026-10-29 16:09 | 5000 | -12.37 | 0.474 | -3.85 | 0.523 | False |
| 2026-10-29 20:08 | 5000 | -12.9 | 0.462 | -4.43 | 0.486 | False |
| 2026-10-30 00:23 | 5000 | -13.53 | 0.451 | -6.04 | 0.342 | False |
| 2026-10-30 04:10 | 5000 | -12.95 | 0.465 | -5.92 | 0.353 | False |
| 2026-10-30 08:11 | 5000 | -12.95 | 0.465 | -5.92 | 0.353 | False |
| 2026-10-30 12:13 | 5000 | -12.95 | 0.465 | -5.92 | 0.353 | False |
| 2026-10-30 16:08 | 5000 | -13.31 | 0.457 | -6.72 | 0.358 | False |
| 2026-10-30 20:06 | 5000 | -13.28 | 0.458 | -6.67 | 0.36 | False |

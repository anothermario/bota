# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-11-02 20:06_

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

- Current-params net profit (full sample): **-11.25%**, PF 0.507, 72 trades, max DD -1284.32
- Optimizer out-of-sample: net **-6.19%**, PF 0.386, 34 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-01 04:08 | 5000 | -11.57 | 0.497 | -4.51 | 0.421 | False |
| 2026-11-01 08:08 | 5000 | -11.27 | 0.505 | -4.77 | 0.409 | False |
| 2026-11-01 12:10 | 5000 | -11.34 | 0.503 | -4.83 | 0.404 | False |
| 2026-11-01 16:07 | 5000 | -11.34 | 0.503 | -4.63 | 0.415 | False |
| 2026-11-01 20:06 | 5000 | -11.34 | 0.503 | -4.81 | 0.405 | False |
| 2026-11-02 00:20 | 5000 | -11.34 | 0.503 | -4.63 | 0.415 | False |
| 2026-11-02 04:09 | 5000 | -11.38 | 0.503 | -4.67 | 0.415 | False |
| 2026-11-02 08:11 | 5000 | -11.75 | 0.494 | -5.34 | 0.381 | False |
| 2026-11-02 12:11 | 5000 | -11.21 | 0.507 | -6.81 | 0.36 | False |
| 2026-11-02 20:06 | 5000 | -11.25 | 0.507 | -6.19 | 0.386 | False |

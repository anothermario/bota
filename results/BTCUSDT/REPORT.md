# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-11-03 16:08_

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

- Current-params net profit (full sample): **-12.71%**, PF 0.476, 74 trades, max DD -1453.36
- Optimizer out-of-sample: net **-9.2%**, PF 0.209, 35 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-02 00:20 | 5000 | -11.34 | 0.503 | -4.63 | 0.415 | False |
| 2026-11-02 04:09 | 5000 | -11.38 | 0.503 | -4.67 | 0.415 | False |
| 2026-11-02 08:11 | 5000 | -11.75 | 0.494 | -5.34 | 0.381 | False |
| 2026-11-02 12:11 | 5000 | -11.21 | 0.507 | -6.81 | 0.36 | False |
| 2026-11-02 20:06 | 5000 | -11.25 | 0.507 | -6.19 | 0.386 | False |
| 2026-11-03 00:19 | 5000 | -11.25 | 0.507 | -4.92 | 0.395 | False |
| 2026-11-03 04:08 | 5000 | -11.77 | 0.495 | -5.41 | 0.371 | False |
| 2026-11-03 08:10 | 5000 | -12.45 | 0.481 | -7.8 | 0.309 | False |
| 2026-11-03 12:10 | 5000 | -12.45 | 0.481 | -8.81 | 0.217 | False |
| 2026-11-03 16:08 | 5000 | -12.71 | 0.476 | -9.2 | 0.209 | False |

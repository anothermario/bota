# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-10-11 08:15_

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

- Current-params net profit (full sample): **-11.68%**, PF 0.496, 63 trades, max DD -1361.95
- Optimizer out-of-sample: net **-4.47%**, PF 0.392, 30 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-09 20:12 | 5000 | -11.12 | 0.538 | -6.78 | 0.24 | False |
| 2026-10-10 00:34 | 5000 | -10.82 | 0.546 | -5.79 | 0.272 | False |
| 2026-10-10 04:14 | 5000 | -10.82 | 0.546 | -6.63 | 0.22 | False |
| 2026-10-10 08:14 | 5000 | -11.46 | 0.516 | -5.48 | 0.341 | False |
| 2026-10-10 12:16 | 5000 | -11.72 | 0.495 | -4.95 | 0.365 | False |
| 2026-10-10 16:12 | 5000 | -11.72 | 0.495 | -5.02 | 0.361 | False |
| 2026-10-10 20:11 | 5000 | -11.71 | 0.495 | -4.83 | 0.373 | False |
| 2026-10-11 00:37 | 5000 | -11.71 | 0.495 | -4.17 | 0.408 | False |
| 2026-10-11 04:14 | 5000 | -12.3 | 0.481 | -4.36 | 0.399 | False |
| 2026-10-11 08:15 | 5000 | -11.68 | 0.496 | -4.47 | 0.392 | False |

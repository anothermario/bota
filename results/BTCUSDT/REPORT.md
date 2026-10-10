# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-10-10 08:14_

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

- Current-params net profit (full sample): **-11.46%**, PF 0.516, 67 trades, max DD -1365.36
- Optimizer out-of-sample: net **-5.48%**, PF 0.341, 30 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-08 20:12 | 5000 | -11.45 | 0.525 | -9.01 | 0.176 | False |
| 2026-10-09 00:35 | 5000 | -11.45 | 0.525 | -8.07 | 0.178 | False |
| 2026-10-09 04:16 | 5000 | -11.95 | 0.514 | -7.99 | 0.179 | False |
| 2026-10-09 08:18 | 5000 | -11.95 | 0.514 | -8.05 | 0.178 | False |
| 2026-10-09 12:17 | 5000 | -11.48 | 0.525 | -7.56 | 0.188 | False |
| 2026-10-09 16:12 | 5000 | -11.15 | 0.538 | -6.42 | 0.307 | False |
| 2026-10-09 20:12 | 5000 | -11.12 | 0.538 | -6.78 | 0.24 | False |
| 2026-10-10 00:34 | 5000 | -10.82 | 0.546 | -5.79 | 0.272 | False |
| 2026-10-10 04:14 | 5000 | -10.82 | 0.546 | -6.63 | 0.22 | False |
| 2026-10-10 08:14 | 5000 | -11.46 | 0.516 | -5.48 | 0.341 | False |

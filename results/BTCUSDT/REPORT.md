# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-16 20:56_

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

- Current-params net profit (full sample): **-9.42%**, PF 0.628, 67 trades, max DD -1333.91
- Optimizer out-of-sample: net **-5.96%**, PF 0.303, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-15 10:01 | 5000 | -7.27 | 0.692 | -3.05 | 0.547 | False |
| 2026-07-15 13:41 | 5000 | -7.3 | 0.692 | -4.07 | 0.395 | False |
| 2026-07-15 17:16 | 5000 | -7.95 | 0.673 | -4.74 | 0.358 | False |
| 2026-07-15 20:58 | 5000 | -7.95 | 0.673 | -4.78 | 0.352 | False |
| 2026-07-16 02:30 | 5000 | -7.99 | 0.673 | -4.81 | 0.352 | False |
| 2026-07-16 06:16 | 5000 | -8.43 | 0.66 | -5.83 | 0.307 | False |
| 2026-07-16 10:07 | 5000 | -8.46 | 0.66 | -5.3 | 0.33 | False |
| 2026-07-16 13:47 | 5000 | -9.09 | 0.643 | -5.94 | 0.304 | False |
| 2026-07-16 17:14 | 5000 | -9.55 | 0.625 | -5.95 | 0.304 | False |
| 2026-07-16 20:56 | 5000 | -9.42 | 0.628 | -5.96 | 0.303 | False |

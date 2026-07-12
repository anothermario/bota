# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-12 02:39_

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

- Current-params net profit (full sample): **-7.69%**, PF 0.686, 68 trades, max DD -1139.92
- Optimizer out-of-sample: net **-2.97%**, PF 0.424, 18 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-10 14:24 | 5000 | -7.33 | 0.696 | -5.49 | 0.279 | False |
| 2026-07-10 17:47 | 5000 | -7.33 | 0.696 | -4.75 | 0.31 | False |
| 2026-07-10 21:05 | 5000 | -7.33 | 0.696 | -4.7 | 0.313 | False |
| 2026-07-11 02:32 | 5000 | -7.46 | 0.692 | -3.65 | 0.372 | False |
| 2026-07-11 06:12 | 5000 | -7.16 | 0.701 | -3.57 | 0.377 | False |
| 2026-07-11 09:28 | 5000 | -7.16 | 0.701 | -3.57 | 0.377 | False |
| 2026-07-11 13:16 | 5000 | -7.16 | 0.701 | -3.57 | 0.377 | False |
| 2026-07-11 16:57 | 5000 | -7.16 | 0.701 | -3.0 | 0.421 | False |
| 2026-07-11 20:45 | 5000 | -7.16 | 0.701 | -2.43 | 0.474 | False |
| 2026-07-12 02:39 | 5000 | -7.69 | 0.686 | -2.97 | 0.424 | False |

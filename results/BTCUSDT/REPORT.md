# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-26 16:29_

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

- Current-params net profit (full sample): **-11.5%**, PF 0.442, 74 trades, max DD -1150.05
- Optimizer out-of-sample: net **-1.89%**, PF 0.657, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-25 04:15 | 5000 | -11.13 | 0.457 | -0.7 | 0.864 | False |
| 2026-08-25 08:16 | 5000 | -11.61 | 0.446 | -1.24 | 0.777 | False |
| 2026-08-25 12:10 | 5000 | -12.24 | 0.424 | -1.24 | 0.777 | False |
| 2026-08-25 16:13 | 5000 | -11.84 | 0.433 | -1.11 | 0.8 | False |
| 2026-08-25 20:07 | 5000 | -11.85 | 0.433 | -1.11 | 0.8 | False |
| 2026-08-26 00:14 | 5000 | -11.49 | 0.442 | -2.24 | 0.617 | False |
| 2026-08-26 04:15 | 5000 | -11.49 | 0.442 | -1.88 | 0.658 | False |
| 2026-08-26 08:16 | 5000 | -11.49 | 0.442 | -1.88 | 0.658 | False |
| 2026-08-26 12:11 | 5000 | -11.32 | 0.451 | -1.88 | 0.658 | False |
| 2026-08-26 16:29 | 5000 | -11.5 | 0.442 | -1.89 | 0.657 | False |

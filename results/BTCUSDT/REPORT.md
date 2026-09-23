# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-23 04:13_

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

- Current-params net profit (full sample): **-6.36%**, PF 0.673, 67 trades, max DD -904.87
- Optimizer out-of-sample: net **-2.16%**, PF 0.722, 24 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-21 16:12 | 5000 | -7.62 | 0.599 | -4.57 | 0.402 | False |
| 2026-09-21 20:11 | 5000 | -7.84 | 0.592 | -4.57 | 0.402 | False |
| 2026-09-22 00:30 | 5000 | -5.58 | 0.706 | -2.01 | 0.735 | False |
| 2026-09-22 04:13 | 5000 | -5.58 | 0.706 | -2.01 | 0.735 | False |
| 2026-09-22 08:16 | 5000 | -5.61 | 0.706 | -2.05 | 0.735 | False |
| 2026-09-22 12:16 | 5000 | -6.76 | 0.658 | -3.03 | 0.647 | False |
| 2026-09-22 16:11 | 5000 | -6.64 | 0.663 | -2.7 | 0.674 | False |
| 2026-09-22 20:10 | 5000 | -6.53 | 0.667 | -2.7 | 0.674 | False |
| 2026-09-23 00:28 | 5000 | -6.36 | 0.673 | -2.16 | 0.722 | False |
| 2026-09-23 04:13 | 5000 | -6.36 | 0.673 | -2.16 | 0.722 | False |

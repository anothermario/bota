# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-18 00:30_

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
  "chand_len": 26,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-4.76%**, PF 0.772, 52 trades, max DD -791.42
- Optimizer out-of-sample: net **-2.79%**, PF 0.662, 18 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-16 12:17 | 5000 | -4.45 | 0.783 | -2.17 | 0.714 | False |
| 2026-09-16 16:13 | 5000 | -4.45 | 0.783 | -2.77 | 0.662 | False |
| 2026-09-16 20:12 | 5000 | -4.45 | 0.783 | -2.77 | 0.662 | False |
| 2026-09-17 00:30 | 5000 | -5.05 | 0.76 | -2.92 | 0.644 | False |
| 2026-09-17 04:14 | 5000 | -5.05 | 0.76 | -2.92 | 0.644 | False |
| 2026-09-17 08:16 | 5000 | -4.62 | 0.776 | -3.61 | 0.592 | False |
| 2026-09-17 12:17 | 5000 | -3.25 | 0.841 | -2.72 | 0.668 | False |
| 2026-09-17 16:13 | 5000 | -4.13 | 0.804 | -2.79 | 0.662 | False |
| 2026-09-17 20:12 | 5000 | -4.76 | 0.772 | -2.79 | 0.662 | False |
| 2026-09-18 00:30 | 5000 | -4.76 | 0.772 | -2.79 | 0.662 | False |

# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-17 08:16_

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

- Current-params net profit (full sample): **-4.62%**, PF 0.776, 53 trades, max DD -716.03
- Optimizer out-of-sample: net **-3.61%**, PF 0.592, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-15 20:12 | 5000 | -4.2 | 0.806 | -2.77 | 0.662 | False |
| 2026-09-16 00:30 | 5000 | -5.47 | 0.744 | -2.77 | 0.662 | False |
| 2026-09-16 04:13 | 5000 | -5.47 | 0.744 | -2.17 | 0.714 | False |
| 2026-09-16 08:16 | 5000 | -5.32 | 0.749 | -2.17 | 0.714 | False |
| 2026-09-16 12:17 | 5000 | -4.45 | 0.783 | -2.17 | 0.714 | False |
| 2026-09-16 16:13 | 5000 | -4.45 | 0.783 | -2.77 | 0.662 | False |
| 2026-09-16 20:12 | 5000 | -4.45 | 0.783 | -2.77 | 0.662 | False |
| 2026-09-17 00:30 | 5000 | -5.05 | 0.76 | -2.92 | 0.644 | False |
| 2026-09-17 04:14 | 5000 | -5.05 | 0.76 | -2.92 | 0.644 | False |
| 2026-09-17 08:16 | 5000 | -4.62 | 0.776 | -3.61 | 0.592 | False |

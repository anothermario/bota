# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-02 00:33_

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

- Current-params net profit (full sample): **-3.78%**, PF 0.839, 58 trades, max DD -1132.15
- Optimizer out-of-sample: net **-3.9%**, PF 0.498, 18 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-30 12:21 | 5000 | -3.54 | 0.848 | -4.35 | 0.468 | False |
| 2026-09-30 16:14 | 5000 | -3.54 | 0.848 | -3.91 | 0.496 | False |
| 2026-09-30 20:14 | 5000 | -3.55 | 0.848 | -3.91 | 0.497 | False |
| 2026-10-01 00:38 | 5000 | -3.42 | 0.853 | -3.45 | 0.529 | False |
| 2026-10-01 04:15 | 5000 | -3.57 | 0.847 | -3.61 | 0.519 | False |
| 2026-10-01 08:17 | 5000 | -3.87 | 0.836 | -3.9 | 0.498 | False |
| 2026-10-01 12:19 | 5000 | -3.78 | 0.839 | -3.9 | 0.498 | False |
| 2026-10-01 16:13 | 5000 | -3.78 | 0.839 | -3.9 | 0.498 | False |
| 2026-10-01 20:13 | 5000 | -3.78 | 0.839 | -3.9 | 0.498 | False |
| 2026-10-02 00:33 | 5000 | -3.78 | 0.839 | -3.9 | 0.498 | False |

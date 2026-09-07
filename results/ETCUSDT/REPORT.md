# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-07 16:12_

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

- Current-params net profit (full sample): **-2.86%**, PF 0.86, 52 trades, max DD -632.64
- Optimizer out-of-sample: net **-4.3%**, PF 0.385, 15 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-06 04:13 | 5000 | -3.27 | 0.842 | -0.4 | 0.942 | False |
| 2026-09-06 08:13 | 5000 | -3.27 | 0.842 | -4.31 | 0.384 | False |
| 2026-09-06 12:15 | 5000 | -3.27 | 0.842 | -3.88 | 0.41 | False |
| 2026-09-06 16:10 | 5000 | -3.84 | 0.819 | -3.88 | 0.41 | False |
| 2026-09-06 20:10 | 5000 | -3.27 | 0.842 | -3.88 | 0.41 | False |
| 2026-09-07 00:33 | 5000 | -2.47 | 0.879 | -3.91 | 0.41 | False |
| 2026-09-07 04:14 | 5000 | -2.86 | 0.86 | -4.3 | 0.385 | False |
| 2026-09-07 08:18 | 5000 | -2.86 | 0.86 | -4.3 | 0.385 | False |
| 2026-09-07 12:17 | 5000 | -2.86 | 0.86 | -4.3 | 0.385 | False |
| 2026-09-07 16:12 | 5000 | -2.86 | 0.86 | -4.3 | 0.385 | False |

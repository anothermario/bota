# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-06 12:18_

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

- Current-params net profit (full sample): **-5.85%**, PF 0.77, 60 trades, max DD -1360.87
- Optimizer out-of-sample: net **-6.58%**, PF 0.232, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-04 20:47 | 5000 | -4.33 | 0.821 | -5.72 | 0.257 | False |
| 2026-10-05 00:36 | 5000 | -4.63 | 0.81 | -5.75 | 0.257 | False |
| 2026-10-05 04:19 | 5000 | -5.19 | 0.791 | -6.3 | 0.239 | False |
| 2026-10-05 08:25 | 5000 | -5.19 | 0.791 | -6.3 | 0.239 | False |
| 2026-10-05 12:19 | 5000 | -4.65 | 0.813 | -6.3 | 0.239 | False |
| 2026-10-05 16:14 | 5000 | -4.65 | 0.813 | -6.3 | 0.239 | False |
| 2026-10-06 00:33 | 5000 | -5.19 | 0.791 | -5.92 | 0.251 | False |
| 2026-10-06 04:14 | 5000 | -5.22 | 0.791 | -5.95 | 0.251 | False |
| 2026-10-06 08:16 | 5000 | -5.22 | 0.791 | -5.95 | 0.251 | False |
| 2026-10-06 12:18 | 5000 | -5.85 | 0.77 | -6.58 | 0.232 | False |

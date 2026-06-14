# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-06-14 05:38_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.3,
  "use_adx": true,
  "adx_len": 14,
  "adx_thresh": 20.0,
  "don_len": 20,
  "atr_len": 14,
  "atr_mult": 3.0,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-16.42%**, PF 0.428, 81 trades, max DD -1641.96
- Optimizer out-of-sample: net **-5.02%**, PF 0.232, 16 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-12 17:03 | 5000 | -13.99 | 0.527 | -6.16 | 0.196 | False |
| 2026-06-12 20:48 | 5000 | -13.96 | 0.528 | -6.96 | 0.194 | False |
| 2026-06-13 00:57 | 5000 | -15.16 | 0.48 | -6.06 | 0.199 | False |
| 2026-06-13 05:35 | 5000 | -15.57 | 0.469 | -5.89 | 0.203 | False |
| 2026-06-13 09:08 | 5000 | -15.32 | 0.474 | -5.88 | 0.203 | False |
| 2026-06-13 12:41 | 5000 | -15.36 | 0.472 | -5.93 | 0.202 | False |
| 2026-06-13 16:34 | 5000 | -16.19 | 0.438 | -5.49 | 0.216 | False |
| 2026-06-13 20:32 | 5000 | -16.65 | 0.424 | -5.49 | 0.216 | False |
| 2026-06-14 00:57 | 5000 | -16.42 | 0.428 | -5.02 | 0.232 | False |
| 2026-06-14 05:38 | 5000 | -16.42 | 0.428 | -5.02 | 0.232 | False |

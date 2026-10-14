# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-10-14 08:15_

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

- Current-params net profit (full sample): **-12.63%**, PF 0.443, 62 trades, max DD -1262.84
- Optimizer out-of-sample: net **-4.0%**, PF 0.265, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-12 20:12 | 5000 | -13.14 | 0.431 | -4.06 | 0.294 | False |
| 2026-10-13 00:35 | 5000 | -13.14 | 0.431 | -4.06 | 0.294 | False |
| 2026-10-13 04:18 | 5000 | -13.14 | 0.431 | -4.06 | 0.294 | False |
| 2026-10-13 08:20 | 5000 | -13.17 | 0.431 | -4.09 | 0.295 | False |
| 2026-10-13 12:19 | 5000 | -13.5 | 0.424 | -4.79 | 0.231 | False |
| 2026-10-13 16:13 | 5000 | -13.51 | 0.424 | -4.62 | 0.237 | False |
| 2026-10-13 20:12 | 5000 | -13.51 | 0.424 | -4.65 | 0.236 | False |
| 2026-10-14 00:27 | 5000 | -12.91 | 0.436 | -3.83 | 0.275 | False |
| 2026-10-14 04:14 | 5000 | -12.91 | 0.437 | -3.83 | 0.275 | False |
| 2026-10-14 08:15 | 5000 | -12.63 | 0.443 | -4.0 | 0.265 | False |

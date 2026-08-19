# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-19 08:12_

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
  "don_len": 15,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-13.08%**, PF 0.423, 57 trades, max DD -1434.79
- Optimizer out-of-sample: net **-2.64%**, PF 0.462, 14 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-17 20:07 | 5000 | -14.51 | 0.368 | -4.0 | 0.249 | False |
| 2026-08-18 00:14 | 5000 | -14.55 | 0.368 | -4.0 | 0.249 | False |
| 2026-08-18 04:15 | 5000 | -13.62 | 0.405 | -4.04 | 0.249 | False |
| 2026-08-18 08:11 | 5000 | -13.6 | 0.406 | -4.78 | 0.217 | False |
| 2026-08-18 12:09 | 5000 | -13.41 | 0.416 | -6.55 | 0.301 | False |
| 2026-08-18 16:08 | 5000 | -14.59 | 0.393 | -3.06 | 0.425 | False |
| 2026-08-18 20:06 | 5000 | -13.88 | 0.406 | -3.06 | 0.425 | False |
| 2026-08-19 00:13 | 5000 | -13.08 | 0.423 | -2.5 | 0.477 | False |
| 2026-08-19 04:15 | 5000 | -13.08 | 0.423 | -2.52 | 0.475 | False |
| 2026-08-19 08:12 | 5000 | -13.08 | 0.423 | -2.64 | 0.462 | False |

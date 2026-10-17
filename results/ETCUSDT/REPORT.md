# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-17 00:28_

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

- Current-params net profit (full sample): **-14.91%**, PF 0.439, 66 trades, max DD -1490.53
- Optimizer out-of-sample: net **-5.2%**, PF 0.38, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-15 12:17 | 5000 | -14.96 | 0.435 | -5.41 | 0.359 | False |
| 2026-10-15 16:12 | 5000 | -14.97 | 0.435 | -5.42 | 0.359 | False |
| 2026-10-15 20:10 | 5000 | -15.0 | 0.434 | -5.42 | 0.359 | False |
| 2026-10-16 00:28 | 5000 | -14.23 | 0.451 | -5.26 | 0.376 | False |
| 2026-10-16 04:13 | 5000 | -14.23 | 0.451 | -5.12 | 0.383 | False |
| 2026-10-16 08:15 | 5000 | -14.23 | 0.451 | -5.12 | 0.383 | False |
| 2026-10-16 12:17 | 5000 | -14.23 | 0.451 | -4.81 | 0.399 | False |
| 2026-10-16 16:12 | 5000 | -13.83 | 0.46 | -4.81 | 0.399 | False |
| 2026-10-16 20:10 | 5000 | -13.84 | 0.46 | -4.83 | 0.399 | False |
| 2026-10-17 00:28 | 5000 | -14.91 | 0.439 | -5.2 | 0.38 | False |

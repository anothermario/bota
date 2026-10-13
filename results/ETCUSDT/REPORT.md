# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-13 08:21_

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

- Current-params net profit (full sample): **-12.52%**, PF 0.479, 61 trades, max DD -1404.93
- Optimizer out-of-sample: net **-4.88%**, PF 0.378, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-11 20:12 | 5000 | -7.14 | 0.716 | -7.32 | 0.149 | False |
| 2026-10-12 00:38 | 5000 | -9.81 | 0.611 | -7.99 | 0.138 | False |
| 2026-10-12 04:21 | 5000 | -9.8 | 0.611 | -7.36 | 0.149 | False |
| 2026-10-12 08:30 | 5000 | -9.79 | 0.611 | -7.36 | 0.149 | False |
| 2026-10-12 12:25 | 5000 | -9.55 | 0.622 | -7.36 | 0.149 | False |
| 2026-10-12 16:13 | 5000 | -11.99 | 0.513 | -9.3 | 0.123 | False |
| 2026-10-12 20:12 | 5000 | -14.87 | 0.399 | -9.32 | 0.123 | False |
| 2026-10-13 00:35 | 5000 | -14.05 | 0.415 | -7.38 | 0.149 | False |
| 2026-10-13 04:18 | 5000 | -12.5 | 0.479 | -4.87 | 0.378 | False |
| 2026-10-13 08:21 | 5000 | -12.52 | 0.479 | -4.88 | 0.378 | False |

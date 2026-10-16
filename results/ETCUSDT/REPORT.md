# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-16 04:13_

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

- Current-params net profit (full sample): **-14.23%**, PF 0.451, 65 trades, max DD -1437.63
- Optimizer out-of-sample: net **-5.12%**, PF 0.383, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-14 16:12 | 5000 | -13.72 | 0.456 | -5.39 | 0.357 | False |
| 2026-10-14 20:11 | 5000 | -14.38 | 0.444 | -5.38 | 0.359 | False |
| 2026-10-15 00:29 | 5000 | -14.38 | 0.444 | -4.77 | 0.389 | False |
| 2026-10-15 04:13 | 5000 | -14.96 | 0.435 | -5.41 | 0.359 | False |
| 2026-10-15 08:15 | 5000 | -14.96 | 0.435 | -5.41 | 0.359 | False |
| 2026-10-15 12:17 | 5000 | -14.96 | 0.435 | -5.41 | 0.359 | False |
| 2026-10-15 16:12 | 5000 | -14.97 | 0.435 | -5.42 | 0.359 | False |
| 2026-10-15 20:10 | 5000 | -15.0 | 0.434 | -5.42 | 0.359 | False |
| 2026-10-16 00:28 | 5000 | -14.23 | 0.451 | -5.26 | 0.376 | False |
| 2026-10-16 04:13 | 5000 | -14.23 | 0.451 | -5.12 | 0.383 | False |

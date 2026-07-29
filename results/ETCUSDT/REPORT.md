# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-29 10:38_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.25,
  "use_adx": true,
  "adx_len": 14,
  "adx_thresh": 20.0,
  "don_len": 15,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 18,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-11.6%**, PF 0.555, 64 trades, max DD -1512.01
- Optimizer out-of-sample: net **-5.89%**, PF 0.416, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-27 21:09 | 5000 | -9.49 | 0.618 | -5.58 | 0.454 | False |
| 2026-07-28 02:27 | 5000 | -9.3 | 0.624 | -6.34 | 0.413 | False |
| 2026-07-28 06:26 | 5000 | -9.65 | 0.616 | -6.91 | 0.375 | False |
| 2026-07-28 10:33 | 5000 | -9.65 | 0.617 | -6.38 | 0.395 | False |
| 2026-07-28 14:03 | 5000 | -9.25 | 0.635 | -6.38 | 0.395 | False |
| 2026-07-28 17:26 | 5000 | -9.81 | 0.621 | -6.39 | 0.395 | False |
| 2026-07-28 21:06 | 5000 | -9.72 | 0.625 | -6.03 | 0.409 | False |
| 2026-07-29 02:31 | 5000 | -11.54 | 0.556 | -6.01 | 0.41 | False |
| 2026-07-29 06:29 | 5000 | -11.74 | 0.552 | -6.54 | 0.389 | False |
| 2026-07-29 10:38 | 5000 | -11.6 | 0.555 | -5.89 | 0.416 | False |

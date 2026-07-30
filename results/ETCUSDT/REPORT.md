# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-30 02:13_

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

- Current-params net profit (full sample): **-11.13%**, PF 0.568, 64 trades, max DD -1533.15
- Optimizer out-of-sample: net **-7.3%**, PF 0.376, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-28 14:03 | 5000 | -9.25 | 0.635 | -6.38 | 0.395 | False |
| 2026-07-28 17:26 | 5000 | -9.81 | 0.621 | -6.39 | 0.395 | False |
| 2026-07-28 21:06 | 5000 | -9.72 | 0.625 | -6.03 | 0.409 | False |
| 2026-07-29 02:31 | 5000 | -11.54 | 0.556 | -6.01 | 0.41 | False |
| 2026-07-29 06:29 | 5000 | -11.74 | 0.552 | -6.54 | 0.389 | False |
| 2026-07-29 10:38 | 5000 | -11.6 | 0.555 | -5.89 | 0.416 | False |
| 2026-07-29 14:07 | 5000 | -11.59 | 0.555 | -5.89 | 0.416 | False |
| 2026-07-29 17:13 | 5000 | -11.01 | 0.57 | -5.93 | 0.415 | False |
| 2026-07-29 20:54 | 5000 | -11.89 | 0.55 | -6.7 | 0.384 | False |
| 2026-07-30 02:13 | 5000 | -11.13 | 0.568 | -7.3 | 0.376 | False |

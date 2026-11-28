# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-11-28 04:08_

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

- Current-params net profit (full sample): **-10.61%**, PF 0.555, 64 trades, max DD -1186.68
- Optimizer out-of-sample: net **-3.91%**, PF 0.579, 28 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-26 16:08 | 5000 | -11.43 | 0.534 | -5.05 | 0.494 | False |
| 2026-11-26 20:07 | 5000 | -11.44 | 0.533 | -4.12 | 0.55 | False |
| 2026-11-27 00:19 | 5000 | -10.81 | 0.549 | -2.92 | 0.628 | False |
| 2026-11-27 04:08 | 5000 | -10.81 | 0.549 | -3.81 | 0.57 | False |
| 2026-11-27 08:10 | 5000 | -10.81 | 0.549 | -3.83 | 0.569 | False |
| 2026-11-27 12:11 | 5000 | -10.81 | 0.549 | -3.63 | 0.583 | False |
| 2026-11-27 16:08 | 5000 | -10.96 | 0.546 | -3.79 | 0.572 | False |
| 2026-11-27 20:07 | 5000 | -10.96 | 0.546 | -3.79 | 0.572 | False |
| 2026-11-28 00:18 | 5000 | -10.61 | 0.555 | -3.21 | 0.628 | False |
| 2026-11-28 04:08 | 5000 | -10.61 | 0.555 | -3.91 | 0.579 | False |

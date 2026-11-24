# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-11-24 12:11_

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

- Current-params net profit (full sample): **-11.0%**, PF 0.548, 75 trades, max DD -1262.79
- Optimizer out-of-sample: net **-5.96%**, PF 0.465, 25 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-23 00:21 | 5000 | -9.17 | 0.594 | -4.58 | 0.526 | False |
| 2026-11-23 04:09 | 5000 | -9.42 | 0.589 | -5.38 | 0.487 | False |
| 2026-11-23 08:11 | 5000 | -9.41 | 0.589 | -5.18 | 0.496 | False |
| 2026-11-23 12:11 | 5000 | -9.89 | 0.573 | -5.18 | 0.496 | False |
| 2026-11-23 16:07 | 5000 | -10.47 | 0.56 | -6.13 | 0.455 | False |
| 2026-11-23 20:06 | 5000 | -10.47 | 0.56 | -5.77 | 0.485 | False |
| 2026-11-24 00:18 | 5000 | -10.47 | 0.56 | -5.99 | 0.465 | False |
| 2026-11-24 04:09 | 5000 | -10.48 | 0.56 | -6.14 | 0.455 | False |
| 2026-11-24 08:10 | 5000 | -11.0 | 0.548 | -5.96 | 0.465 | False |
| 2026-11-24 12:11 | 5000 | -11.0 | 0.548 | -5.96 | 0.465 | False |

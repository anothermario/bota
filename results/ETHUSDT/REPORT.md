# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-30 08:11_

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

- Current-params net profit (full sample): **-11.61%**, PF 0.548, 79 trades, max DD -1160.68
- Optimizer out-of-sample: net **-6.73%**, PF 0.227, 24 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-28 20:09 | 5000 | -10.33 | 0.575 | -3.28 | 0.474 | False |
| 2026-10-29 00:22 | 5000 | -10.8 | 0.563 | -3.79 | 0.437 | False |
| 2026-10-29 04:10 | 5000 | -10.52 | 0.571 | -3.82 | 0.437 | False |
| 2026-10-29 08:11 | 5000 | -10.8 | 0.564 | -4.12 | 0.416 | False |
| 2026-10-29 12:13 | 5000 | -10.8 | 0.564 | -3.62 | 0.489 | False |
| 2026-10-29 16:09 | 5000 | -10.82 | 0.564 | -3.65 | 0.489 | False |
| 2026-10-29 20:09 | 5000 | -11.39 | 0.551 | -4.26 | 0.449 | False |
| 2026-10-30 00:23 | 5000 | -12.81 | 0.519 | -6.35 | 0.237 | False |
| 2026-10-30 04:10 | 5000 | -12.38 | 0.53 | -6.73 | 0.226 | False |
| 2026-10-30 08:11 | 5000 | -11.61 | 0.548 | -6.73 | 0.227 | False |

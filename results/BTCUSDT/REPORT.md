# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-10-13 08:20_

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

- Current-params net profit (full sample): **-13.17%**, PF 0.431, 63 trades, max DD -1340.61
- Optimizer out-of-sample: net **-4.09%**, PF 0.295, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-11 20:12 | 5000 | -13.19 | 0.443 | -4.69 | 0.38 | False |
| 2026-10-12 00:38 | 5000 | -12.7 | 0.454 | -6.52 | 0.224 | False |
| 2026-10-12 04:21 | 5000 | -13.34 | 0.422 | -4.32 | 0.276 | False |
| 2026-10-12 08:30 | 5000 | -13.34 | 0.422 | -4.32 | 0.276 | False |
| 2026-10-12 12:25 | 5000 | -14.04 | 0.407 | -4.32 | 0.276 | False |
| 2026-10-12 16:12 | 5000 | -14.05 | 0.408 | -4.29 | 0.283 | False |
| 2026-10-12 20:12 | 5000 | -13.14 | 0.431 | -4.06 | 0.294 | False |
| 2026-10-13 00:35 | 5000 | -13.14 | 0.431 | -4.06 | 0.294 | False |
| 2026-10-13 04:18 | 5000 | -13.14 | 0.431 | -4.06 | 0.294 | False |
| 2026-10-13 08:20 | 5000 | -13.17 | 0.431 | -4.09 | 0.295 | False |

# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-10-13 20:12_

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

- Current-params net profit (full sample): **-13.51%**, PF 0.424, 64 trades, max DD -1350.8
- Optimizer out-of-sample: net **-4.65%**, PF 0.236, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-12 08:30 | 5000 | -13.34 | 0.422 | -4.32 | 0.276 | False |
| 2026-10-12 12:25 | 5000 | -14.04 | 0.407 | -4.32 | 0.276 | False |
| 2026-10-12 16:12 | 5000 | -14.05 | 0.408 | -4.29 | 0.283 | False |
| 2026-10-12 20:12 | 5000 | -13.14 | 0.431 | -4.06 | 0.294 | False |
| 2026-10-13 00:35 | 5000 | -13.14 | 0.431 | -4.06 | 0.294 | False |
| 2026-10-13 04:18 | 5000 | -13.14 | 0.431 | -4.06 | 0.294 | False |
| 2026-10-13 08:20 | 5000 | -13.17 | 0.431 | -4.09 | 0.295 | False |
| 2026-10-13 12:19 | 5000 | -13.5 | 0.424 | -4.79 | 0.231 | False |
| 2026-10-13 16:13 | 5000 | -13.51 | 0.424 | -4.62 | 0.237 | False |
| 2026-10-13 20:12 | 5000 | -13.51 | 0.424 | -4.65 | 0.236 | False |

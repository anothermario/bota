# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-06-11 00:55_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.3,
  "use_adx": true,
  "adx_len": 14,
  "adx_thresh": 20.0,
  "don_len": 20,
  "atr_len": 14,
  "atr_mult": 3.0,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-15.52%**, PF 0.483, 84 trades, max DD -1647.23
- Optimizer out-of-sample: net **-6.86%**, PF 0.261, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-09 16:58 | 5000 | -15.55 | 0.478 | -5.61 | 0.35 | False |
| 2026-06-09 20:44 | 5000 | -15.52 | 0.479 | -6.91 | 0.301 | False |
| 2026-06-10 00:56 | 5000 | -15.15 | 0.486 | -5.35 | 0.362 | False |
| 2026-06-10 05:36 | 5000 | -15.14 | 0.486 | -5.34 | 0.363 | False |
| 2026-06-10 09:19 | 5000 | -15.17 | 0.485 | -6.21 | 0.28 | False |
| 2026-06-10 13:16 | 5000 | -14.76 | 0.493 | -5.92 | 0.29 | False |
| 2026-06-10 17:09 | 5000 | -15.27 | 0.484 | -5.94 | 0.29 | False |
| 2026-06-10 20:57 | 5000 | -15.67 | 0.479 | -6.9 | 0.26 | False |
| 2026-06-11 00:55 | 5000 | -15.52 | 0.483 | -6.86 | 0.261 | False |

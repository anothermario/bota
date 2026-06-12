# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-06-12 13:14_

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

- Current-params net profit (full sample): **-14.99%**, PF 0.494, 84 trades, max DD -1669.99
- Optimizer out-of-sample: net **-6.58%**, PF 0.241, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-11 00:55 | 5000 | -15.52 | 0.483 | -6.86 | 0.261 | False |
| 2026-06-11 05:39 | 5000 | -15.06 | 0.492 | -6.6 | 0.27 | False |
| 2026-06-11 09:34 | 5000 | -15.27 | 0.489 | -6.93 | 0.26 | False |
| 2026-06-11 13:24 | 5000 | -15.27 | 0.489 | -6.92 | 0.26 | False |
| 2026-06-11 17:19 | 5000 | -16.19 | 0.471 | -6.92 | 0.26 | False |
| 2026-06-11 20:52 | 5000 | -16.19 | 0.471 | -6.92 | 0.26 | False |
| 2026-06-12 00:58 | 5000 | -15.46 | 0.485 | -5.26 | 0.32 | False |
| 2026-06-12 05:38 | 5000 | -15.01 | 0.494 | -4.49 | 0.424 | False |
| 2026-06-12 09:29 | 5000 | -15.01 | 0.494 | -5.2 | 0.328 | False |
| 2026-06-12 13:14 | 5000 | -14.99 | 0.494 | -6.58 | 0.241 | False |

# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-19 08:19_

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

- Current-params net profit (full sample): **-14.6%**, PF 0.45, 66 trades, max DD -1472.32
- Optimizer out-of-sample: net **-5.64%**, PF 0.35, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-17 20:10 | 5000 | -14.62 | 0.445 | -5.14 | 0.383 | False |
| 2026-10-18 00:32 | 5000 | -14.62 | 0.444 | -5.15 | 0.383 | False |
| 2026-10-18 04:12 | 5000 | -13.89 | 0.459 | -4.86 | 0.372 | False |
| 2026-10-18 08:13 | 5000 | -13.89 | 0.459 | -4.86 | 0.372 | False |
| 2026-10-18 12:15 | 5000 | -14.7 | 0.445 | -5.76 | 0.333 | False |
| 2026-10-18 16:10 | 5000 | -15.27 | 0.434 | -5.76 | 0.333 | False |
| 2026-10-18 20:10 | 5000 | -15.28 | 0.434 | -5.78 | 0.333 | False |
| 2026-10-19 00:31 | 5000 | -14.57 | 0.45 | -5.61 | 0.35 | False |
| 2026-10-19 04:13 | 5000 | -14.57 | 0.45 | -5.61 | 0.35 | False |
| 2026-10-19 08:19 | 5000 | -14.6 | 0.45 | -5.64 | 0.35 | False |

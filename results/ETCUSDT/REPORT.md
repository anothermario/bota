# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-04 20:47_

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

- Current-params net profit (full sample): **-4.33%**, PF 0.821, 59 trades, max DD -1239.08
- Optimizer out-of-sample: net **-5.72%**, PF 0.257, 18 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-03 08:15 | 5000 | -3.5 | 0.852 | -3.96 | 0.479 | False |
| 2026-10-03 13:44 | 5000 | -3.47 | 0.853 | -5.89 | 0.286 | False |
| 2026-10-03 17:22 | 5000 | -3.64 | 0.846 | -5.89 | 0.286 | False |
| 2026-10-03 21:01 | 5000 | -3.64 | 0.846 | -5.12 | 0.318 | False |
| 2026-10-04 01:10 | 5000 | -4.52 | 0.814 | -5.51 | 0.263 | False |
| 2026-10-04 05:30 | 5000 | -3.64 | 0.846 | -5.51 | 0.263 | False |
| 2026-10-04 10:10 | 5000 | -3.64 | 0.846 | -5.51 | 0.263 | False |
| 2026-10-04 13:58 | 5000 | -3.48 | 0.852 | -5.51 | 0.263 | False |
| 2026-10-04 17:28 | 5000 | -4.16 | 0.829 | -6.17 | 0.242 | False |
| 2026-10-04 20:47 | 5000 | -4.33 | 0.821 | -5.72 | 0.257 | False |

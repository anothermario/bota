# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-10 20:10_

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

- Current-params net profit (full sample): **-1.72%**, PF 0.913, 51 trades, max DD -638.52
- Optimizer out-of-sample: net **-2.59%**, PF 0.557, 14 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-09 08:16 | 5000 | -3.08 | 0.852 | -5.1 | 0.346 | False |
| 2026-09-09 12:17 | 5000 | -3.08 | 0.852 | -3.84 | 0.415 | False |
| 2026-09-09 16:12 | 5000 | -2.22 | 0.89 | -3.84 | 0.415 | False |
| 2026-09-09 20:11 | 5000 | -1.92 | 0.904 | -3.84 | 0.415 | False |
| 2026-09-10 00:29 | 5000 | -1.92 | 0.904 | -3.84 | 0.415 | False |
| 2026-09-10 04:13 | 5000 | -1.47 | 0.926 | -3.86 | 0.413 | False |
| 2026-09-10 08:16 | 5000 | -1.5 | 0.924 | -3.39 | 0.447 | False |
| 2026-09-10 12:17 | 5000 | -2.23 | 0.889 | -3.98 | 0.408 | False |
| 2026-09-10 16:11 | 5000 | -1.72 | 0.913 | -2.52 | 0.569 | False |
| 2026-09-10 20:10 | 5000 | -1.72 | 0.913 | -2.59 | 0.557 | False |

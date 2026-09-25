# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-25 20:10_

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

- Current-params net profit (full sample): **-8.61%**, PF 0.593, 67 trades, max DD -903.77
- Optimizer out-of-sample: net **-2.36%**, PF 0.724, 24 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-24 08:16 | 5000 | -6.96 | 0.642 | -2.04 | 0.748 | False |
| 2026-09-24 12:17 | 5000 | -6.69 | 0.652 | -1.64 | 0.788 | False |
| 2026-09-24 16:13 | 5000 | -7.67 | 0.62 | -1.86 | 0.768 | False |
| 2026-09-24 20:12 | 5000 | -7.67 | 0.62 | -1.86 | 0.768 | False |
| 2026-09-25 00:31 | 5000 | -8.24 | 0.602 | -1.86 | 0.768 | False |
| 2026-09-25 04:13 | 5000 | -8.23 | 0.602 | -1.86 | 0.768 | False |
| 2026-09-25 08:16 | 5000 | -7.67 | 0.62 | -1.17 | 0.841 | False |
| 2026-09-25 12:17 | 5000 | -8.61 | 0.593 | -2.04 | 0.753 | False |
| 2026-09-25 16:13 | 5000 | -8.61 | 0.593 | -2.04 | 0.753 | False |
| 2026-09-25 20:10 | 5000 | -8.61 | 0.593 | -2.36 | 0.724 | False |

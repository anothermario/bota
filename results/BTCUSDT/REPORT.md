# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-06-29 17:04_

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

- Current-params net profit (full sample): **-6.24%**, PF 0.727, 65 trades, max DD -848.68
- Optimizer out-of-sample: net **-6.23%**, PF 0.399, 24 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-28 05:33 | 5000 | -6.61 | 0.715 | -6.96 | 0.375 | False |
| 2026-06-28 09:06 | 5000 | -6.61 | 0.715 | -6.96 | 0.375 | False |
| 2026-06-28 12:33 | 5000 | -6.61 | 0.715 | -6.95 | 0.375 | False |
| 2026-06-28 16:29 | 5000 | -6.61 | 0.715 | -6.96 | 0.375 | False |
| 2026-06-28 20:29 | 5000 | -6.64 | 0.715 | -7.43 | 0.356 | False |
| 2026-06-29 00:54 | 5000 | -6.63 | 0.714 | -7.06 | 0.367 | False |
| 2026-06-29 05:39 | 5000 | -6.24 | 0.727 | -6.73 | 0.379 | False |
| 2026-06-29 09:40 | 5000 | -6.24 | 0.727 | -6.74 | 0.379 | False |
| 2026-06-29 13:34 | 5000 | -6.24 | 0.727 | -6.72 | 0.38 | False |
| 2026-06-29 17:04 | 5000 | -6.24 | 0.727 | -6.23 | 0.399 | False |

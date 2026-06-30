# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-06-30 12:45_

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

- Current-params net profit (full sample): **-6.11%**, PF 0.733, 64 trades, max DD -853.73
- Optimizer out-of-sample: net **-7.48%**, PF 0.27, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-29 00:54 | 5000 | -6.63 | 0.714 | -7.06 | 0.367 | False |
| 2026-06-29 05:39 | 5000 | -6.24 | 0.727 | -6.73 | 0.379 | False |
| 2026-06-29 09:40 | 5000 | -6.24 | 0.727 | -6.74 | 0.379 | False |
| 2026-06-29 13:34 | 5000 | -6.24 | 0.727 | -6.72 | 0.38 | False |
| 2026-06-29 17:04 | 5000 | -6.24 | 0.727 | -6.23 | 0.399 | False |
| 2026-06-29 20:39 | 5000 | -6.24 | 0.727 | -6.22 | 0.399 | False |
| 2026-06-30 00:51 | 5000 | -6.24 | 0.727 | -6.38 | 0.393 | False |
| 2026-06-30 05:26 | 5000 | -6.07 | 0.735 | -6.6 | 0.339 | False |
| 2026-06-30 09:11 | 5000 | -6.07 | 0.735 | -7.47 | 0.271 | False |
| 2026-06-30 12:45 | 5000 | -6.11 | 0.733 | -7.48 | 0.27 | False |

# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-11 20:11_

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

- Current-params net profit (full sample): **-7.34%**, PF 0.565, 63 trades, max DD -738.17
- Optimizer out-of-sample: net **-4.54%**, PF 0.399, 16 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-10 08:15 | 5000 | -7.16 | 0.584 | -3.18 | 0.487 | False |
| 2026-09-10 12:16 | 5000 | -7.47 | 0.573 | -3.98 | 0.429 | False |
| 2026-09-10 16:11 | 5000 | -6.65 | 0.604 | -4.02 | 0.429 | False |
| 2026-09-10 20:10 | 5000 | -7.13 | 0.586 | -3.71 | 0.448 | False |
| 2026-09-11 00:30 | 5000 | -7.13 | 0.586 | -3.71 | 0.448 | False |
| 2026-09-11 04:14 | 5000 | -7.69 | 0.552 | -4.33 | 0.409 | False |
| 2026-09-11 08:15 | 5000 | -8.48 | 0.525 | -3.71 | 0.449 | False |
| 2026-09-11 12:17 | 5000 | -7.67 | 0.552 | -4.44 | 0.403 | False |
| 2026-09-11 16:12 | 5000 | -7.94 | 0.544 | -5.54 | 0.35 | False |
| 2026-09-11 20:11 | 5000 | -7.34 | 0.565 | -4.54 | 0.399 | False |

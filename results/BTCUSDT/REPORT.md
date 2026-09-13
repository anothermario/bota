# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-13 04:12_

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

- Current-params net profit (full sample): **-7.4%**, PF 0.564, 63 trades, max DD -764.17
- Optimizer out-of-sample: net **-4.12%**, PF 0.419, 15 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-11 16:12 | 5000 | -7.94 | 0.544 | -5.54 | 0.35 | False |
| 2026-09-11 20:11 | 5000 | -7.34 | 0.565 | -4.54 | 0.399 | False |
| 2026-09-12 00:29 | 5000 | -7.64 | 0.555 | -4.54 | 0.399 | False |
| 2026-09-12 04:12 | 5000 | -7.16 | 0.572 | -4.53 | 0.399 | False |
| 2026-09-12 08:13 | 5000 | -7.16 | 0.572 | -4.51 | 0.4 | False |
| 2026-09-12 12:14 | 5000 | -7.16 | 0.572 | -3.81 | 0.443 | False |
| 2026-09-12 16:11 | 5000 | -7.16 | 0.572 | -3.81 | 0.443 | False |
| 2026-09-12 20:10 | 5000 | -7.2 | 0.572 | -3.85 | 0.443 | False |
| 2026-09-13 00:34 | 5000 | -7.4 | 0.564 | -4.12 | 0.419 | False |
| 2026-09-13 04:12 | 5000 | -7.4 | 0.564 | -4.12 | 0.419 | False |

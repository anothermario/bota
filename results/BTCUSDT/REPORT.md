# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-16 20:11_

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

- Current-params net profit (full sample): **-8.27%**, PF 0.556, 67 trades, max DD -910.56
- Optimizer out-of-sample: net **-3.72%**, PF 0.553, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-15 08:16 | 5000 | -9.41 | 0.485 | -5.45 | 0.356 | False |
| 2026-09-15 12:16 | 5000 | -9.41 | 0.485 | -5.44 | 0.356 | False |
| 2026-09-15 16:12 | 5000 | -8.39 | 0.552 | -4.57 | 0.499 | False |
| 2026-09-15 20:11 | 5000 | -8.39 | 0.552 | -4.06 | 0.53 | False |
| 2026-09-16 00:30 | 5000 | -8.39 | 0.552 | -4.06 | 0.53 | False |
| 2026-09-16 04:13 | 5000 | -8.39 | 0.552 | -3.72 | 0.553 | False |
| 2026-09-16 08:16 | 5000 | -8.39 | 0.552 | -3.72 | 0.553 | False |
| 2026-09-16 12:17 | 5000 | -8.39 | 0.552 | -3.72 | 0.553 | False |
| 2026-09-16 16:12 | 5000 | -8.4 | 0.552 | -3.72 | 0.553 | False |
| 2026-09-16 20:11 | 5000 | -8.27 | 0.556 | -3.72 | 0.553 | False |

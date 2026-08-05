# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-08-05 20:32_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.25,
  "use_adx": true,
  "adx_len": 14,
  "adx_thresh": 20.0,
  "don_len": 15,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-16.97%**, PF 0.485, 100 trades, max DD -2046.95
- Optimizer out-of-sample: net **-5.02%**, PF 0.422, 27 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-04 10:37 | 5000 | -16.82 | 0.492 | -4.77 | 0.493 | False |
| 2026-08-04 14:08 | 5000 | -17.52 | 0.482 | -5.66 | 0.45 | False |
| 2026-08-04 17:47 | 5000 | -17.57 | 0.481 | -5.8 | 0.372 | False |
| 2026-08-04 20:33 | 5000 | -16.48 | 0.502 | -3.56 | 0.587 | False |
| 2026-08-05 00:35 | 5000 | -16.48 | 0.503 | -3.39 | 0.599 | False |
| 2026-08-05 05:05 | 5000 | -16.47 | 0.503 | -3.27 | 0.606 | False |
| 2026-08-05 08:58 | 5000 | -17.22 | 0.487 | -4.0 | 0.538 | False |
| 2026-08-05 12:39 | 5000 | -16.57 | 0.499 | -4.47 | 0.481 | False |
| 2026-08-05 16:35 | 5000 | -16.57 | 0.499 | -5.16 | 0.418 | False |
| 2026-08-05 20:32 | 5000 | -16.97 | 0.485 | -5.02 | 0.422 | False |

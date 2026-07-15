# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-15 06:13_

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
  "chand_len": 18,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-12.08%**, PF 0.515, 66 trades, max DD -1243.57
- Optimizer out-of-sample: net **-3.64%**, PF 0.362, 15 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-13 17:54 | 5000 | -11.33 | 0.553 | -3.73 | 0.358 | False |
| 2026-07-13 20:56 | 5000 | -10.83 | 0.566 | -3.73 | 0.358 | False |
| 2026-07-14 02:25 | 5000 | -10.85 | 0.565 | -3.73 | 0.358 | False |
| 2026-07-14 06:10 | 5000 | -10.54 | 0.573 | -3.73 | 0.358 | False |
| 2026-07-14 09:57 | 5000 | -10.75 | 0.564 | -3.73 | 0.358 | False |
| 2026-07-14 13:41 | 5000 | -11.64 | 0.524 | -3.76 | 0.358 | False |
| 2026-07-14 17:13 | 5000 | -11.66 | 0.523 | -3.76 | 0.358 | False |
| 2026-07-14 20:59 | 5000 | -11.24 | 0.534 | -3.76 | 0.358 | False |
| 2026-07-15 02:22 | 5000 | -12.11 | 0.513 | -3.02 | 0.412 | False |
| 2026-07-15 06:13 | 5000 | -12.08 | 0.515 | -3.64 | 0.362 | False |

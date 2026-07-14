# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-14 09:57_

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

- Current-params net profit (full sample): **-10.75%**, PF 0.564, 66 trades, max DD -1207.07
- Optimizer out-of-sample: net **-3.73%**, PF 0.358, 14 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-12 20:45 | 5000 | -8.9 | 0.642 | -2.63 | 0.508 | False |
| 2026-07-13 02:41 | 5000 | -9.21 | 0.628 | -4.91 | 0.294 | False |
| 2026-07-13 06:52 | 5000 | -9.21 | 0.628 | -3.59 | 0.366 | False |
| 2026-07-13 11:09 | 5000 | -9.35 | 0.623 | -3.25 | 0.392 | False |
| 2026-07-13 14:32 | 5000 | -9.87 | 0.609 | -3.73 | 0.358 | False |
| 2026-07-13 17:54 | 5000 | -11.33 | 0.553 | -3.73 | 0.358 | False |
| 2026-07-13 20:56 | 5000 | -10.83 | 0.566 | -3.73 | 0.358 | False |
| 2026-07-14 02:25 | 5000 | -10.85 | 0.565 | -3.73 | 0.358 | False |
| 2026-07-14 06:10 | 5000 | -10.54 | 0.573 | -3.73 | 0.358 | False |
| 2026-07-14 09:57 | 5000 | -10.75 | 0.564 | -3.73 | 0.358 | False |

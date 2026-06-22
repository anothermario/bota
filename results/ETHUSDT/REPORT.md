# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-06-22 00:58_

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

- Current-params net profit (full sample): **-11.67%**, PF 0.585, 88 trades, max DD -1282.38
- Optimizer out-of-sample: net **-4.15%**, PF 0.581, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-20 12:41 | 5000 | -11.24 | 0.591 | -0.93 | 0.888 | False |
| 2026-06-20 16:35 | 5000 | -12.52 | 0.564 | -2.84 | 0.594 | False |
| 2026-06-20 20:31 | 5000 | -12.51 | 0.564 | -2.85 | 0.593 | False |
| 2026-06-21 00:58 | 5000 | -11.84 | 0.58 | -3.99 | 0.593 | False |
| 2026-06-21 05:40 | 5000 | -12.23 | 0.572 | -4.12 | 0.584 | False |
| 2026-06-21 09:19 | 5000 | -11.67 | 0.585 | -4.12 | 0.584 | False |
| 2026-06-21 12:45 | 5000 | -11.67 | 0.585 | -4.03 | 0.592 | False |
| 2026-06-21 16:36 | 5000 | -11.99 | 0.577 | -4.14 | 0.581 | False |
| 2026-06-21 20:35 | 5000 | -11.99 | 0.577 | -4.14 | 0.581 | False |
| 2026-06-22 00:58 | 5000 | -11.67 | 0.585 | -4.15 | 0.581 | False |

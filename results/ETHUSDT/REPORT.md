# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-06-29 13:34_

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

- Current-params net profit (full sample): **-12.23%**, PF 0.582, 89 trades, max DD -1222.58
- Optimizer out-of-sample: net **-2.96%**, PF 0.57, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-28 00:53 | 5000 | -11.76 | 0.607 | -1.52 | 0.78 | False |
| 2026-06-28 05:34 | 5000 | -11.02 | 0.625 | -1.52 | 0.78 | False |
| 2026-06-28 09:06 | 5000 | -11.64 | 0.612 | -2.72 | 0.739 | False |
| 2026-06-28 12:33 | 5000 | -12.73 | 0.57 | -2.99 | 0.568 | False |
| 2026-06-28 16:29 | 5000 | -12.73 | 0.57 | -2.96 | 0.57 | False |
| 2026-06-28 20:29 | 5000 | -12.73 | 0.57 | -3.22 | 0.549 | False |
| 2026-06-29 00:54 | 5000 | -12.73 | 0.57 | -3.21 | 0.549 | False |
| 2026-06-29 05:39 | 5000 | -12.7 | 0.571 | -2.96 | 0.57 | False |
| 2026-06-29 09:40 | 5000 | -12.24 | 0.581 | -2.96 | 0.57 | False |
| 2026-06-29 13:34 | 5000 | -12.23 | 0.582 | -2.96 | 0.57 | False |

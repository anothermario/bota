# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-06-30 16:47_

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

- Current-params net profit (full sample): **-10.98%**, PF 0.615, 88 trades, max DD -1187.38
- Optimizer out-of-sample: net **-1.32%**, PF 0.781, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-29 05:39 | 5000 | -12.7 | 0.571 | -2.96 | 0.57 | False |
| 2026-06-29 09:40 | 5000 | -12.24 | 0.581 | -2.96 | 0.57 | False |
| 2026-06-29 13:34 | 5000 | -12.23 | 0.582 | -2.96 | 0.57 | False |
| 2026-06-29 17:04 | 5000 | -12.41 | 0.577 | -2.96 | 0.57 | False |
| 2026-06-29 20:40 | 5000 | -12.41 | 0.577 | -2.95 | 0.571 | False |
| 2026-06-30 00:52 | 5000 | -12.4 | 0.578 | -2.31 | 0.632 | False |
| 2026-06-30 05:27 | 5000 | -12.24 | 0.582 | -1.92 | 0.678 | False |
| 2026-06-30 09:11 | 5000 | -12.4 | 0.578 | -1.93 | 0.679 | False |
| 2026-06-30 12:45 | 5000 | -11.96 | 0.589 | -2.1 | 0.657 | False |
| 2026-06-30 16:47 | 5000 | -10.98 | 0.615 | -1.32 | 0.781 | False |

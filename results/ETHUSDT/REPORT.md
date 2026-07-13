# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-13 06:52_

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

- Current-params net profit (full sample): **-12.67%**, PF 0.62, 96 trades, max DD -1581.5
- Optimizer out-of-sample: net **-7.64%**, PF 0.262, 32 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-11 16:57 | 5000 | -13.18 | 0.603 | -6.64 | 0.287 | False |
| 2026-07-11 20:45 | 5000 | -12.52 | 0.617 | -5.88 | 0.315 | False |
| 2026-07-12 02:39 | 5000 | -12.38 | 0.622 | -6.26 | 0.301 | False |
| 2026-07-12 06:32 | 5000 | -11.85 | 0.634 | -6.31 | 0.298 | False |
| 2026-07-12 09:50 | 5000 | -12.43 | 0.621 | -6.26 | 0.301 | False |
| 2026-07-12 13:17 | 5000 | -11.77 | 0.635 | -6.45 | 0.294 | False |
| 2026-07-12 16:57 | 5000 | -11.66 | 0.639 | -6.24 | 0.309 | False |
| 2026-07-12 20:45 | 5000 | -11.1 | 0.652 | -6.12 | 0.321 | False |
| 2026-07-13 02:40 | 5000 | -13.04 | 0.612 | -7.64 | 0.262 | False |
| 2026-07-13 06:52 | 5000 | -12.67 | 0.62 | -7.64 | 0.262 | False |

# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-14 12:18_

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

- Current-params net profit (full sample): **-12.35%**, PF 0.438, 70 trades, max DD -1366.22
- Optimizer out-of-sample: net **-2.3%**, PF 0.46, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-13 00:25 | 5000 | -11.7 | 0.475 | -4.9 | 0.338 | False |
| 2026-08-13 04:37 | 5000 | -11.27 | 0.491 | -4.83 | 0.342 | False |
| 2026-08-13 08:33 | 5000 | -11.5 | 0.48 | -1.68 | 0.592 | False |
| 2026-08-13 12:19 | 5000 | -11.5 | 0.48 | -4.78 | 0.346 | False |
| 2026-08-13 16:20 | 5000 | -11.5 | 0.48 | -6.29 | 0.283 | False |
| 2026-08-13 20:13 | 5000 | -11.5 | 0.48 | -1.08 | 0.694 | False |
| 2026-08-14 00:26 | 5000 | -11.52 | 0.479 | -1.08 | 0.694 | False |
| 2026-08-14 04:36 | 5000 | -12.31 | 0.438 | -2.27 | 0.458 | False |
| 2026-08-14 08:30 | 5000 | -12.35 | 0.438 | -2.31 | 0.458 | False |
| 2026-08-14 12:18 | 5000 | -12.35 | 0.438 | -2.3 | 0.46 | False |

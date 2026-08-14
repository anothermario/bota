# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-14 00:26_

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

- Current-params net profit (full sample): **-11.52%**, PF 0.479, 71 trades, max DD -1374.94
- Optimizer out-of-sample: net **-1.08%**, PF 0.694, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-12 12:19 | 5000 | -11.48 | 0.479 | -4.78 | 0.344 | False |
| 2026-08-12 16:20 | 5000 | -12.14 | 0.464 | -5.65 | 0.306 | False |
| 2026-08-12 20:15 | 5000 | -11.28 | 0.485 | -5.64 | 0.306 | False |
| 2026-08-13 00:25 | 5000 | -11.7 | 0.475 | -4.9 | 0.338 | False |
| 2026-08-13 04:37 | 5000 | -11.27 | 0.491 | -4.83 | 0.342 | False |
| 2026-08-13 08:33 | 5000 | -11.5 | 0.48 | -1.68 | 0.592 | False |
| 2026-08-13 12:19 | 5000 | -11.5 | 0.48 | -4.78 | 0.346 | False |
| 2026-08-13 16:20 | 5000 | -11.5 | 0.48 | -6.29 | 0.283 | False |
| 2026-08-13 20:13 | 5000 | -11.5 | 0.48 | -1.08 | 0.694 | False |
| 2026-08-14 00:26 | 5000 | -11.52 | 0.479 | -1.08 | 0.694 | False |

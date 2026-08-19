# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-19 04:15_

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

- Current-params net profit (full sample): **-10.78%**, PF 0.434, 70 trades, max DD -1280.49
- Optimizer out-of-sample: net **-1.75%**, PF 0.37, 17 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-17 16:06 | 5000 | -11.27 | 0.41 | -2.02 | 0.406 | False |
| 2026-08-17 20:07 | 5000 | -11.27 | 0.41 | -1.62 | 0.462 | False |
| 2026-08-18 00:14 | 5000 | -11.27 | 0.41 | -1.63 | 0.461 | False |
| 2026-08-18 04:15 | 5000 | -10.78 | 0.434 | -1.44 | 0.564 | False |
| 2026-08-18 08:11 | 5000 | -10.78 | 0.434 | -0.94 | 0.664 | False |
| 2026-08-18 12:09 | 5000 | -10.78 | 0.434 | -1.62 | 0.45 | False |
| 2026-08-18 16:08 | 5000 | -10.78 | 0.434 | -1.47 | 0.475 | False |
| 2026-08-18 20:06 | 5000 | -10.78 | 0.434 | -1.46 | 0.476 | False |
| 2026-08-19 00:13 | 5000 | -10.78 | 0.434 | -1.75 | 0.37 | False |
| 2026-08-19 04:15 | 5000 | -10.78 | 0.434 | -1.75 | 0.37 | False |

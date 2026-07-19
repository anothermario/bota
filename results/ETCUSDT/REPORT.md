# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-19 20:45_

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

- Current-params net profit (full sample): **-13.29%**, PF 0.46, 62 trades, max DD -1329.33
- Optimizer out-of-sample: net **-4.79%**, PF 0.285, 14 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-18 09:24 | 5000 | -12.98 | 0.486 | -4.95 | 0.295 | False |
| 2026-07-18 13:12 | 5000 | -12.18 | 0.504 | -4.95 | 0.295 | False |
| 2026-07-18 16:57 | 5000 | -11.36 | 0.541 | -4.95 | 0.296 | False |
| 2026-07-18 20:45 | 5000 | -12.15 | 0.505 | -5.96 | 0.239 | False |
| 2026-07-19 02:36 | 5000 | -13.01 | 0.465 | -5.12 | 0.269 | False |
| 2026-07-19 06:29 | 5000 | -13.13 | 0.462 | -5.12 | 0.269 | False |
| 2026-07-19 09:52 | 5000 | -12.91 | 0.467 | -5.13 | 0.269 | False |
| 2026-07-19 13:15 | 5000 | -12.92 | 0.467 | -4.22 | 0.311 | False |
| 2026-07-19 16:57 | 5000 | -12.76 | 0.47 | -4.23 | 0.311 | False |
| 2026-07-19 20:45 | 5000 | -13.29 | 0.46 | -4.79 | 0.285 | False |

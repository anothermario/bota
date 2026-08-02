# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-02 09:55_

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

- Current-params net profit (full sample): **-15.74%**, PF 0.395, 75 trades, max DD -1610.21
- Optimizer out-of-sample: net **-6.59%**, PF 0.287, 29 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-31 21:02 | 5000 | -16.4 | 0.378 | -6.52 | 0.311 | False |
| 2026-08-01 02:41 | 5000 | -16.39 | 0.378 | -6.52 | 0.311 | False |
| 2026-08-01 06:28 | 5000 | -16.39 | 0.378 | -6.95 | 0.296 | False |
| 2026-08-01 09:57 | 5000 | -15.79 | 0.389 | -7.01 | 0.255 | False |
| 2026-08-01 13:17 | 5000 | -15.79 | 0.389 | -7.04 | 0.251 | False |
| 2026-08-01 16:57 | 5000 | -15.79 | 0.389 | -7.04 | 0.251 | False |
| 2026-08-01 20:53 | 5000 | -15.54 | 0.398 | -6.77 | 0.28 | False |
| 2026-08-02 02:39 | 5000 | -15.63 | 0.398 | -6.47 | 0.292 | False |
| 2026-08-02 06:31 | 5000 | -15.63 | 0.398 | -6.47 | 0.292 | False |
| 2026-08-02 09:55 | 5000 | -15.74 | 0.395 | -6.59 | 0.287 | False |

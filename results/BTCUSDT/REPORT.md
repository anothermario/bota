# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-03 17:49_

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

- Current-params net profit (full sample): **-15.79%**, PF 0.405, 78 trades, max DD -1634.48
- Optimizer out-of-sample: net **-7.01%**, PF 0.29, 31 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-02 06:31 | 5000 | -15.63 | 0.398 | -6.47 | 0.292 | False |
| 2026-08-02 09:55 | 5000 | -15.74 | 0.395 | -6.59 | 0.287 | False |
| 2026-08-02 13:17 | 5000 | -15.77 | 0.395 | -6.63 | 0.287 | False |
| 2026-08-02 16:56 | 5000 | -16.08 | 0.39 | -7.15 | 0.27 | False |
| 2026-08-02 20:54 | 5000 | -16.11 | 0.39 | -7.01 | 0.275 | False |
| 2026-08-03 02:41 | 5000 | -16.2 | 0.389 | -7.56 | 0.237 | False |
| 2026-08-03 06:58 | 5000 | -16.23 | 0.389 | -7.41 | 0.242 | False |
| 2026-08-03 11:21 | 5000 | -15.75 | 0.406 | -6.88 | 0.293 | False |
| 2026-08-03 14:35 | 5000 | -15.78 | 0.406 | -6.91 | 0.293 | False |
| 2026-08-03 17:49 | 5000 | -15.79 | 0.405 | -7.01 | 0.29 | False |

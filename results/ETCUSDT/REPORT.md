# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-11-03 04:08_

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
  "chand_len": 26,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-14.7%**, PF 0.44, 68 trades, max DD -1486.99
- Optimizer out-of-sample: net **-4.13%**, PF 0.518, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-01 12:10 | 5000 | -16.12 | 0.408 | -4.26 | 0.558 | False |
| 2026-11-01 16:07 | 5000 | -16.12 | 0.408 | -2.71 | 0.696 | False |
| 2026-11-01 20:07 | 5000 | -16.12 | 0.408 | -3.44 | 0.612 | False |
| 2026-11-02 00:21 | 5000 | -16.13 | 0.408 | -3.97 | 0.534 | False |
| 2026-11-02 04:09 | 5000 | -15.61 | 0.417 | -3.97 | 0.534 | False |
| 2026-11-02 08:11 | 5000 | -14.79 | 0.432 | -3.97 | 0.534 | False |
| 2026-11-02 12:11 | 5000 | -14.09 | 0.447 | -3.97 | 0.534 | False |
| 2026-11-02 20:06 | 5000 | -14.16 | 0.449 | -3.08 | 0.601 | False |
| 2026-11-03 00:19 | 5000 | -14.7 | 0.44 | -4.01 | 0.533 | False |
| 2026-11-03 04:08 | 5000 | -14.7 | 0.44 | -4.13 | 0.518 | False |

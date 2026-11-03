# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-11-03 16:08_

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

- Current-params net profit (full sample): **-15.47%**, PF 0.422, 69 trades, max DD -1546.95
- Optimizer out-of-sample: net **-4.52%**, PF 0.539, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-02 00:21 | 5000 | -16.13 | 0.408 | -3.97 | 0.534 | False |
| 2026-11-02 04:09 | 5000 | -15.61 | 0.417 | -3.97 | 0.534 | False |
| 2026-11-02 08:11 | 5000 | -14.79 | 0.432 | -3.97 | 0.534 | False |
| 2026-11-02 12:11 | 5000 | -14.09 | 0.447 | -3.97 | 0.534 | False |
| 2026-11-02 20:06 | 5000 | -14.16 | 0.449 | -3.08 | 0.601 | False |
| 2026-11-03 00:19 | 5000 | -14.7 | 0.44 | -4.01 | 0.533 | False |
| 2026-11-03 04:08 | 5000 | -14.7 | 0.44 | -4.13 | 0.518 | False |
| 2026-11-03 08:10 | 5000 | -14.7 | 0.44 | -4.81 | 0.478 | False |
| 2026-11-03 12:10 | 5000 | -14.42 | 0.446 | -4.85 | 0.478 | False |
| 2026-11-03 16:08 | 5000 | -15.47 | 0.422 | -4.52 | 0.539 | False |

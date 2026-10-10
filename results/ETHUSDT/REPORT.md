# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-10 16:12_

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

- Current-params net profit (full sample): **-14.85%**, PF 0.511, 103 trades, max DD -1616.28
- Optimizer out-of-sample: net **-6.28%**, PF 0.193, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-09 04:16 | 5000 | -15.04 | 0.513 | -6.24 | 0.193 | False |
| 2026-10-09 08:18 | 5000 | -15.05 | 0.513 | -6.24 | 0.193 | False |
| 2026-10-09 12:17 | 5000 | -14.46 | 0.527 | -6.24 | 0.193 | False |
| 2026-10-09 16:12 | 5000 | -14.47 | 0.527 | -6.24 | 0.193 | False |
| 2026-10-09 20:12 | 5000 | -14.46 | 0.527 | -6.24 | 0.193 | False |
| 2026-10-10 00:34 | 5000 | -14.81 | 0.52 | -6.24 | 0.193 | False |
| 2026-10-10 04:14 | 5000 | -14.84 | 0.519 | -6.24 | 0.193 | False |
| 2026-10-10 08:15 | 5000 | -13.97 | 0.541 | -6.24 | 0.193 | False |
| 2026-10-10 12:16 | 5000 | -14.6 | 0.515 | -6.24 | 0.193 | False |
| 2026-10-10 16:12 | 5000 | -14.85 | 0.511 | -6.28 | 0.193 | False |

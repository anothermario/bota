# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-28 08:22_

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

- Current-params net profit (full sample): **-13.52%**, PF 0.521, 98 trades, max DD -1462.13
- Optimizer out-of-sample: net **-3.68%**, PF 0.541, 26 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-26 20:10 | 5000 | -13.86 | 0.51 | -3.33 | 0.594 | False |
| 2026-09-27 00:36 | 5000 | -13.88 | 0.51 | -3.35 | 0.578 | False |
| 2026-09-27 04:13 | 5000 | -13.91 | 0.51 | -3.35 | 0.579 | False |
| 2026-09-27 08:14 | 5000 | -13.59 | 0.517 | -3.24 | 0.59 | False |
| 2026-09-27 12:16 | 5000 | -13.99 | 0.509 | -3.64 | 0.557 | False |
| 2026-09-27 16:11 | 5000 | -14.05 | 0.509 | -4.22 | 0.506 | False |
| 2026-09-27 20:11 | 5000 | -13.88 | 0.514 | -4.15 | 0.51 | False |
| 2026-09-28 00:35 | 5000 | -13.45 | 0.524 | -3.85 | 0.53 | False |
| 2026-09-28 04:15 | 5000 | -13.47 | 0.524 | -3.68 | 0.541 | False |
| 2026-09-28 08:22 | 5000 | -13.52 | 0.521 | -3.68 | 0.541 | False |

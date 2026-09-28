# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-28 20:11_

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

- Current-params net profit (full sample): **-13.5%**, PF 0.524, 98 trades, max DD -1350.32
- Optimizer out-of-sample: net **-5.67%**, PF 0.479, 31 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-27 08:14 | 5000 | -13.59 | 0.517 | -3.24 | 0.59 | False |
| 2026-09-27 12:16 | 5000 | -13.99 | 0.509 | -3.64 | 0.557 | False |
| 2026-09-27 16:11 | 5000 | -14.05 | 0.509 | -4.22 | 0.506 | False |
| 2026-09-27 20:11 | 5000 | -13.88 | 0.514 | -4.15 | 0.51 | False |
| 2026-09-28 00:35 | 5000 | -13.45 | 0.524 | -3.85 | 0.53 | False |
| 2026-09-28 04:15 | 5000 | -13.47 | 0.524 | -3.68 | 0.541 | False |
| 2026-09-28 08:22 | 5000 | -13.52 | 0.521 | -3.68 | 0.541 | False |
| 2026-09-28 12:19 | 5000 | -13.42 | 0.525 | -4.79 | 0.523 | False |
| 2026-09-28 16:14 | 5000 | -13.5 | 0.524 | -5.1 | 0.507 | False |
| 2026-09-28 20:11 | 5000 | -13.5 | 0.524 | -5.67 | 0.479 | False |

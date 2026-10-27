# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-27 12:17_

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

- Current-params net profit (full sample): **-13.43%**, PF 0.479, 65 trades, max DD -1562.3
- Optimizer out-of-sample: net **-4.02%**, PF 0.549, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-26 00:30 | 5000 | -11.78 | 0.545 | -5.22 | 0.478 | False |
| 2026-10-26 04:14 | 5000 | -11.25 | 0.558 | -4.8 | 0.501 | False |
| 2026-10-26 08:21 | 5000 | -12.37 | 0.533 | -5.72 | 0.456 | False |
| 2026-10-26 13:39 | 5000 | -12.0 | 0.542 | -4.76 | 0.504 | False |
| 2026-10-26 16:15 | 5000 | -12.07 | 0.539 | -4.33 | 0.529 | False |
| 2026-10-26 20:11 | 5000 | -12.42 | 0.524 | -2.89 | 0.724 | False |
| 2026-10-27 00:29 | 5000 | -13.34 | 0.483 | -4.02 | 0.549 | False |
| 2026-10-27 04:12 | 5000 | -13.42 | 0.479 | -4.02 | 0.549 | False |
| 2026-10-27 08:15 | 5000 | -13.43 | 0.479 | -4.02 | 0.549 | False |
| 2026-10-27 12:17 | 5000 | -13.43 | 0.479 | -4.02 | 0.549 | False |

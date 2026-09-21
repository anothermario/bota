# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-21 12:17_

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

- Current-params net profit (full sample): **-2.69%**, PF 0.872, 55 trades, max DD -800.39
- Optimizer out-of-sample: net **-3.3%**, PF 0.586, 18 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-20 00:35 | 5000 | -2.3 | 0.889 | -2.25 | 0.737 | False |
| 2026-09-20 04:13 | 5000 | -2.3 | 0.889 | -2.25 | 0.738 | False |
| 2026-09-20 08:14 | 5000 | -2.3 | 0.889 | -2.25 | 0.737 | False |
| 2026-09-20 12:15 | 5000 | -2.3 | 0.889 | -3.31 | 0.609 | False |
| 2026-09-20 16:11 | 5000 | -2.83 | 0.866 | -3.84 | 0.546 | False |
| 2026-09-20 20:10 | 5000 | -2.83 | 0.866 | -4.21 | 0.523 | False |
| 2026-09-21 00:33 | 5000 | -2.7 | 0.872 | -4.22 | 0.523 | False |
| 2026-09-21 04:15 | 5000 | -2.7 | 0.872 | -4.21 | 0.523 | False |
| 2026-09-21 08:18 | 5000 | -2.7 | 0.872 | -3.3 | 0.586 | False |
| 2026-09-21 12:17 | 5000 | -2.69 | 0.872 | -3.3 | 0.586 | False |

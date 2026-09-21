# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-21 08:18_

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

- Current-params net profit (full sample): **-13.23%**, PF 0.518, 103 trades, max DD -1651.09
- Optimizer out-of-sample: net **-8.27%**, PF 0.367, 38 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-19 20:10 | 5000 | -13.07 | 0.527 | -7.53 | 0.38 | False |
| 2026-09-20 00:34 | 5000 | -12.4 | 0.542 | -7.53 | 0.38 | False |
| 2026-09-20 04:13 | 5000 | -12.42 | 0.543 | -7.88 | 0.37 | False |
| 2026-09-20 08:14 | 5000 | -12.7 | 0.536 | -7.88 | 0.37 | False |
| 2026-09-20 12:15 | 5000 | -12.2 | 0.548 | -8.46 | 0.352 | False |
| 2026-09-20 16:11 | 5000 | -12.23 | 0.547 | -7.94 | 0.38 | False |
| 2026-09-20 20:10 | 5000 | -12.23 | 0.547 | -7.65 | 0.404 | False |
| 2026-09-21 00:33 | 5000 | -11.93 | 0.559 | -8.47 | 0.362 | False |
| 2026-09-21 04:14 | 5000 | -13.69 | 0.506 | -8.81 | 0.352 | False |
| 2026-09-21 08:18 | 5000 | -13.23 | 0.518 | -8.27 | 0.367 | False |

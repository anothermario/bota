# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-31 20:06_

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

- Current-params net profit (full sample): **-10.54%**, PF 0.575, 77 trades, max DD -1145.14
- Optimizer out-of-sample: net **-5.22%**, PF 0.277, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-30 08:11 | 5000 | -11.61 | 0.548 | -6.73 | 0.227 | False |
| 2026-10-30 12:13 | 5000 | -11.61 | 0.548 | -6.13 | 0.244 | False |
| 2026-10-30 16:08 | 5000 | -11.29 | 0.556 | -6.81 | 0.224 | False |
| 2026-10-30 20:07 | 5000 | -11.29 | 0.556 | -6.81 | 0.224 | False |
| 2026-10-31 00:18 | 5000 | -11.59 | 0.549 | -6.78 | 0.225 | False |
| 2026-10-31 04:08 | 5000 | -10.76 | 0.57 | -6.78 | 0.225 | False |
| 2026-10-31 08:08 | 5000 | -10.76 | 0.57 | -6.78 | 0.225 | False |
| 2026-10-31 12:09 | 5000 | -10.76 | 0.57 | -6.1 | 0.245 | False |
| 2026-10-31 16:07 | 5000 | -11.17 | 0.559 | -7.55 | 0.219 | False |
| 2026-10-31 20:06 | 5000 | -10.54 | 0.575 | -5.22 | 0.277 | False |

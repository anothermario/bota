# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-11-01 12:10_

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

- Current-params net profit (full sample): **-10.38%**, PF 0.58, 76 trades, max DD -1151.18
- Optimizer out-of-sample: net **-4.99%**, PF 0.289, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-31 00:18 | 5000 | -11.59 | 0.549 | -6.78 | 0.225 | False |
| 2026-10-31 04:08 | 5000 | -10.76 | 0.57 | -6.78 | 0.225 | False |
| 2026-10-31 08:08 | 5000 | -10.76 | 0.57 | -6.78 | 0.225 | False |
| 2026-10-31 12:09 | 5000 | -10.76 | 0.57 | -6.1 | 0.245 | False |
| 2026-10-31 16:07 | 5000 | -11.17 | 0.559 | -7.55 | 0.219 | False |
| 2026-10-31 20:06 | 5000 | -10.54 | 0.575 | -5.22 | 0.277 | False |
| 2026-11-01 00:23 | 5000 | -10.53 | 0.575 | -5.22 | 0.277 | False |
| 2026-11-01 04:08 | 5000 | -10.56 | 0.575 | -4.99 | 0.289 | False |
| 2026-11-01 08:09 | 5000 | -10.38 | 0.58 | -4.99 | 0.289 | False |
| 2026-11-01 12:10 | 5000 | -10.38 | 0.58 | -4.99 | 0.289 | False |

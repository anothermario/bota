# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-06-17 17:06_

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
  "don_len": 30,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 26,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-10.07%**, PF 0.579, 76 trades, max DD -1218.87
- Optimizer out-of-sample: net **0.41%**, PF 1.064, 20 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-16 05:54 | 5000 | -14.5 | 0.438 | -1.27 | 0.83 | False |
| 2026-06-16 09:51 | 5000 | -13.3 | 0.485 | -0.88 | 0.883 | False |
| 2026-06-16 13:53 | 5000 | -12.76 | 0.501 | -0.71 | 0.903 | False |
| 2026-06-16 17:45 | 5000 | -13.07 | 0.495 | -0.17 | 0.975 | False |
| 2026-06-16 21:06 | 5000 | -13.07 | 0.495 | -0.17 | 0.975 | False |
| 2026-06-17 00:58 | 5000 | -12.76 | 0.501 | -0.17 | 0.975 | False |
| 2026-06-17 05:43 | 5000 | -12.76 | 0.501 | 0.85 | 1.145 | True |
| 2026-06-17 09:43 | 5000 | -9.55 | 0.591 | 1.35 | 1.249 | True |
| 2026-06-17 13:21 | 5000 | -9.28 | 0.6 | 1.32 | 1.249 | True |
| 2026-06-17 17:06 | 5000 | -10.07 | 0.579 | 0.41 | 1.064 | True |

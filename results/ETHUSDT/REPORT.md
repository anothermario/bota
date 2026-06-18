# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-06-18 13:15_

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

- Current-params net profit (full sample): **-10.4%**, PF 0.57, 75 trades, max DD -1248.73
- Optimizer out-of-sample: net **0.29%**, PF 1.046, 18 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-17 00:58 | 5000 | -12.76 | 0.501 | -0.17 | 0.975 | False |
| 2026-06-17 05:43 | 5000 | -12.76 | 0.501 | 0.85 | 1.145 | True |
| 2026-06-17 09:43 | 5000 | -9.55 | 0.591 | 1.35 | 1.249 | True |
| 2026-06-17 13:21 | 5000 | -9.28 | 0.6 | 1.32 | 1.249 | True |
| 2026-06-17 17:06 | 5000 | -10.07 | 0.579 | 0.41 | 1.064 | True |
| 2026-06-17 20:47 | 5000 | -10.07 | 0.579 | 0.43 | 1.068 | True |
| 2026-06-18 00:58 | 5000 | -10.53 | 0.567 | -1.31 | 0.848 | False |
| 2026-06-18 05:40 | 5000 | -10.36 | 0.572 | 0.38 | 1.061 | True |
| 2026-06-18 09:34 | 5000 | -10.54 | 0.566 | -2.29 | 0.758 | False |
| 2026-06-18 13:15 | 5000 | -10.4 | 0.57 | 0.29 | 1.046 | True |

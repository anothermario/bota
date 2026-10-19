# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-19 12:18_

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

- Current-params net profit (full sample): **-7.81%**, PF 0.663, 73 trades, max DD -1018.27
- Optimizer out-of-sample: net **0.29%**, PF 1.05, 23 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-18 00:32 | 5000 | -12.05 | 0.614 | -0.93 | 0.853 | False |
| 2026-10-18 04:12 | 5000 | -12.07 | 0.615 | -0.44 | 0.925 | False |
| 2026-10-18 08:13 | 5000 | -12.7 | 0.601 | -0.44 | 0.925 | False |
| 2026-10-18 12:14 | 5000 | -12.7 | 0.601 | -0.44 | 0.925 | False |
| 2026-10-18 16:10 | 5000 | -13.32 | 0.588 | -3.29 | 0.651 | False |
| 2026-10-18 20:10 | 5000 | -13.32 | 0.588 | -0.43 | 0.932 | False |
| 2026-10-19 00:31 | 5000 | -12.4 | 0.612 | 0.13 | 1.022 | True |
| 2026-10-19 04:13 | 5000 | -8.11 | 0.652 | 0.17 | 1.034 | True |
| 2026-10-19 08:19 | 5000 | -7.88 | 0.661 | 0.1 | 1.022 | True |
| 2026-10-19 12:18 | 5000 | -7.81 | 0.663 | 0.29 | 1.05 | True |

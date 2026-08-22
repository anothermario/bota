# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-22 12:07_

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
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-10.18%**, PF 0.476, 74 trades, max DD -1261.15
- Optimizer out-of-sample: net **1.18%**, PF 1.39, 22 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-21 00:15 | 5000 | -11.1 | 0.431 | -1.55 | 0.609 | False |
| 2026-08-21 04:16 | 5000 | -10.34 | 0.471 | -0.77 | 0.809 | False |
| 2026-08-21 08:14 | 5000 | -10.39 | 0.468 | -0.75 | 0.817 | False |
| 2026-08-21 12:09 | 5000 | -9.72 | 0.502 | 0.43 | 1.121 | True |
| 2026-08-21 16:08 | 5000 | -10.27 | 0.487 | 0.43 | 1.122 | True |
| 2026-08-21 20:06 | 5000 | -9.72 | 0.502 | 0.08 | 1.021 | True |
| 2026-08-22 00:14 | 5000 | -9.72 | 0.502 | 0.64 | 1.19 | True |
| 2026-08-22 04:13 | 5000 | -9.72 | 0.502 | 0.64 | 1.19 | True |
| 2026-08-22 08:07 | 5000 | -9.73 | 0.501 | 1.02 | 1.338 | True |
| 2026-08-22 12:07 | 5000 | -10.18 | 0.476 | 1.18 | 1.39 | True |

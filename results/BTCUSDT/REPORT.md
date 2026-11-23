# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-11-23 04:09_

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
  "don_len": 15,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 26,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-4.86%**, PF 0.777, 70 trades, max DD -1043.82
- Optimizer out-of-sample: net **2.88%**, PF 1.445, 19 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-21 16:07 | 5000 | -7.87 | 0.661 | -0.09 | 0.991 | False |
| 2026-11-21 20:06 | 5000 | -7.85 | 0.662 | 0.86 | 1.125 | True |
| 2026-11-22 00:20 | 5000 | -7.01 | 0.697 | 2.71 | 1.443 | True |
| 2026-11-22 04:08 | 5000 | -6.61 | 0.711 | 2.67 | 1.443 | True |
| 2026-11-22 08:09 | 5000 | -6.61 | 0.711 | 2.38 | 1.379 | True |
| 2026-11-22 12:09 | 5000 | -6.12 | 0.732 | 2.91 | 1.46 | True |
| 2026-11-22 16:07 | 5000 | -5.63 | 0.749 | 2.93 | 1.464 | True |
| 2026-11-22 20:07 | 5000 | -5.93 | 0.738 | 2.88 | 1.445 | True |
| 2026-11-23 00:21 | 5000 | -4.42 | 0.798 | 2.88 | 1.445 | True |
| 2026-11-23 04:09 | 5000 | -4.86 | 0.777 | 2.88 | 1.445 | True |

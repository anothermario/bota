# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-11-24 04:09_

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

- Current-params net profit (full sample): **-6.19%**, PF 0.728, 70 trades, max DD -1039.14
- Optimizer out-of-sample: net **2.02%**, PF 1.278, 20 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-22 16:07 | 5000 | -5.63 | 0.749 | 2.93 | 1.464 | True |
| 2026-11-22 20:07 | 5000 | -5.93 | 0.738 | 2.88 | 1.445 | True |
| 2026-11-23 00:21 | 5000 | -4.42 | 0.798 | 2.88 | 1.445 | True |
| 2026-11-23 04:09 | 5000 | -4.86 | 0.777 | 2.88 | 1.445 | True |
| 2026-11-23 08:11 | 5000 | -4.85 | 0.777 | 2.88 | 1.445 | True |
| 2026-11-23 12:11 | 5000 | -4.86 | 0.777 | 2.88 | 1.445 | True |
| 2026-11-23 16:07 | 5000 | -6.18 | 0.728 | 1.9 | 1.256 | True |
| 2026-11-23 20:06 | 5000 | -6.2 | 0.728 | 1.89 | 1.256 | True |
| 2026-11-24 00:18 | 5000 | -6.19 | 0.728 | 2.03 | 1.279 | True |
| 2026-11-24 04:09 | 5000 | -6.19 | 0.728 | 2.02 | 1.278 | True |

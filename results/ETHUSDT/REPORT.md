# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-24 04:12_

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

- Current-params net profit (full sample): **-7.68%**, PF 0.685, 76 trades, max DD -1032.66
- Optimizer out-of-sample: net **-0.65%**, PF 0.901, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-22 16:13 | 5000 | -7.8 | 0.68 | 1.34 | 1.218 | True |
| 2026-10-22 20:11 | 5000 | -7.8 | 0.68 | 0.52 | 1.08 | True |
| 2026-10-23 00:30 | 5000 | -7.8 | 0.68 | 0.83 | 1.135 | True |
| 2026-10-23 04:13 | 5000 | -7.8 | 0.68 | 0.83 | 1.135 | True |
| 2026-10-23 08:15 | 5000 | -7.8 | 0.68 | 0.82 | 1.133 | True |
| 2026-10-23 12:15 | 5000 | -7.8 | 0.68 | 0.83 | 1.136 | True |
| 2026-10-23 16:12 | 5000 | -7.03 | 0.704 | 0.8 | 1.13 | True |
| 2026-10-23 20:11 | 5000 | -7.03 | 0.704 | 0.07 | 1.012 | True |
| 2026-10-24 00:28 | 5000 | -7.57 | 0.689 | -0.65 | 0.901 | False |
| 2026-10-24 04:12 | 5000 | -7.68 | 0.685 | -0.65 | 0.901 | False |

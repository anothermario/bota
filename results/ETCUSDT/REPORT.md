# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-23 12:17_

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

- Current-params net profit (full sample): **-3.09%**, PF 0.852, 54 trades, max DD -799.94
- Optimizer out-of-sample: net **-3.21%**, PF 0.603, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-22 00:31 | 5000 | -1.43 | 0.933 | -3.84 | 0.548 | False |
| 2026-09-22 04:13 | 5000 | -1.47 | 0.931 | -3.85 | 0.548 | False |
| 2026-09-22 08:16 | 5000 | -1.84 | 0.913 | -3.85 | 0.548 | False |
| 2026-09-22 12:17 | 5000 | -2.55 | 0.879 | -3.42 | 0.578 | False |
| 2026-09-22 16:11 | 5000 | -3.37 | 0.839 | -4.41 | 0.513 | False |
| 2026-09-22 20:10 | 5000 | -3.37 | 0.839 | -4.41 | 0.512 | False |
| 2026-09-23 00:29 | 5000 | -3.3 | 0.842 | -3.42 | 0.578 | False |
| 2026-09-23 04:14 | 5000 | -3.3 | 0.842 | -3.42 | 0.578 | False |
| 2026-09-23 08:16 | 5000 | -3.09 | 0.852 | -3.21 | 0.603 | False |
| 2026-09-23 12:17 | 5000 | -3.09 | 0.852 | -3.21 | 0.603 | False |

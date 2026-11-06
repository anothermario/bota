# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-11-06 20:07_

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

- Current-params net profit (full sample): **-9.33%**, PF 0.601, 73 trades, max DD -1401.31
- Optimizer out-of-sample: net **-6.09%**, PF 0.156, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-05 08:11 | 5000 | -9.78 | 0.591 | -6.01 | 0.186 | False |
| 2026-11-05 12:11 | 5000 | -9.76 | 0.591 | -6.01 | 0.186 | False |
| 2026-11-05 16:09 | 5000 | -9.81 | 0.588 | -6.22 | 0.224 | False |
| 2026-11-05 20:07 | 5000 | -9.8 | 0.589 | -6.72 | 0.21 | False |
| 2026-11-06 00:20 | 5000 | -10.83 | 0.552 | -5.46 | 0.255 | False |
| 2026-11-06 04:08 | 5000 | -9.69 | 0.591 | -4.81 | 0.342 | False |
| 2026-11-06 08:10 | 5000 | -9.69 | 0.591 | -4.83 | 0.339 | False |
| 2026-11-06 12:10 | 5000 | -9.33 | 0.601 | -6.37 | 0.15 | False |
| 2026-11-06 16:07 | 5000 | -9.33 | 0.601 | -6.09 | 0.156 | False |
| 2026-11-06 20:07 | 5000 | -9.33 | 0.601 | -6.09 | 0.156 | False |

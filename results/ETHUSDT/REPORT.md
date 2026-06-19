# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-06-19 13:16_

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
  "don_len": 15,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-10.09%**, PF 0.631, 89 trades, max DD -1318.71
- Optimizer out-of-sample: net **-0.98%**, PF 0.881, 24 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-18 00:58 | 5000 | -10.53 | 0.567 | -1.31 | 0.848 | False |
| 2026-06-18 05:40 | 5000 | -10.36 | 0.572 | 0.38 | 1.061 | True |
| 2026-06-18 09:34 | 5000 | -10.54 | 0.566 | -2.29 | 0.758 | False |
| 2026-06-18 13:15 | 5000 | -10.4 | 0.57 | 0.29 | 1.046 | True |
| 2026-06-18 17:07 | 5000 | -10.48 | 0.568 | 0.52 | 1.084 | True |
| 2026-06-18 20:53 | 5000 | -10.02 | 0.58 | 0.38 | 1.045 | True |
| 2026-06-19 01:03 | 5000 | -10.53 | 0.619 | -0.37 | 0.955 | False |
| 2026-06-19 05:47 | 5000 | -10.73 | 0.614 | -1.78 | 0.802 | False |
| 2026-06-19 09:39 | 5000 | -10.74 | 0.614 | -0.98 | 0.881 | False |
| 2026-06-19 13:16 | 5000 | -10.09 | 0.631 | -0.98 | 0.881 | False |

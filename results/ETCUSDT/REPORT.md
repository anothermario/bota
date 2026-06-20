# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-06-20 09:08_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.3,
  "use_adx": true,
  "adx_len": 14,
  "adx_thresh": 20.0,
  "don_len": 15,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 18,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-10.59%**, PF 0.615, 76 trades, max DD -1360.86
- Optimizer out-of-sample: net **1.68%**, PF 1.426, 14 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-18 20:53 | 5000 | -12.37 | 0.567 | -0.27 | 0.949 | False |
| 2026-06-19 01:03 | 5000 | -12.39 | 0.567 | -0.3 | 0.949 | False |
| 2026-06-19 05:47 | 5000 | -12.5 | 0.564 | -0.33 | 0.939 | False |
| 2026-06-19 09:39 | 5000 | -12.5 | 0.564 | -0.34 | 0.938 | False |
| 2026-06-19 13:16 | 5000 | -12.53 | 0.564 | 0.09 | 1.022 | False |
| 2026-06-19 16:52 | 5000 | -11.83 | 0.588 | 0.57 | 1.118 | True |
| 2026-06-19 20:35 | 5000 | -10.31 | 0.626 | 0.95 | 1.2 | True |
| 2026-06-20 00:53 | 5000 | -10.61 | 0.615 | 0.96 | 1.204 | True |
| 2026-06-20 05:33 | 5000 | -10.59 | 0.615 | 1.8 | 1.456 | False |
| 2026-06-20 09:08 | 5000 | -10.59 | 0.615 | 1.68 | 1.426 | False |

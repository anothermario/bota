# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-08-28 11:53_

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

- Current-params net profit (full sample): **-20.96%**, PF 0.302, 102 trades, max DD -2096.05
- Optimizer out-of-sample: net **-6.49%**, PF 0.052, 25 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-26 20:50 | 5000 | -21.65 | 0.292 | -6.77 | 0.091 | False |
| 2026-08-27 01:35 | 5000 | -21.68 | 0.292 | -6.13 | 0.101 | False |
| 2026-08-27 06:08 | 5000 | -21.87 | 0.29 | -5.14 | 0.081 | False |
| 2026-08-27 11:26 | 5000 | -21.21 | 0.299 | -6.34 | 0.098 | False |
| 2026-08-27 15:44 | 5000 | -21.05 | 0.301 | -6.33 | 0.099 | False |
| 2026-08-27 19:33 | 5000 | -21.04 | 0.301 | -6.72 | 0.05 | False |
| 2026-08-27 23:09 | 5000 | -21.04 | 0.301 | -6.64 | 0.051 | False |
| 2026-08-28 02:57 | 5000 | -20.96 | 0.302 | -6.64 | 0.051 | False |
| 2026-08-28 06:35 | 5000 | -20.96 | 0.302 | -6.49 | 0.052 | False |
| 2026-08-28 11:53 | 5000 | -20.96 | 0.302 | -6.49 | 0.052 | False |

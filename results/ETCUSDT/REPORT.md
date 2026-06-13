# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-06-13 05:35_

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
  "don_len": 20,
  "atr_len": 14,
  "atr_mult": 3.0,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-15.57%**, PF 0.469, 83 trades, max DD -1658.76
- Optimizer out-of-sample: net **-5.89%**, PF 0.203, 18 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-11 17:19 | 5000 | -16.19 | 0.471 | -6.92 | 0.26 | False |
| 2026-06-11 20:52 | 5000 | -16.19 | 0.471 | -6.92 | 0.26 | False |
| 2026-06-12 00:58 | 5000 | -15.46 | 0.485 | -5.26 | 0.32 | False |
| 2026-06-12 05:38 | 5000 | -15.01 | 0.494 | -4.49 | 0.424 | False |
| 2026-06-12 09:29 | 5000 | -15.01 | 0.494 | -5.2 | 0.328 | False |
| 2026-06-12 13:14 | 5000 | -14.99 | 0.494 | -6.58 | 0.241 | False |
| 2026-06-12 17:03 | 5000 | -13.99 | 0.527 | -6.16 | 0.196 | False |
| 2026-06-12 20:48 | 5000 | -13.96 | 0.528 | -6.96 | 0.194 | False |
| 2026-06-13 00:57 | 5000 | -15.16 | 0.48 | -6.06 | 0.199 | False |
| 2026-06-13 05:35 | 5000 | -15.57 | 0.469 | -5.89 | 0.203 | False |

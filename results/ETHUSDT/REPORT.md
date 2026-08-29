# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-08-29 08:13_

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

- Current-params net profit (full sample): **-19.91%**, PF 0.316, 99 trades, max DD -1990.85
- Optimizer out-of-sample: net **-5.51%**, PF 0.061, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-27 19:33 | 5000 | -21.04 | 0.301 | -6.72 | 0.05 | False |
| 2026-08-27 23:09 | 5000 | -21.04 | 0.301 | -6.64 | 0.051 | False |
| 2026-08-28 02:57 | 5000 | -20.96 | 0.302 | -6.64 | 0.051 | False |
| 2026-08-28 06:35 | 5000 | -20.96 | 0.302 | -6.49 | 0.052 | False |
| 2026-08-28 11:53 | 5000 | -20.96 | 0.302 | -6.49 | 0.052 | False |
| 2026-08-28 16:11 | 5000 | -20.42 | 0.309 | -6.06 | 0.056 | False |
| 2026-08-28 21:57 | 5000 | -20.42 | 0.309 | -5.51 | 0.061 | False |
| 2026-08-29 00:28 | 5000 | -20.43 | 0.309 | -5.51 | 0.061 | False |
| 2026-08-29 04:12 | 5000 | -20.44 | 0.309 | -4.52 | 0.027 | False |
| 2026-08-29 08:13 | 5000 | -19.91 | 0.316 | -5.51 | 0.061 | False |

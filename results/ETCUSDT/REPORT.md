# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-08 16:14_

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

- Current-params net profit (full sample): **-5.51%**, PF 0.777, 61 trades, max DD -1407.43
- Optimizer out-of-sample: net **-6.25%**, PF 0.247, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-07 04:15 | 5000 | -5.79 | 0.772 | -6.42 | 0.238 | False |
| 2026-10-07 08:17 | 5000 | -5.79 | 0.772 | -6.42 | 0.238 | False |
| 2026-10-07 12:19 | 5000 | -5.8 | 0.772 | -6.42 | 0.238 | False |
| 2026-10-07 16:13 | 5000 | -5.74 | 0.768 | -6.42 | 0.237 | False |
| 2026-10-07 20:13 | 5000 | -5.74 | 0.768 | -6.42 | 0.237 | False |
| 2026-10-08 00:33 | 5000 | -5.76 | 0.768 | -6.64 | 0.213 | False |
| 2026-10-08 04:15 | 5000 | -5.47 | 0.778 | -6.35 | 0.244 | False |
| 2026-10-08 08:18 | 5000 | -5.47 | 0.778 | -6.35 | 0.244 | False |
| 2026-10-08 12:18 | 5000 | -5.47 | 0.778 | -6.35 | 0.244 | False |
| 2026-10-08 16:14 | 5000 | -5.51 | 0.777 | -6.25 | 0.247 | False |

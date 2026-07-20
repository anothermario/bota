# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-20 02:51_

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
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-8.98%**, PF 0.648, 69 trades, max DD -1459.49
- Optimizer out-of-sample: net **-6.63%**, PF 0.27, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-18 13:12 | 5000 | -7.62 | 0.687 | -5.82 | 0.311 | False |
| 2026-07-18 16:57 | 5000 | -7.62 | 0.687 | -5.53 | 0.322 | False |
| 2026-07-18 20:45 | 5000 | -7.63 | 0.688 | -5.57 | 0.322 | False |
| 2026-07-19 02:35 | 5000 | -7.91 | 0.676 | -5.58 | 0.322 | False |
| 2026-07-19 06:29 | 5000 | -7.78 | 0.68 | -5.15 | 0.346 | False |
| 2026-07-19 09:51 | 5000 | -7.78 | 0.68 | -5.15 | 0.346 | False |
| 2026-07-19 13:15 | 5000 | -7.82 | 0.68 | -5.19 | 0.346 | False |
| 2026-07-19 16:57 | 5000 | -8.26 | 0.667 | -5.65 | 0.326 | False |
| 2026-07-19 20:45 | 5000 | -8.26 | 0.667 | -5.65 | 0.326 | False |
| 2026-07-20 02:51 | 5000 | -8.98 | 0.648 | -6.63 | 0.27 | False |

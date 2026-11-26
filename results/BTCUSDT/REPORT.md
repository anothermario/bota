# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-11-26 04:08_

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
  "don_len": 15,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 26,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-8.43%**, PF 0.655, 71 trades, max DD -1033.8
- Optimizer out-of-sample: net **2.09%**, PF 1.271, 20 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-24 16:08 | 5000 | -6.52 | 0.72 | 2.08 | 1.275 | True |
| 2026-11-24 20:07 | 5000 | -6.52 | 0.72 | 2.67 | 1.381 | True |
| 2026-11-25 00:19 | 5000 | -6.52 | 0.72 | 2.63 | 1.373 | True |
| 2026-11-25 04:09 | 5000 | -6.69 | 0.713 | 3.55 | 1.569 | True |
| 2026-11-25 08:10 | 5000 | -6.67 | 0.713 | 2.74 | 1.394 | True |
| 2026-11-25 12:11 | 5000 | -6.67 | 0.713 | 2.68 | 1.382 | True |
| 2026-11-25 16:09 | 5000 | -7.7 | 0.683 | 2.41 | 1.327 | True |
| 2026-11-25 20:07 | 5000 | -8.67 | 0.648 | 2.83 | 1.407 | True |
| 2026-11-26 00:18 | 5000 | -7.97 | 0.658 | 2.39 | 1.327 | True |
| 2026-11-26 04:08 | 5000 | -8.43 | 0.655 | 2.09 | 1.271 | True |

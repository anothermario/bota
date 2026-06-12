# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-06-12 05:38_

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
  "don_len": 20,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-7.2%**, PF 0.656, 64 trades, max DD -1216.85
- Optimizer out-of-sample: net **4.41%**, PF 2.139, 14 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-10 17:09 | 5000 | -6.37 | 0.684 | 2.18 | 1.367 | True |
| 2026-06-10 20:57 | 5000 | -6.95 | 0.664 | 2.14 | 1.349 | True |
| 2026-06-11 00:55 | 5000 | -6.95 | 0.664 | 3.39 | 1.682 | True |
| 2026-06-11 05:39 | 5000 | -6.98 | 0.664 | 2.68 | 1.484 | True |
| 2026-06-11 09:34 | 5000 | -6.98 | 0.664 | 2.7 | 1.488 | True |
| 2026-06-11 13:24 | 5000 | -7.01 | 0.662 | 2.7 | 1.481 | True |
| 2026-06-11 17:18 | 5000 | -7.01 | 0.662 | 3.07 | 1.58 | True |
| 2026-06-11 20:52 | 5000 | -7.0 | 0.662 | 3.07 | 1.581 | True |
| 2026-06-12 00:58 | 5000 | -7.02 | 0.662 | 3.34 | 1.664 | True |
| 2026-06-12 05:38 | 5000 | -7.2 | 0.656 | 4.41 | 2.139 | False |

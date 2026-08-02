# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-08-02 13:17_

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

- Current-params net profit (full sample): **-17.44%**, PF 0.466, 95 trades, max DD -2033.8
- Optimizer out-of-sample: net **-5.79%**, PF 0.388, 28 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-01 02:41 | 5000 | -18.26 | 0.45 | -6.0 | 0.375 | False |
| 2026-08-01 06:28 | 5000 | -17.66 | 0.46 | -6.19 | 0.367 | False |
| 2026-08-01 09:58 | 5000 | -18.23 | 0.45 | -6.61 | 0.27 | False |
| 2026-08-01 13:17 | 5000 | -17.22 | 0.468 | -5.7 | 0.388 | False |
| 2026-08-01 16:58 | 5000 | -17.16 | 0.469 | -5.58 | 0.394 | False |
| 2026-08-01 20:53 | 5000 | -17.25 | 0.469 | -6.09 | 0.373 | False |
| 2026-08-02 02:39 | 5000 | -17.9 | 0.458 | -5.53 | 0.399 | False |
| 2026-08-02 06:31 | 5000 | -17.89 | 0.458 | -5.53 | 0.399 | False |
| 2026-08-02 09:55 | 5000 | -17.44 | 0.466 | -5.79 | 0.388 | False |
| 2026-08-02 13:17 | 5000 | -17.44 | 0.466 | -5.79 | 0.388 | False |

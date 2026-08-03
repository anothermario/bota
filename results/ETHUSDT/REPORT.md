# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-08-03 02:41_

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

- Current-params net profit (full sample): **-17.75%**, PF 0.465, 98 trades, max DD -2020.39
- Optimizer out-of-sample: net **-7.09%**, PF 0.259, 26 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-01 13:17 | 5000 | -17.22 | 0.468 | -5.7 | 0.388 | False |
| 2026-08-01 16:58 | 5000 | -17.16 | 0.469 | -5.58 | 0.394 | False |
| 2026-08-01 20:53 | 5000 | -17.25 | 0.469 | -6.09 | 0.373 | False |
| 2026-08-02 02:39 | 5000 | -17.9 | 0.458 | -5.53 | 0.399 | False |
| 2026-08-02 06:31 | 5000 | -17.89 | 0.458 | -5.53 | 0.399 | False |
| 2026-08-02 09:55 | 5000 | -17.44 | 0.466 | -5.79 | 0.388 | False |
| 2026-08-02 13:17 | 5000 | -17.44 | 0.466 | -5.79 | 0.388 | False |
| 2026-08-02 16:57 | 5000 | -16.98 | 0.477 | -5.5 | 0.415 | False |
| 2026-08-02 20:54 | 5000 | -16.94 | 0.479 | -5.65 | 0.415 | False |
| 2026-08-03 02:41 | 5000 | -17.75 | 0.465 | -7.09 | 0.259 | False |

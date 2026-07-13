# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-13 11:09_

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

- Current-params net profit (full sample): **-6.99%**, PF 0.705, 67 trades, max DD -1191.79
- Optimizer out-of-sample: net **-3.37%**, PF 0.394, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-11 20:45 | 5000 | -7.16 | 0.701 | -2.43 | 0.474 | False |
| 2026-07-12 02:39 | 5000 | -7.69 | 0.686 | -2.97 | 0.424 | False |
| 2026-07-12 06:31 | 5000 | -7.66 | 0.687 | -2.97 | 0.424 | False |
| 2026-07-12 09:50 | 5000 | -6.8 | 0.714 | -2.97 | 0.424 | False |
| 2026-07-12 13:17 | 5000 | -6.8 | 0.714 | -2.97 | 0.424 | False |
| 2026-07-12 16:57 | 5000 | -6.81 | 0.714 | -2.97 | 0.424 | False |
| 2026-07-12 20:44 | 5000 | -6.81 | 0.714 | -2.97 | 0.424 | False |
| 2026-07-13 02:40 | 5000 | -7.19 | 0.702 | -3.37 | 0.394 | False |
| 2026-07-13 06:52 | 5000 | -6.71 | 0.718 | -3.37 | 0.394 | False |
| 2026-07-13 11:09 | 5000 | -6.99 | 0.705 | -3.37 | 0.394 | False |

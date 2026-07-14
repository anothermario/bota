# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-14 06:10_

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

- Current-params net profit (full sample): **-8.84%**, PF 0.637, 67 trades, max DD -1297.54
- Optimizer out-of-sample: net **-4.54%**, PF 0.326, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-12 16:57 | 5000 | -6.81 | 0.714 | -2.97 | 0.424 | False |
| 2026-07-12 20:44 | 5000 | -6.81 | 0.714 | -2.97 | 0.424 | False |
| 2026-07-13 02:40 | 5000 | -7.19 | 0.702 | -3.37 | 0.394 | False |
| 2026-07-13 06:52 | 5000 | -6.71 | 0.718 | -3.37 | 0.394 | False |
| 2026-07-13 11:09 | 5000 | -6.99 | 0.705 | -3.37 | 0.394 | False |
| 2026-07-13 14:32 | 5000 | -8.09 | 0.658 | -3.41 | 0.394 | False |
| 2026-07-13 17:53 | 5000 | -8.65 | 0.641 | -3.85 | 0.362 | False |
| 2026-07-13 20:56 | 5000 | -8.47 | 0.647 | -3.89 | 0.362 | False |
| 2026-07-14 02:24 | 5000 | -8.84 | 0.637 | -4.54 | 0.326 | False |
| 2026-07-14 06:10 | 5000 | -8.84 | 0.637 | -4.54 | 0.326 | False |

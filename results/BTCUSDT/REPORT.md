# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-06-26 05:29_

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

- Current-params net profit (full sample): **-7.01%**, PF 0.699, 66 trades, max DD -741.84
- Optimizer out-of-sample: net **-5.84%**, PF 0.417, 25 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-24 16:47 | 5000 | -7.66 | 0.652 | -5.65 | 0.37 | False |
| 2026-06-24 20:37 | 5000 | -5.56 | 0.745 | -4.52 | 0.489 | False |
| 2026-06-25 00:51 | 5000 | -5.56 | 0.745 | -4.69 | 0.469 | False |
| 2026-06-25 05:24 | 5000 | -5.17 | 0.759 | -4.69 | 0.469 | False |
| 2026-06-25 09:10 | 5000 | -5.21 | 0.759 | -4.73 | 0.469 | False |
| 2026-06-25 12:51 | 5000 | -5.91 | 0.734 | -5.43 | 0.433 | False |
| 2026-06-25 16:49 | 5000 | -6.98 | 0.7 | -6.51 | 0.389 | False |
| 2026-06-25 20:42 | 5000 | -6.98 | 0.7 | -6.51 | 0.389 | False |
| 2026-06-26 00:53 | 5000 | -6.98 | 0.7 | -5.84 | 0.417 | False |
| 2026-06-26 05:29 | 5000 | -7.01 | 0.699 | -5.84 | 0.417 | False |

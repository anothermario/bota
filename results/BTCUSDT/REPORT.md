# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-27 11:19_

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

- Current-params net profit (full sample): **-15.63%**, PF 0.412, 72 trades, max DD -1629.87
- Optimizer out-of-sample: net **-6.38%**, PF 0.349, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-25 20:51 | 5000 | -15.97 | 0.404 | -6.13 | 0.359 | False |
| 2026-07-26 02:40 | 5000 | -16.1 | 0.402 | -6.28 | 0.351 | False |
| 2026-07-26 06:35 | 5000 | -15.28 | 0.417 | -6.3 | 0.351 | False |
| 2026-07-26 09:58 | 5000 | -15.28 | 0.417 | -6.28 | 0.351 | False |
| 2026-07-26 13:19 | 5000 | -15.28 | 0.417 | -6.28 | 0.351 | False |
| 2026-07-26 16:59 | 5000 | -15.28 | 0.417 | -6.28 | 0.351 | False |
| 2026-07-26 20:56 | 5000 | -15.28 | 0.417 | -6.11 | 0.358 | False |
| 2026-07-27 02:48 | 5000 | -15.39 | 0.415 | -6.24 | 0.354 | False |
| 2026-07-27 07:29 | 5000 | -15.42 | 0.415 | -6.52 | 0.344 | False |
| 2026-07-27 11:19 | 5000 | -15.63 | 0.412 | -6.38 | 0.349 | False |

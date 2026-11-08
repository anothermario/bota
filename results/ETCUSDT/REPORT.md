# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-11-08 04:08_

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

- Current-params net profit (full sample): **-12.59%**, PF 0.502, 67 trades, max DD -1558.33
- Optimizer out-of-sample: net **-7.19%**, PF 0.28, 29 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-06 16:08 | 5000 | -12.58 | 0.502 | -4.7 | 0.477 | False |
| 2026-11-06 20:07 | 5000 | -12.58 | 0.502 | -4.7 | 0.477 | False |
| 2026-11-07 00:17 | 5000 | -12.58 | 0.502 | -4.53 | 0.486 | False |
| 2026-11-07 04:08 | 5000 | -12.58 | 0.502 | -4.54 | 0.486 | False |
| 2026-11-07 08:09 | 5000 | -12.58 | 0.502 | -4.52 | 0.487 | False |
| 2026-11-07 12:10 | 5000 | -12.58 | 0.502 | -5.44 | 0.417 | False |
| 2026-11-07 16:07 | 5000 | -12.57 | 0.502 | -4.88 | 0.446 | False |
| 2026-11-07 20:06 | 5000 | -12.58 | 0.502 | -4.87 | 0.446 | False |
| 2026-11-08 00:21 | 5000 | -12.58 | 0.502 | -4.88 | 0.446 | False |
| 2026-11-08 04:08 | 5000 | -12.59 | 0.502 | -7.19 | 0.28 | False |

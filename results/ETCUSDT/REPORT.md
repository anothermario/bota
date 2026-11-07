# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-11-07 16:07_

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

- Current-params net profit (full sample): **-12.57%**, PF 0.502, 67 trades, max DD -1558.51
- Optimizer out-of-sample: net **-4.88%**, PF 0.446, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-06 04:09 | 5000 | -13.0 | 0.493 | -1.23 | 0.865 | False |
| 2026-11-06 08:10 | 5000 | -13.0 | 0.493 | -1.95 | 0.785 | False |
| 2026-11-06 12:10 | 5000 | -12.58 | 0.502 | -3.16 | 0.647 | False |
| 2026-11-06 16:08 | 5000 | -12.58 | 0.502 | -4.7 | 0.477 | False |
| 2026-11-06 20:07 | 5000 | -12.58 | 0.502 | -4.7 | 0.477 | False |
| 2026-11-07 00:17 | 5000 | -12.58 | 0.502 | -4.53 | 0.486 | False |
| 2026-11-07 04:08 | 5000 | -12.58 | 0.502 | -4.54 | 0.486 | False |
| 2026-11-07 08:09 | 5000 | -12.58 | 0.502 | -4.52 | 0.487 | False |
| 2026-11-07 12:10 | 5000 | -12.58 | 0.502 | -5.44 | 0.417 | False |
| 2026-11-07 16:07 | 5000 | -12.57 | 0.502 | -4.88 | 0.446 | False |

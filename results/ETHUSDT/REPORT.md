# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-16 12:17_

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

- Current-params net profit (full sample): **-15.81%**, PF 0.43, 103 trades, max DD -1710.82
- Optimizer out-of-sample: net **-5.59%**, PF 0.494, 34 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-15 00:32 | 5000 | -16.15 | 0.43 | -6.17 | 0.463 | False |
| 2026-09-15 04:13 | 5000 | -15.92 | 0.434 | -5.85 | 0.477 | False |
| 2026-09-15 08:16 | 5000 | -15.95 | 0.434 | -6.95 | 0.393 | False |
| 2026-09-15 12:16 | 5000 | -16.44 | 0.422 | -6.33 | 0.415 | False |
| 2026-09-15 16:12 | 5000 | -15.73 | 0.441 | -6.19 | 0.444 | False |
| 2026-09-15 20:11 | 5000 | -15.25 | 0.458 | -5.64 | 0.492 | False |
| 2026-09-16 00:30 | 5000 | -15.55 | 0.452 | -5.94 | 0.478 | False |
| 2026-09-16 04:13 | 5000 | -15.26 | 0.458 | -6.95 | 0.437 | False |
| 2026-09-16 08:16 | 5000 | -15.29 | 0.457 | -6.29 | 0.463 | False |
| 2026-09-16 12:17 | 5000 | -15.81 | 0.43 | -5.59 | 0.494 | False |

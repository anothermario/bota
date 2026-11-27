# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-11-27 20:07_

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

- Current-params net profit (full sample): **-10.84%**, PF 0.555, 74 trades, max DD -1397.8
- Optimizer out-of-sample: net **-6.69%**, PF 0.425, 25 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-26 08:10 | 5000 | -11.44 | 0.537 | -5.57 | 0.486 | False |
| 2026-11-26 12:10 | 5000 | -10.86 | 0.551 | -5.57 | 0.486 | False |
| 2026-11-26 16:08 | 5000 | -11.45 | 0.538 | -6.16 | 0.461 | False |
| 2026-11-26 20:07 | 5000 | -10.94 | 0.551 | -6.16 | 0.461 | False |
| 2026-11-27 00:19 | 5000 | -11.24 | 0.543 | -6.16 | 0.461 | False |
| 2026-11-27 04:08 | 5000 | -10.73 | 0.556 | -5.77 | 0.48 | False |
| 2026-11-27 08:09 | 5000 | -10.73 | 0.556 | -5.87 | 0.468 | False |
| 2026-11-27 12:11 | 5000 | -10.72 | 0.556 | -5.86 | 0.468 | False |
| 2026-11-27 16:07 | 5000 | -10.84 | 0.555 | -6.5 | 0.443 | False |
| 2026-11-27 20:07 | 5000 | -10.84 | 0.555 | -6.69 | 0.425 | False |

# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-11-12 00:19_

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

- Current-params net profit (full sample): **-13.79%**, PF 0.412, 75 trades, max DD -1483.32
- Optimizer out-of-sample: net **-6.34%**, PF 0.149, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-10 12:10 | 5000 | -12.01 | 0.479 | -5.18 | 0.176 | False |
| 2026-11-10 16:08 | 5000 | -12.76 | 0.447 | -5.34 | 0.172 | False |
| 2026-11-10 20:07 | 5000 | -12.76 | 0.447 | -5.34 | 0.172 | False |
| 2026-11-11 00:19 | 5000 | -13.25 | 0.438 | -5.9 | 0.158 | False |
| 2026-11-11 04:08 | 5000 | -13.26 | 0.437 | -5.9 | 0.158 | False |
| 2026-11-11 08:10 | 5000 | -13.24 | 0.438 | -6.82 | 0.138 | False |
| 2026-11-11 12:11 | 5000 | -13.82 | 0.41 | -6.81 | 0.138 | False |
| 2026-11-11 16:07 | 5000 | -13.82 | 0.41 | -5.96 | 0.156 | False |
| 2026-11-11 20:07 | 5000 | -13.41 | 0.418 | -5.98 | 0.156 | False |
| 2026-11-12 00:19 | 5000 | -13.79 | 0.412 | -6.34 | 0.149 | False |

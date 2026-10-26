# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-26 04:14_

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

- Current-params net profit (full sample): **-11.25%**, PF 0.558, 66 trades, max DD -1586.77
- Optimizer out-of-sample: net **-4.8%**, PF 0.501, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-24 16:10 | 5000 | -10.85 | 0.573 | -4.08 | 0.514 | False |
| 2026-10-24 20:09 | 5000 | -9.78 | 0.614 | -2.93 | 0.648 | False |
| 2026-10-25 00:31 | 5000 | -9.77 | 0.614 | -2.93 | 0.648 | False |
| 2026-10-25 04:12 | 5000 | -9.81 | 0.613 | -2.93 | 0.648 | False |
| 2026-10-25 08:13 | 5000 | -10.14 | 0.598 | -4.84 | 0.497 | False |
| 2026-10-25 12:14 | 5000 | -11.23 | 0.558 | -4.88 | 0.496 | False |
| 2026-10-25 16:11 | 5000 | -11.23 | 0.558 | -5.3 | 0.474 | False |
| 2026-10-25 20:10 | 5000 | -11.23 | 0.558 | -4.87 | 0.496 | False |
| 2026-10-26 00:30 | 5000 | -11.78 | 0.545 | -5.22 | 0.478 | False |
| 2026-10-26 04:14 | 5000 | -11.25 | 0.558 | -4.8 | 0.501 | False |

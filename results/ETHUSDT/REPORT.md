# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-03 17:22_

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

- Current-params net profit (full sample): **-15.1%**, PF 0.48, 96 trades, max DD -1572.58
- Optimizer out-of-sample: net **-3.64%**, PF 0.626, 26 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-02 04:14 | 5000 | -14.32 | 0.499 | -1.9 | 0.775 | False |
| 2026-10-02 08:16 | 5000 | -15.15 | 0.485 | -3.72 | 0.636 | False |
| 2026-10-02 12:18 | 5000 | -15.61 | 0.477 | -5.68 | 0.53 | False |
| 2026-10-02 16:12 | 5000 | -15.16 | 0.486 | -4.82 | 0.604 | False |
| 2026-10-02 20:11 | 5000 | -15.16 | 0.486 | -4.2 | 0.639 | False |
| 2026-10-03 00:30 | 5000 | -14.49 | 0.508 | -2.25 | 0.785 | False |
| 2026-10-03 04:17 | 5000 | -15.15 | 0.483 | -1.95 | 0.817 | False |
| 2026-10-03 08:15 | 5000 | -15.71 | 0.469 | -3.74 | 0.577 | False |
| 2026-10-03 13:44 | 5000 | -15.33 | 0.476 | -2.41 | 0.757 | False |
| 2026-10-03 17:22 | 5000 | -15.1 | 0.48 | -3.64 | 0.626 | False |

# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-18 04:12_

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

- Current-params net profit (full sample): **-12.07%**, PF 0.615, 103 trades, max DD -1387.78
- Optimizer out-of-sample: net **-0.44%**, PF 0.925, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-16 16:12 | 5000 | -12.73 | 0.593 | -1.35 | 0.803 | False |
| 2026-10-16 20:10 | 5000 | -12.59 | 0.597 | -1.37 | 0.803 | False |
| 2026-10-17 00:28 | 5000 | -12.82 | 0.592 | -1.63 | 0.772 | False |
| 2026-10-17 04:12 | 5000 | -12.82 | 0.592 | -1.93 | 0.74 | False |
| 2026-10-17 08:12 | 5000 | -11.85 | 0.614 | -0.81 | 0.873 | False |
| 2026-10-17 12:14 | 5000 | -11.85 | 0.614 | -0.63 | 0.899 | False |
| 2026-10-17 16:10 | 5000 | -11.9 | 0.614 | -0.3 | 0.954 | False |
| 2026-10-17 20:10 | 5000 | -11.28 | 0.63 | -0.4 | 0.931 | False |
| 2026-10-18 00:32 | 5000 | -12.05 | 0.614 | -0.93 | 0.853 | False |
| 2026-10-18 04:12 | 5000 | -12.07 | 0.615 | -0.44 | 0.925 | False |

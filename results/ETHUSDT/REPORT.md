# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-25 04:12_

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

- Current-params net profit (full sample): **-7.6%**, PF 0.69, 77 trades, max DD -1040.3
- Optimizer out-of-sample: net **-1.3%**, PF 0.826, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-23 16:12 | 5000 | -7.03 | 0.704 | 0.8 | 1.13 | True |
| 2026-10-23 20:11 | 5000 | -7.03 | 0.704 | 0.07 | 1.012 | True |
| 2026-10-24 00:28 | 5000 | -7.57 | 0.689 | -0.65 | 0.901 | False |
| 2026-10-24 04:12 | 5000 | -7.68 | 0.685 | -0.65 | 0.901 | False |
| 2026-10-24 08:13 | 5000 | -6.99 | 0.707 | -0.65 | 0.901 | False |
| 2026-10-24 12:14 | 5000 | -7.03 | 0.707 | -0.69 | 0.901 | False |
| 2026-10-24 16:10 | 5000 | -7.3 | 0.699 | -0.98 | 0.863 | False |
| 2026-10-24 20:09 | 5000 | -7.56 | 0.69 | -1.26 | 0.826 | False |
| 2026-10-25 00:31 | 5000 | -7.55 | 0.69 | -1.26 | 0.826 | False |
| 2026-10-25 04:12 | 5000 | -7.6 | 0.69 | -1.3 | 0.826 | False |

# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-06 04:13_

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

- Current-params net profit (full sample): **-3.27%**, PF 0.842, 52 trades, max DD -712.87
- Optimizer out-of-sample: net **-0.4%**, PF 0.942, 15 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-04 16:12 | 5000 | -5.23 | 0.751 | 1.67 | 1.256 | False |
| 2026-09-04 20:11 | 5000 | -5.28 | 0.749 | 1.63 | 1.245 | True |
| 2026-09-05 00:30 | 5000 | -4.4 | 0.783 | 1.33 | 1.191 | True |
| 2026-09-05 04:12 | 5000 | -4.43 | 0.783 | 2.29 | 1.383 | False |
| 2026-09-05 08:13 | 5000 | -3.94 | 0.803 | 2.24 | 1.375 | False |
| 2026-09-05 12:14 | 5000 | -2.35 | 0.882 | 1.77 | 1.296 | True |
| 2026-09-05 16:10 | 5000 | -2.35 | 0.882 | 0.55 | 1.078 | True |
| 2026-09-05 20:10 | 5000 | -3.04 | 0.851 | 1.8 | 1.304 | False |
| 2026-09-06 00:34 | 5000 | -3.97 | 0.814 | 0.87 | 1.126 | True |
| 2026-09-06 04:13 | 5000 | -3.27 | 0.842 | -0.4 | 0.942 | False |

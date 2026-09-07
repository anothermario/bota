# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-07 00:33_

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

- Current-params net profit (full sample): **-2.47%**, PF 0.879, 51 trades, max DD -632.64
- Optimizer out-of-sample: net **-3.91%**, PF 0.41, 14 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-05 12:14 | 5000 | -2.35 | 0.882 | 1.77 | 1.296 | True |
| 2026-09-05 16:10 | 5000 | -2.35 | 0.882 | 0.55 | 1.078 | True |
| 2026-09-05 20:10 | 5000 | -3.04 | 0.851 | 1.8 | 1.304 | False |
| 2026-09-06 00:34 | 5000 | -3.97 | 0.814 | 0.87 | 1.126 | True |
| 2026-09-06 04:13 | 5000 | -3.27 | 0.842 | -0.4 | 0.942 | False |
| 2026-09-06 08:13 | 5000 | -3.27 | 0.842 | -4.31 | 0.384 | False |
| 2026-09-06 12:15 | 5000 | -3.27 | 0.842 | -3.88 | 0.41 | False |
| 2026-09-06 16:10 | 5000 | -3.84 | 0.819 | -3.88 | 0.41 | False |
| 2026-09-06 20:10 | 5000 | -3.27 | 0.842 | -3.88 | 0.41 | False |
| 2026-09-07 00:33 | 5000 | -2.47 | 0.879 | -3.91 | 0.41 | False |

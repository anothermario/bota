# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-10-24 00:28_

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
  "atr_mult": 3.0,
  "chand_len": 18,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-7.69%**, PF 0.651, 67 trades, max DD -1152.38
- Optimizer out-of-sample: net **-2.23%**, PF 0.697, 26 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-22 12:17 | 5000 | -11.62 | 0.501 | 0.06 | 1.016 | True |
| 2026-10-22 16:13 | 5000 | -8.19 | 0.634 | -0.6 | 0.869 | False |
| 2026-10-22 20:11 | 5000 | -8.19 | 0.634 | -0.57 | 0.875 | False |
| 2026-10-23 00:30 | 5000 | -8.19 | 0.634 | -0.41 | 0.907 | False |
| 2026-10-23 04:13 | 5000 | -8.19 | 0.634 | -0.41 | 0.907 | False |
| 2026-10-23 08:15 | 5000 | -8.19 | 0.634 | -1.65 | 0.763 | False |
| 2026-10-23 12:15 | 5000 | -8.19 | 0.634 | -0.41 | 0.907 | False |
| 2026-10-23 16:12 | 5000 | -7.29 | 0.663 | -0.41 | 0.907 | False |
| 2026-10-23 20:11 | 5000 | -7.29 | 0.663 | -0.41 | 0.907 | False |
| 2026-10-24 00:28 | 5000 | -7.69 | 0.651 | -2.23 | 0.697 | False |

# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-10-01 16:12_

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
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-10.35%**, PF 0.543, 67 trades, max DD -1123.46
- Optimizer out-of-sample: net **-3.17%**, PF 0.624, 26 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-30 04:14 | 5000 | -9.3 | 0.578 | -0.51 | 0.928 | False |
| 2026-09-30 08:16 | 5000 | -8.95 | 0.593 | -1.11 | 0.843 | False |
| 2026-09-30 12:21 | 5000 | -8.95 | 0.593 | -2.56 | 0.695 | False |
| 2026-09-30 16:13 | 5000 | -9.29 | 0.584 | -3.31 | 0.613 | False |
| 2026-09-30 20:13 | 5000 | -9.29 | 0.584 | -2.95 | 0.641 | False |
| 2026-10-01 00:38 | 5000 | -9.17 | 0.59 | -2.91 | 0.644 | False |
| 2026-10-01 04:14 | 5000 | -9.17 | 0.59 | -2.91 | 0.644 | False |
| 2026-10-01 08:17 | 5000 | -9.99 | 0.561 | -3.17 | 0.624 | False |
| 2026-10-01 12:18 | 5000 | -10.35 | 0.543 | -3.17 | 0.624 | False |
| 2026-10-01 16:12 | 5000 | -10.35 | 0.543 | -3.17 | 0.624 | False |

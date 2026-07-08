# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-08 02:35_

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

- Current-params net profit (full sample): **-6.31%**, PF 0.727, 65 trades, max DD -903.02
- Optimizer out-of-sample: net **-1.53%**, PF 0.773, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-06 15:30 | 5000 | -6.56 | 0.718 | -2.88 | 0.636 | False |
| 2026-07-06 18:10 | 5000 | -6.55 | 0.719 | -2.47 | 0.671 | False |
| 2026-07-06 21:28 | 5000 | -6.55 | 0.719 | -2.47 | 0.671 | False |
| 2026-07-07 03:17 | 5000 | -6.75 | 0.712 | -2.03 | 0.718 | False |
| 2026-07-07 07:36 | 5000 | -6.74 | 0.712 | -1.72 | 0.748 | False |
| 2026-07-07 10:54 | 5000 | -6.55 | 0.718 | -1.72 | 0.747 | False |
| 2026-07-07 14:31 | 5000 | -6.55 | 0.718 | -1.24 | 0.813 | False |
| 2026-07-07 17:58 | 5000 | -6.55 | 0.718 | -1.27 | 0.809 | False |
| 2026-07-07 21:23 | 5000 | -6.28 | 0.727 | -1.5 | 0.773 | False |
| 2026-07-08 02:35 | 5000 | -6.31 | 0.727 | -1.53 | 0.773 | False |

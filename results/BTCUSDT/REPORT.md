# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-06-28 09:06_

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

- Current-params net profit (full sample): **-6.61%**, PF 0.715, 65 trades, max DD -841.31
- Optimizer out-of-sample: net **-6.96%**, PF 0.375, 26 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-26 20:37 | 5000 | -7.47 | 0.687 | -6.96 | 0.375 | False |
| 2026-06-27 00:50 | 5000 | -7.47 | 0.687 | -6.96 | 0.375 | False |
| 2026-06-27 05:21 | 5000 | -7.71 | 0.68 | -6.96 | 0.375 | False |
| 2026-06-27 08:59 | 5000 | -7.29 | 0.693 | -6.96 | 0.375 | False |
| 2026-06-27 12:31 | 5000 | -7.29 | 0.693 | -6.96 | 0.375 | False |
| 2026-06-27 16:27 | 5000 | -7.29 | 0.693 | -6.96 | 0.375 | False |
| 2026-06-27 20:27 | 5000 | -7.29 | 0.693 | -6.96 | 0.375 | False |
| 2026-06-28 00:53 | 5000 | -7.32 | 0.692 | -6.96 | 0.375 | False |
| 2026-06-28 05:33 | 5000 | -6.61 | 0.715 | -6.96 | 0.375 | False |
| 2026-06-28 09:06 | 5000 | -6.61 | 0.715 | -6.96 | 0.375 | False |

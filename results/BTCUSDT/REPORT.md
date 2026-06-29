# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-06-29 00:54_

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

- Current-params net profit (full sample): **-6.63%**, PF 0.714, 66 trades, max DD -845.09
- Optimizer out-of-sample: net **-7.06%**, PF 0.367, 26 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-27 12:31 | 5000 | -7.29 | 0.693 | -6.96 | 0.375 | False |
| 2026-06-27 16:27 | 5000 | -7.29 | 0.693 | -6.96 | 0.375 | False |
| 2026-06-27 20:27 | 5000 | -7.29 | 0.693 | -6.96 | 0.375 | False |
| 2026-06-28 00:53 | 5000 | -7.32 | 0.692 | -6.96 | 0.375 | False |
| 2026-06-28 05:33 | 5000 | -6.61 | 0.715 | -6.96 | 0.375 | False |
| 2026-06-28 09:06 | 5000 | -6.61 | 0.715 | -6.96 | 0.375 | False |
| 2026-06-28 12:33 | 5000 | -6.61 | 0.715 | -6.95 | 0.375 | False |
| 2026-06-28 16:29 | 5000 | -6.61 | 0.715 | -6.96 | 0.375 | False |
| 2026-06-28 20:29 | 5000 | -6.64 | 0.715 | -7.43 | 0.356 | False |
| 2026-06-29 00:54 | 5000 | -6.63 | 0.714 | -7.06 | 0.367 | False |

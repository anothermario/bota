# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-06-11 05:39_

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
  "don_len": 20,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-6.98%**, PF 0.664, 63 trades, max DD -1219.27
- Optimizer out-of-sample: net **2.68%**, PF 1.484, 16 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-09 16:58 | 5000 | -17.33 | 0.365 | 1.41 | 1.239 | True |
| 2026-06-09 20:44 | 5000 | -6.98 | 0.661 | 2.58 | 1.428 | True |
| 2026-06-10 00:55 | 5000 | -6.98 | 0.661 | 2.58 | 1.428 | True |
| 2026-06-10 05:36 | 5000 | -6.97 | 0.661 | 2.58 | 1.427 | True |
| 2026-06-10 09:18 | 5000 | -7.06 | 0.659 | 3.26 | 1.671 | False |
| 2026-06-10 13:15 | 5000 | -6.34 | 0.684 | 2.21 | 1.368 | True |
| 2026-06-10 17:09 | 5000 | -6.37 | 0.684 | 2.18 | 1.367 | True |
| 2026-06-10 20:57 | 5000 | -6.95 | 0.664 | 2.14 | 1.349 | True |
| 2026-06-11 00:55 | 5000 | -6.95 | 0.664 | 3.39 | 1.682 | True |
| 2026-06-11 05:39 | 5000 | -6.98 | 0.664 | 2.68 | 1.484 | True |

# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-24 12:17_

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

- Current-params net profit (full sample): **-6.69%**, PF 0.652, 65 trades, max DD -902.39
- Optimizer out-of-sample: net **-1.64%**, PF 0.788, 25 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-23 00:28 | 5000 | -6.36 | 0.673 | -2.16 | 0.722 | False |
| 2026-09-23 04:13 | 5000 | -6.36 | 0.673 | -2.16 | 0.722 | False |
| 2026-09-23 08:16 | 5000 | -5.98 | 0.687 | -2.77 | 0.666 | False |
| 2026-09-23 12:17 | 5000 | -6.02 | 0.687 | -2.2 | 0.722 | False |
| 2026-09-23 16:13 | 5000 | -6.27 | 0.678 | -2.17 | 0.726 | False |
| 2026-09-23 20:12 | 5000 | -5.92 | 0.695 | -1.67 | 0.785 | False |
| 2026-09-24 00:30 | 5000 | -6.58 | 0.661 | -1.67 | 0.785 | False |
| 2026-09-24 04:13 | 5000 | -6.42 | 0.667 | -2.08 | 0.745 | False |
| 2026-09-24 08:16 | 5000 | -6.96 | 0.642 | -2.04 | 0.748 | False |
| 2026-09-24 12:17 | 5000 | -6.69 | 0.652 | -1.64 | 0.788 | False |

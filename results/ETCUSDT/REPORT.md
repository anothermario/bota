# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-03 00:30_

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

- Current-params net profit (full sample): **-4.12%**, PF 0.83, 61 trades, max DD -1166.04
- Optimizer out-of-sample: net **-3.43%**, PF 0.552, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-01 12:19 | 5000 | -3.78 | 0.839 | -3.9 | 0.498 | False |
| 2026-10-01 16:13 | 5000 | -3.78 | 0.839 | -3.9 | 0.498 | False |
| 2026-10-01 20:13 | 5000 | -3.78 | 0.839 | -3.9 | 0.498 | False |
| 2026-10-02 00:33 | 5000 | -3.78 | 0.839 | -3.9 | 0.498 | False |
| 2026-10-02 04:14 | 5000 | -3.78 | 0.839 | -3.9 | 0.498 | False |
| 2026-10-02 08:16 | 5000 | -3.8 | 0.839 | -3.92 | 0.498 | False |
| 2026-10-02 12:18 | 5000 | -3.83 | 0.837 | -3.96 | 0.494 | False |
| 2026-10-02 16:12 | 5000 | -3.83 | 0.837 | -3.94 | 0.495 | False |
| 2026-10-02 20:11 | 5000 | -3.53 | 0.851 | -2.84 | 0.598 | False |
| 2026-10-03 00:30 | 5000 | -4.12 | 0.83 | -3.43 | 0.552 | False |

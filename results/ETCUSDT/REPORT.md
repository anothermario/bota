# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-06-16 09:51_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.3,
  "use_adx": true,
  "adx_len": 14,
  "adx_thresh": 20.0,
  "don_len": 20,
  "atr_len": 14,
  "atr_mult": 3.0,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-12.31%**, PF 0.568, 83 trades, max DD -1624.82
- Optimizer out-of-sample: net **-1.53%**, PF 0.765, 17 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-14 20:32 | 5000 | -15.97 | 0.438 | -5.05 | 0.232 | False |
| 2026-06-15 00:59 | 5000 | -16.1 | 0.435 | -5.09 | 0.23 | False |
| 2026-06-15 05:52 | 5000 | -16.56 | 0.427 | -5.09 | 0.23 | False |
| 2026-06-15 10:12 | 5000 | -16.1 | 0.435 | -5.09 | 0.23 | False |
| 2026-06-15 14:12 | 5000 | -16.1 | 0.435 | -5.09 | 0.23 | False |
| 2026-06-15 17:41 | 5000 | -16.1 | 0.435 | -5.09 | 0.23 | False |
| 2026-06-15 21:05 | 5000 | -12.31 | 0.568 | -1.95 | 0.718 | False |
| 2026-06-16 01:04 | 5000 | -12.31 | 0.568 | -1.57 | 0.761 | False |
| 2026-06-16 05:54 | 5000 | -12.31 | 0.568 | -1.57 | 0.761 | False |
| 2026-06-16 09:51 | 5000 | -12.31 | 0.568 | -1.53 | 0.765 | False |

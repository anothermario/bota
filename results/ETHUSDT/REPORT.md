# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-02 20:11_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.25,
  "use_adx": true,
  "adx_len": 14,
  "adx_thresh": 20.0,
  "don_len": 15,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-15.16%**, PF 0.486, 97 trades, max DD -1610.92
- Optimizer out-of-sample: net **-4.2%**, PF 0.639, 27 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-01 08:17 | 5000 | -13.24 | 0.543 | -3.31 | 0.661 | False |
| 2026-10-01 12:19 | 5000 | -14.34 | 0.498 | -3.31 | 0.661 | False |
| 2026-10-01 16:12 | 5000 | -14.34 | 0.498 | -4.09 | 0.61 | False |
| 2026-10-01 20:13 | 5000 | -14.34 | 0.498 | -4.2 | 0.603 | False |
| 2026-10-02 00:33 | 5000 | -14.33 | 0.498 | -3.31 | 0.661 | False |
| 2026-10-02 04:14 | 5000 | -14.32 | 0.499 | -1.9 | 0.775 | False |
| 2026-10-02 08:16 | 5000 | -15.15 | 0.485 | -3.72 | 0.636 | False |
| 2026-10-02 12:18 | 5000 | -15.61 | 0.477 | -5.68 | 0.53 | False |
| 2026-10-02 16:12 | 5000 | -15.16 | 0.486 | -4.82 | 0.604 | False |
| 2026-10-02 20:11 | 5000 | -15.16 | 0.486 | -4.2 | 0.639 | False |

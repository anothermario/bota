# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-02 16:13_

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

- Current-params net profit (full sample): **-19.67%**, PF 0.311, 100 trades, max DD -1966.59
- Optimizer out-of-sample: net **-7.15%**, PF 0.047, 25 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-01 04:13 | 5000 | -19.18 | 0.32 | -7.09 | 0.13 | False |
| 2026-09-01 08:16 | 5000 | -19.17 | 0.321 | -6.7 | 0.137 | False |
| 2026-09-01 12:17 | 5000 | -18.47 | 0.331 | -6.73 | 0.137 | False |
| 2026-09-01 16:33 | 5000 | -18.83 | 0.326 | -5.72 | 0.058 | False |
| 2026-09-01 20:11 | 5000 | -19.38 | 0.313 | -6.27 | 0.053 | False |
| 2026-09-02 00:31 | 5000 | -19.16 | 0.316 | -6.27 | 0.053 | False |
| 2026-09-02 04:15 | 5000 | -19.49 | 0.313 | -6.27 | 0.053 | False |
| 2026-09-02 08:16 | 5000 | -19.5 | 0.313 | -6.27 | 0.053 | False |
| 2026-09-02 12:18 | 5000 | -19.2 | 0.317 | -6.77 | 0.05 | False |
| 2026-09-02 16:13 | 5000 | -19.67 | 0.311 | -7.15 | 0.047 | False |

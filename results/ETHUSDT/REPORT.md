# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-09-02 00:31_

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

- Current-params net profit (full sample): **-19.16%**, PF 0.316, 99 trades, max DD -1916.34
- Optimizer out-of-sample: net **-6.27%**, PF 0.053, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-31 12:18 | 5000 | -18.88 | 0.324 | -6.45 | 0.141 | False |
| 2026-08-31 16:12 | 5000 | -18.9 | 0.324 | -6.45 | 0.141 | False |
| 2026-08-31 20:11 | 5000 | -18.9 | 0.324 | -6.48 | 0.141 | False |
| 2026-09-01 00:37 | 5000 | -19.19 | 0.32 | -7.13 | 0.129 | False |
| 2026-09-01 04:13 | 5000 | -19.18 | 0.32 | -7.09 | 0.13 | False |
| 2026-09-01 08:16 | 5000 | -19.17 | 0.321 | -6.7 | 0.137 | False |
| 2026-09-01 12:17 | 5000 | -18.47 | 0.331 | -6.73 | 0.137 | False |
| 2026-09-01 16:33 | 5000 | -18.83 | 0.326 | -5.72 | 0.058 | False |
| 2026-09-01 20:11 | 5000 | -19.38 | 0.313 | -6.27 | 0.053 | False |
| 2026-09-02 00:31 | 5000 | -19.16 | 0.316 | -6.27 | 0.053 | False |

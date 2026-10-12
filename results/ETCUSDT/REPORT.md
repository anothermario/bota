# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-12 04:21_

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

- Current-params net profit (full sample): **-9.8%**, PF 0.611, 61 trades, max DD -1472.29
- Optimizer out-of-sample: net **-7.36%**, PF 0.149, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-10 16:12 | 5000 | -5.31 | 0.78 | -6.2 | 0.171 | False |
| 2026-10-10 20:11 | 5000 | -5.34 | 0.78 | -6.23 | 0.171 | False |
| 2026-10-11 00:37 | 5000 | -5.5 | 0.774 | -6.4 | 0.166 | False |
| 2026-10-11 04:15 | 5000 | -6.96 | 0.719 | -7.66 | 0.146 | False |
| 2026-10-11 08:15 | 5000 | -7.81 | 0.694 | -7.29 | 0.149 | False |
| 2026-10-11 12:17 | 5000 | -7.2 | 0.712 | -8.0 | 0.137 | False |
| 2026-10-11 16:13 | 5000 | -7.23 | 0.711 | -8.0 | 0.137 | False |
| 2026-10-11 20:12 | 5000 | -7.14 | 0.716 | -7.32 | 0.149 | False |
| 2026-10-12 00:38 | 5000 | -9.81 | 0.611 | -7.99 | 0.138 | False |
| 2026-10-12 04:21 | 5000 | -9.8 | 0.611 | -7.36 | 0.149 | False |

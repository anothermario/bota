# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-11 12:17_

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

- Current-params net profit (full sample): **-7.2%**, PF 0.712, 61 trades, max DD -1433.64
- Optimizer out-of-sample: net **-8.0%**, PF 0.137, 24 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-10 00:34 | 5000 | -5.91 | 0.761 | -6.12 | 0.173 | False |
| 2026-10-10 04:14 | 5000 | -5.99 | 0.758 | -6.2 | 0.171 | False |
| 2026-10-10 08:15 | 5000 | -5.99 | 0.758 | -6.2 | 0.171 | False |
| 2026-10-10 12:16 | 5000 | -5.22 | 0.784 | -6.2 | 0.171 | False |
| 2026-10-10 16:12 | 5000 | -5.31 | 0.78 | -6.2 | 0.171 | False |
| 2026-10-10 20:11 | 5000 | -5.34 | 0.78 | -6.23 | 0.171 | False |
| 2026-10-11 00:37 | 5000 | -5.5 | 0.774 | -6.4 | 0.166 | False |
| 2026-10-11 04:15 | 5000 | -6.96 | 0.719 | -7.66 | 0.146 | False |
| 2026-10-11 08:15 | 5000 | -7.81 | 0.694 | -7.29 | 0.149 | False |
| 2026-10-11 12:17 | 5000 | -7.2 | 0.712 | -8.0 | 0.137 | False |

# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-10 08:15_

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

- Current-params net profit (full sample): **-5.99%**, PF 0.758, 63 trades, max DD -1393.9
- Optimizer out-of-sample: net **-6.2%**, PF 0.171, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-08 20:12 | 5000 | -5.68 | 0.772 | -6.11 | 0.275 | False |
| 2026-10-09 00:35 | 5000 | -6.61 | 0.733 | -6.38 | 0.244 | False |
| 2026-10-09 04:17 | 5000 | -6.61 | 0.733 | -7.1 | 0.152 | False |
| 2026-10-09 08:18 | 5000 | -6.61 | 0.733 | -6.24 | 0.261 | False |
| 2026-10-09 12:17 | 5000 | -5.88 | 0.761 | -7.0 | 0.156 | False |
| 2026-10-09 16:12 | 5000 | -5.88 | 0.761 | -7.02 | 0.153 | False |
| 2026-10-09 20:12 | 5000 | -5.88 | 0.761 | -7.02 | 0.153 | False |
| 2026-10-10 00:34 | 5000 | -5.91 | 0.761 | -6.12 | 0.173 | False |
| 2026-10-10 04:14 | 5000 | -5.99 | 0.758 | -6.2 | 0.171 | False |
| 2026-10-10 08:15 | 5000 | -5.99 | 0.758 | -6.2 | 0.171 | False |

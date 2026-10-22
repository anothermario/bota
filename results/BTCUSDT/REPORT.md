# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-10-22 00:28_

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

- Current-params net profit (full sample): **-11.79%**, PF 0.496, 64 trades, max DD -1251.27
- Optimizer out-of-sample: net **-2.28%**, PF 0.487, 17 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-20 12:16 | 5000 | -12.3 | 0.483 | -2.8 | 0.435 | False |
| 2026-10-20 16:13 | 5000 | -11.93 | 0.492 | -2.8 | 0.435 | False |
| 2026-10-20 20:11 | 5000 | -11.93 | 0.492 | -2.8 | 0.435 | False |
| 2026-10-21 00:28 | 5000 | -11.93 | 0.492 | -2.8 | 0.435 | False |
| 2026-10-21 04:13 | 5000 | -11.93 | 0.492 | -2.8 | 0.435 | False |
| 2026-10-21 08:15 | 5000 | -11.93 | 0.492 | -3.3 | 0.394 | False |
| 2026-10-21 12:16 | 5000 | -11.77 | 0.496 | -3.3 | 0.393 | False |
| 2026-10-21 16:11 | 5000 | -12.45 | 0.481 | -2.84 | 0.434 | False |
| 2026-10-21 20:10 | 5000 | -11.85 | 0.495 | -2.28 | 0.487 | False |
| 2026-10-22 00:28 | 5000 | -11.79 | 0.496 | -2.28 | 0.487 | False |

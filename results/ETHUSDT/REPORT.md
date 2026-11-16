# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-11-16 12:14_

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

- Current-params net profit (full sample): **-11.5%**, PF 0.509, 75 trades, max DD -1379.36
- Optimizer out-of-sample: net **-1.5%**, PF 0.816, 26 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-15 00:21 | 5000 | -14.67 | 0.395 | -4.27 | 0.494 | False |
| 2026-11-15 04:08 | 5000 | -12.4 | 0.487 | -1.73 | 0.794 | False |
| 2026-11-15 08:09 | 5000 | -12.4 | 0.487 | -1.73 | 0.794 | False |
| 2026-11-15 12:10 | 5000 | -12.4 | 0.487 | -1.68 | 0.8 | False |
| 2026-11-15 16:07 | 5000 | -12.4 | 0.487 | -1.68 | 0.8 | False |
| 2026-11-15 20:07 | 5000 | -12.4 | 0.487 | -1.73 | 0.794 | False |
| 2026-11-16 00:24 | 5000 | -12.41 | 0.487 | -1.73 | 0.794 | False |
| 2026-11-16 04:09 | 5000 | -12.4 | 0.487 | -2.01 | 0.767 | False |
| 2026-11-16 08:22 | 5000 | -11.5 | 0.509 | -1.73 | 0.794 | False |
| 2026-11-16 12:14 | 5000 | -11.5 | 0.509 | -1.5 | 0.816 | False |

# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-29 04:12_

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

- Current-params net profit (full sample): **-10.81%**, PF 0.451, 70 trades, max DD -1084.47
- Optimizer out-of-sample: net **-1.15%**, PF 0.761, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-27 15:44 | 5000 | -11.43 | 0.435 | -1.97 | 0.646 | False |
| 2026-08-27 19:33 | 5000 | -11.43 | 0.435 | -2.29 | 0.61 | False |
| 2026-08-27 23:09 | 5000 | -11.76 | 0.427 | -1.21 | 0.749 | False |
| 2026-08-28 02:57 | 5000 | -11.24 | 0.44 | -1.21 | 0.749 | False |
| 2026-08-28 06:35 | 5000 | -11.24 | 0.44 | -1.21 | 0.749 | False |
| 2026-08-28 11:53 | 5000 | -11.24 | 0.44 | -1.21 | 0.749 | False |
| 2026-08-28 16:11 | 5000 | -11.24 | 0.44 | -1.21 | 0.749 | False |
| 2026-08-28 21:57 | 5000 | -11.27 | 0.439 | -1.23 | 0.749 | False |
| 2026-08-29 00:28 | 5000 | -11.24 | 0.44 | -1.15 | 0.761 | False |
| 2026-08-29 04:12 | 5000 | -10.81 | 0.451 | -1.15 | 0.761 | False |

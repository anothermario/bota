# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-30 21:08_

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
  "chand_len": 18,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-11.85%**, PF 0.553, 65 trades, max DD -1532.78
- Optimizer out-of-sample: net **-6.66%**, PF 0.384, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-29 10:38 | 5000 | -11.6 | 0.555 | -5.89 | 0.416 | False |
| 2026-07-29 14:07 | 5000 | -11.59 | 0.555 | -5.89 | 0.416 | False |
| 2026-07-29 17:13 | 5000 | -11.01 | 0.57 | -5.93 | 0.415 | False |
| 2026-07-29 20:54 | 5000 | -11.89 | 0.55 | -6.7 | 0.384 | False |
| 2026-07-30 02:13 | 5000 | -11.13 | 0.568 | -7.3 | 0.376 | False |
| 2026-07-30 06:27 | 5000 | -11.13 | 0.568 | -7.28 | 0.377 | False |
| 2026-07-30 10:24 | 5000 | -10.6 | 0.586 | -6.8 | 0.376 | False |
| 2026-07-30 13:57 | 5000 | -10.63 | 0.599 | -7.51 | 0.353 | False |
| 2026-07-30 17:25 | 5000 | -11.02 | 0.583 | -6.64 | 0.384 | False |
| 2026-07-30 21:08 | 5000 | -11.85 | 0.553 | -6.66 | 0.384 | False |

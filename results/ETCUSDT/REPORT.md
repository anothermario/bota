# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-02 13:17_

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

- Current-params net profit (full sample): **-10.76%**, PF 0.589, 63 trades, max DD -1536.51
- Optimizer out-of-sample: net **-3.78%**, PF 0.575, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-01 02:41 | 5000 | -11.57 | 0.56 | -7.0 | 0.39 | False |
| 2026-08-01 06:28 | 5000 | -11.32 | 0.569 | -6.29 | 0.428 | False |
| 2026-08-01 09:58 | 5000 | -11.32 | 0.569 | -5.99 | 0.441 | False |
| 2026-08-01 13:17 | 5000 | -10.63 | 0.586 | -5.14 | 0.484 | False |
| 2026-08-01 16:58 | 5000 | -10.96 | 0.577 | -5.27 | 0.449 | False |
| 2026-08-01 20:53 | 5000 | -10.44 | 0.592 | -5.31 | 0.449 | False |
| 2026-08-02 02:40 | 5000 | -9.94 | 0.61 | -3.78 | 0.575 | False |
| 2026-08-02 06:31 | 5000 | -10.75 | 0.589 | -3.78 | 0.575 | False |
| 2026-08-02 09:55 | 5000 | -10.75 | 0.589 | -3.78 | 0.575 | False |
| 2026-08-02 13:17 | 5000 | -10.76 | 0.589 | -3.78 | 0.575 | False |

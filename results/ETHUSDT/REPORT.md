# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-26 13:19_

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

- Current-params net profit (full sample): **-18.94%**, PF 0.445, 94 trades, max DD -2132.75
- Optimizer out-of-sample: net **-11.56%**, PF 0.102, 30 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-25 02:32 | 5000 | -17.84 | 0.479 | -10.31 | 0.166 | False |
| 2026-07-25 06:17 | 5000 | -17.82 | 0.48 | -10.3 | 0.166 | False |
| 2026-07-25 09:45 | 5000 | -17.76 | 0.482 | -9.86 | 0.217 | False |
| 2026-07-25 13:23 | 5000 | -19.14 | 0.438 | -11.24 | 0.091 | False |
| 2026-07-25 16:55 | 5000 | -19.48 | 0.433 | -11.23 | 0.091 | False |
| 2026-07-25 20:51 | 5000 | -18.82 | 0.443 | -11.11 | 0.092 | False |
| 2026-07-26 02:40 | 5000 | -18.63 | 0.448 | -10.9 | 0.107 | False |
| 2026-07-26 06:35 | 5000 | -19.29 | 0.438 | -11.17 | 0.105 | False |
| 2026-07-26 09:58 | 5000 | -18.58 | 0.45 | -11.17 | 0.105 | False |
| 2026-07-26 13:19 | 5000 | -18.94 | 0.445 | -11.56 | 0.102 | False |

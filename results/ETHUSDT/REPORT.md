# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-27 07:29_

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

- Current-params net profit (full sample): **-18.63%**, PF 0.447, 95 trades, max DD -2106.88
- Optimizer out-of-sample: net **-10.73%**, PF 0.163, 30 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-25 16:55 | 5000 | -19.48 | 0.433 | -11.23 | 0.091 | False |
| 2026-07-25 20:51 | 5000 | -18.82 | 0.443 | -11.11 | 0.092 | False |
| 2026-07-26 02:40 | 5000 | -18.63 | 0.448 | -10.9 | 0.107 | False |
| 2026-07-26 06:35 | 5000 | -19.29 | 0.438 | -11.17 | 0.105 | False |
| 2026-07-26 09:58 | 5000 | -18.58 | 0.45 | -11.17 | 0.105 | False |
| 2026-07-26 13:19 | 5000 | -18.94 | 0.445 | -11.56 | 0.102 | False |
| 2026-07-26 16:59 | 5000 | -18.99 | 0.444 | -11.6 | 0.102 | False |
| 2026-07-26 20:56 | 5000 | -18.13 | 0.469 | -10.79 | 0.163 | False |
| 2026-07-27 02:48 | 5000 | -18.78 | 0.445 | -9.7 | 0.197 | False |
| 2026-07-27 07:29 | 5000 | -18.63 | 0.447 | -10.73 | 0.163 | False |

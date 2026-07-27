# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-27 14:30_

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

- Current-params net profit (full sample): **-19.4%**, PF 0.436, 96 trades, max DD -2105.51
- Optimizer out-of-sample: net **-10.72%**, PF 0.164, 30 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-26 02:40 | 5000 | -18.63 | 0.448 | -10.9 | 0.107 | False |
| 2026-07-26 06:35 | 5000 | -19.29 | 0.438 | -11.17 | 0.105 | False |
| 2026-07-26 09:58 | 5000 | -18.58 | 0.45 | -11.17 | 0.105 | False |
| 2026-07-26 13:19 | 5000 | -18.94 | 0.445 | -11.56 | 0.102 | False |
| 2026-07-26 16:59 | 5000 | -18.99 | 0.444 | -11.6 | 0.102 | False |
| 2026-07-26 20:56 | 5000 | -18.13 | 0.469 | -10.79 | 0.163 | False |
| 2026-07-27 02:48 | 5000 | -18.78 | 0.445 | -9.7 | 0.197 | False |
| 2026-07-27 07:29 | 5000 | -18.63 | 0.447 | -10.73 | 0.163 | False |
| 2026-07-27 11:19 | 5000 | -19.26 | 0.436 | -9.93 | 0.175 | False |
| 2026-07-27 14:30 | 5000 | -19.4 | 0.436 | -10.72 | 0.164 | False |

# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-03 10:34_

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

- Current-params net profit (full sample): **-11.17%**, PF 0.626, 90 trades, max DD -1239.96
- Optimizer out-of-sample: net **-4.22%**, PF 0.41, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-01 20:37 | 5000 | -12.07 | 0.586 | -5.75 | 0.219 | False |
| 2026-07-02 00:51 | 5000 | -11.8 | 0.601 | -5.57 | 0.244 | False |
| 2026-07-02 07:31 | 5000 | -12.54 | 0.585 | -5.06 | 0.29 | False |
| 2026-07-02 10:38 | 5000 | -12.54 | 0.585 | -5.06 | 0.29 | False |
| 2026-07-02 13:58 | 5000 | -11.9 | 0.6 | -5.08 | 0.291 | False |
| 2026-07-02 17:46 | 5000 | -11.88 | 0.601 | -6.19 | 0.225 | False |
| 2026-07-02 21:05 | 5000 | -11.93 | 0.6 | -5.33 | 0.254 | False |
| 2026-07-03 02:53 | 5000 | -10.67 | 0.639 | -4.79 | 0.466 | False |
| 2026-07-03 07:19 | 5000 | -11.15 | 0.626 | -4.2 | 0.41 | False |
| 2026-07-03 10:34 | 5000 | -11.17 | 0.626 | -4.22 | 0.41 | False |

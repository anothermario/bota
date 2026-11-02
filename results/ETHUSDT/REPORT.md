# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-11-02 12:11_

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

- Current-params net profit (full sample): **-9.81%**, PF 0.591, 75 trades, max DD -1180.78
- Optimizer out-of-sample: net **-5.1%**, PF 0.438, 28 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-01 00:23 | 5000 | -10.53 | 0.575 | -5.22 | 0.277 | False |
| 2026-11-01 04:08 | 5000 | -10.56 | 0.575 | -4.99 | 0.289 | False |
| 2026-11-01 08:09 | 5000 | -10.38 | 0.58 | -4.99 | 0.289 | False |
| 2026-11-01 12:10 | 5000 | -10.38 | 0.58 | -4.99 | 0.289 | False |
| 2026-11-01 16:07 | 5000 | -10.55 | 0.575 | -5.17 | 0.28 | False |
| 2026-11-01 20:06 | 5000 | -10.55 | 0.575 | -5.16 | 0.28 | False |
| 2026-11-02 00:21 | 5000 | -10.57 | 0.575 | -5.03 | 0.285 | False |
| 2026-11-02 04:09 | 5000 | -10.18 | 0.586 | -5.07 | 0.285 | False |
| 2026-11-02 08:11 | 5000 | -10.33 | 0.578 | -5.0 | 0.291 | False |
| 2026-11-02 12:11 | 5000 | -9.81 | 0.591 | -5.1 | 0.438 | False |

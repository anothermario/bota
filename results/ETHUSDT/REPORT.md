# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-11-04 00:19_

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

- Current-params net profit (full sample): **-10.56%**, PF 0.57, 75 trades, max DD -1241.93
- Optimizer out-of-sample: net **-6.09%**, PF 0.182, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-02 08:11 | 5000 | -10.33 | 0.578 | -5.0 | 0.291 | False |
| 2026-11-02 12:11 | 5000 | -9.81 | 0.591 | -5.1 | 0.438 | False |
| 2026-11-02 20:06 | 5000 | -9.68 | 0.596 | -5.02 | 0.291 | False |
| 2026-11-03 00:19 | 5000 | -9.68 | 0.596 | -5.64 | 0.213 | False |
| 2026-11-03 04:08 | 5000 | -10.62 | 0.568 | -6.08 | 0.199 | False |
| 2026-11-03 08:10 | 5000 | -10.37 | 0.575 | -6.19 | 0.183 | False |
| 2026-11-03 12:10 | 5000 | -10.36 | 0.575 | -6.22 | 0.179 | False |
| 2026-11-03 16:08 | 5000 | -10.27 | 0.578 | -6.36 | 0.176 | False |
| 2026-11-03 20:07 | 5000 | -10.58 | 0.57 | -6.34 | 0.176 | False |
| 2026-11-04 00:19 | 5000 | -10.56 | 0.57 | -6.09 | 0.182 | False |

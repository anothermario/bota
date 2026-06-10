# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-06-10 00:55_

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
  "don_len": 20,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-6.98%**, PF 0.661, 64 trades, max DD -1210.23
- Optimizer out-of-sample: net **2.58%**, PF 1.428, 17 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-09 16:58 | 5000 | -17.33 | 0.365 | 1.41 | 1.239 | True |
| 2026-06-09 20:44 | 5000 | -6.98 | 0.661 | 2.58 | 1.428 | True |
| 2026-06-10 00:55 | 5000 | -6.98 | 0.661 | 2.58 | 1.428 | True |

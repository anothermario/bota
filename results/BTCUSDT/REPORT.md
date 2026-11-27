# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-11-27 20:07_

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
  "don_len": 15,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 26,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-8.35%**, PF 0.659, 72 trades, max DD -969.63
- Optimizer out-of-sample: net **0.64%**, PF 1.078, 22 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-26 08:09 | 5000 | -8.43 | 0.655 | 2.09 | 1.271 | True |
| 2026-11-26 12:10 | 5000 | -8.84 | 0.643 | 2.09 | 1.272 | True |
| 2026-11-26 16:08 | 5000 | -9.03 | 0.64 | 1.42 | 1.17 | True |
| 2026-11-26 20:07 | 5000 | -9.57 | 0.625 | 1.43 | 1.172 | True |
| 2026-11-27 00:19 | 5000 | -9.57 | 0.625 | 1.42 | 1.17 | True |
| 2026-11-27 04:08 | 5000 | -9.04 | 0.639 | 1.48 | 1.177 | True |
| 2026-11-27 08:09 | 5000 | -9.03 | 0.64 | 2.42 | 1.303 | True |
| 2026-11-27 12:11 | 5000 | -8.2 | 0.652 | 2.0 | 1.239 | True |
| 2026-11-27 16:07 | 5000 | -8.4 | 0.658 | 2.03 | 1.241 | True |
| 2026-11-27 20:07 | 5000 | -8.35 | 0.659 | 0.64 | 1.078 | True |

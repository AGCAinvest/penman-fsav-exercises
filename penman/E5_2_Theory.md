# Exercise E5.2 — ROCE and Valuation
**Source:** Penman, S. H. (2013). *Financial Statement Analysis and Security Valuation* (5th ed.), Chapter 5, p. 175.

## Problem Statement
The following are ROCE forecasts made for a firm at the end of 2010:
- **2011-2013 ROCE:** 12.0%
- **Post-2013 ROCE:** 12.0% (Constant)
- **Book Value (2010):** $3.2 Billion
- **Shares Outstanding:** 500 Million
- **Required Return (r):** 12%

## Mathematical Theory
### The Normal Price-to-Book Ratio
When the forecasted Return on Common Equity ($ROCE$) equals the cost of capital ($r$), the firm generates zero Residual Earnings ($RE$). In this case, the intrinsic value equals the book value ($P/B = 1.0$).

$$ROCE = r \implies RE = 0 \implies V_0^E = B_0$$

### Valuation Model
The equity value is the current book value plus the present value of future residual earnings:
$$V_0^E = B_0 + \sum_{t=1}^{\infty} \frac{RE_t}{(1+r)^t}$$

## Python Implementation Summary
The script `e5_2.py` calculates the following:
- **BPS 2010:** $3.2B / 500M = \$6.40$
- **Residual Earnings:** $(0.12 - 0.12) \times 6.40 = \$0.00$
- **Intrinsic Value:** $\$6.40 + \$0.00 = \$6.40$

---
*Developed by Antônio Guilherme Coelho de Assis* *Amazon Institute of Value Investing and Applied Data Science*
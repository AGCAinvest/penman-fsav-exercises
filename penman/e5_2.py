# Exercise E5.2 — ROCE and Valuation
# Source: Penman, S. H. (2013). Financial Statement Analysis and Security Valuation (5th ed.), Chapter 5, p. 168.

# Define Inputs Variables
#  
book_value_2010 = 3200000000
shares_outstanding = 500000000
required_return = 0.12
forecasted_roce = 0.12

# 2. Calculation The Funadamentals
# BPS calculation (Book Value Per Share)

bps_2010 = book_value_2010 / shares_outstanding

#Residual Earnings salculation: RE = (ROCE - r) * BPS
 # 2. Calculating the fundamentals
# BPS calculation (Book Value per Share)
bps_2010 = book_value_2010 / shares_outstanding

# Residual Earnings calculation: RE = (ROCE - r) * BPS
# Since ROCE equals the required return, RE will be zero.
residual_earnings = (forecasted_roce - required_return) * bps_2010

# Final Value calculation
# Value = BPS + Present Value of Future RE
intrinsic_value = bps_2010 + residual_earnings

# 3. Output results using f-strings
print(f"Book Value per Share: ${bps_2010:.2f}")
print(f"Forecasted ROCE:      {forecasted_roce:.1%}")
print(f"Required Return (r):  {required_return:.1%}")
print(f"Residual Earnings:    ${residual_earnings:.2f}")
print(f"Value per Share:      ${intrinsic_value:.2f}")

# 3. Summary Output (Formatted exactly like your reference image)
print("========== E5.2 Summary ==========")
print(f"{'Year':<10} {'End Book':<12} {'ROCE':<10} {'RE':<10}")

# Since ROCE is constant at 12%, we can show the 2011 forecast row
year = 2010
print(f"{year:<10} {bps_2010:<12.2f} {forecasted_roce:<10.2%} {residual_earnings:<10.4f}")
print("==================================")

# Final valuation output
print(f"\nValue per Share: ${intrinsic_value:.2f}")
print(f"P/B Ratio:       {intrinsic_value / bps_2010:.1f}")
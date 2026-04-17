# E5.1 - Forecasting ROCE and Residual Earnings
# Penman FSAV Cap 5
# Required Return: 10%
# ROCE = Return On Common Shareholder's Equity 
# ROCE calculate as Box 5.1 page 147
# Financial Data
required_return = 0.10
book_2012 = 20.00
book_2013 = 20.00
book_2014 = 22.75
book_2015 = 26.10
eps_2013 = 3
eps_2014 = 3.6
eps_2015 = 4.10
dps_2013 = 0.25
dps_2014 = 0.25
dps_2015 = 0.30
ending_book_2013 = (book_2013 + eps_2013 - dps_2013)
print(f"Ending Book 2013: {ending_book_2013:.2f}")
ending_book_2014 = ending_book_2013 + eps_2014 - dps_2014
print(f"Ending Book 2014: {ending_book_2014:.2f}")
ending_book_2015 = ending_book_2014 + eps_2015 - dps_2015
print(f"Ending Book 2015: {ending_book_2015:.2f}")
# Calculation Residual Earnings
re_2013 = (eps_2013) - (required_return*book_2012)
print(f"RE 2013: {re_2013:.4f}")
re_2014 = (eps_2014) - (required_return*ending_book_2013)
print(f"RE 2014: {re_2014:.4f}")
re_2015 = (eps_2015) - (required_return*ending_book_2014)
print(f"RE 2015: {re_2015:.4f}")
#  I  think this firm is worth more than its book value because its residual earnings is positive.
# ROCE calculation
roce_2013 = eps_2013 / book_2012
roce_2014 = eps_2014 / ending_book_2013
roce_2015 = eps_2015 / ending_book_2014

print(f"ROCE 2013: {roce_2013:.2%}")
print(f"ROCE 2014: {roce_2014:.2%}")
print(f"ROCE 2015: {roce_2015:.2%}")
# Summary
print("\n========== E5.1 Summary ==========")
print(f"{'Year':<8} {'End Book':>10} {'ROCE':>8} {'RE':>8}")
print(f"{'2013':<8} {ending_book_2013:>10.2f} {roce_2013:>8.2%} {re_2013:>8.4f}")
print(f"{'2014':<8} {ending_book_2014:>10.2f} {roce_2014:>8.2%} {re_2014:>8.4f}")
print(f"{'2015':<8} {ending_book_2015:>10.2f} {roce_2015:>8.2%} {re_2015:>8.4f}")
print("===================================")
# E5.1 - Forecasting ROCE and Residual Earnings
# Penman FSAV Cap 5
# Required Retur: 10%
# ROCE = Returne On Common Sahreholder's Equity 
# ROCE calculate as Box 5.1 page 147
# Financaal Data
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
#  I  think this firm is worthink more thant tis book value because its residual earnings is positive.
# ROCE calculation
roce_2013 = eps_2013 / book_2012
roce_2014 = eps_2014 / ending_book_2013
roce_2015 = eps_2015 / ending_book_2014

print(f"ROCE 2013: {roce_2013:.2%}")
print(f"ROCE 2014: {roce_2014:.2%}")
print(f"ROCE 2015: {roce_2015:.2%}")
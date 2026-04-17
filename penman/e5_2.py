# E5.2 - ROCE and Valuation
# Penman, S. H. Financial Statement Analysis and Security Valuation
# (5th ed.), Chapter 5, p. 168.
# Required Return: 12%

# --- Input Data ---
book_value_2010 = 3_200_000_000
shares_outstanding = 500_000_000
required_return = 0.12
roce_2011 = 0.12
roce_2012 = 0.12
roce_2013 = 0.12

# --- Calculations ---
bps_2010 = book_value_2010 / shares_outstanding

re_2011 = (roce_2011 - required_return) * bps_2010
re_2012 = (roce_2012 - required_return) * bps_2010
re_2013 = (roce_2013 - required_return) * bps_2010

intrinsic_value = bps_2010  # RE = 0, no premium

pb_ratio = intrinsic_value / bps_2010

# --- Summary ---
print("\n========== E5.2 Summary ==========")
print(f"{'Year':<8} {'ROCE':>8} {'RE':>10} {'PV of RE':>10}")
print(f"{'2011':<8} {roce_2011:>8.1%} {re_2011:>10.4f} {re_2011:>10.4f}")
print(f"{'2012':<8} {roce_2012:>8.1%} {re_2012:>10.4f} {re_2012:>10.4f}")
print(f"{'2013':<8} {roce_2013:>8.1%} {re_2013:>10.4f} {re_2013:>10.4f}")
print("===================================")
print(f"\nBPS 2010:        ${bps_2010:.2f}")
print(f"Intrinsic Value: ${intrinsic_value:.2f}")
print(f"P/B Ratio:        {pb_ratio:.1f}")
print("\nConclusion: ROCE = required return → RE = 0 → Value = Book Value")
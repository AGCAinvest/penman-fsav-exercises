# E5.3 - A Residual Earnings Valuation
# Penman FSAV Cap 5
# Required Return: 10%

# --- Input Data ---
book_2012 = 4_310_000_000
shares_outstanding = 1_380_000_000
required_return = 0.10

anos = [2013, 2014, 2015, 2016, 2017]
eps  = [388_000_000, 570_000_000, 599_000_000, 629_000_000, 660_000_000]
dps  = [115_000_000, 160_000_000, 349_000_000, 367_000_000, 385_000_000]

# Calculations

# --- Calculations ---
bps_2012 = book_2012 / shares_outstanding

# Book Value per year
book = [0] * 5
book[0] = book_2012 + eps[0] - dps[0]
book[1] = book[0]  + eps[1] - dps[1]
book[2] = book[1]  + eps[2] - dps[2]
book[3] = book[2]  + eps[3] - dps[3]
book[4] = book[3]  + eps[4] - dps[4]

# Residual Earnings
re = [0] * 5
re[0] = eps[0] - (required_return * book_2012)
re[1] = eps[1] - (required_return * book[0])
re[2] = eps[2] - (required_return * book[1])
re[3] = eps[3] - (required_return * book[2])
re[4] = eps[4] - (required_return * book[3])

# Continuing Value (Case 2 — constant RE)
continuing_value = re[4] / required_return
# --- Summary ---
print("\n========== E5.3 Summary ==========")
print(f"{'Year':<8} {'EPS':>12} {'Book':>14} {'RE':>14}")
for i in range(5):
    print(f"{anos[i]:<8} {eps[i]/1e6:>11.1f}M {book[i]/1e6:>13.1f}M {re[i]/1e6:>13.1f}M")
print("===================================")
print(f"\nBPS 2012:          ${bps_2012:.4f}")
print(f"Continuing Value:  ${continuing_value/1e6:.1f}M")
print(f"\nConclusion: Case 2 — RE constant after 2017")
company = "Vivara"
ticker = "VIVA3"
print(ticker)
print(company)
bps = 12.55    
roce = 22.75
eps = 2.6353
print(bps)
print(roce)
print(eps)
# Book Value per Share histórico — Vivara S.A. (VIVA3)
bps_2025 = 12.55
bps_2024 = 10.62
bps_2023 = 8.22
bps_2022 = 7.03
bps_2021 = 5.90
   # Geometric growth of BPS — Vivara S.A. (VIVA3) 2021-2025
n = 4
bps_growth = ((bps_2025 / bps_2021) ** (1/n) - 1)
print(f"BPS Growth (CAGR): {bps_growth:.2%}") 
# Financial data - Vivara S.A (VIVA3)
eps_2022 = 1.5295       
required_return = 0.10
 # Residual Earnings 2022
re_2022 = eps_2022 - (required_return * bps_2021)
print(f"Residual Earnings 2022: {re_2022:.4f}")
# Residual Earnings 2023
eps_2023 = 1.5689
re_2023 = eps_2023 - (required_return * bps_2022)
print(f"Residual Earnings 2023: {re_2023:.4f}")

# Residual Earnings 2024
eps_2024 = 2.7794
re_2024 = eps_2024 - (required_return * bps_2023)
print(f"Residual Earnings 2024: {re_2024:.4f}")

# Residual Earnings 2025
eps_2025 = 2.6353
re_2025 = eps_2025 - (required_return * bps_2024)
print(f"Residual Earnings 2025: {re_2025:.4f}")
print("\n--- Vivara RE Summary ---")
print(f"2022: {re_2022:.4f}")
print(f"2023: {re_2023:.4f}")
print(f"2024: {re_2024:.4f}")
print(f"2025: {re_2025:.4f}")

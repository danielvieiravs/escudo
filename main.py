"""Main
"""
from decimal import Decimal

from data import stocks

from investment_strategies import value_investing

# TM
quote_table = stocks.get_quote_table(ticker="TM")
analysis_info = stocks.get_analysis_info(ticker="TM")

eps_ttm = Decimal(quote_table["EPS (TTM)"])
growth_rate = Decimal(analysis_info["Growth Estimates"]["TM"][4].strip("%")) / 100
pe_ratio = Decimal(quote_table["PE Ratio (TTM)"])

result = value_investing.intrinsic_value_phil_town(
    eps_ttm=eps_ttm,
    growth_rate=growth_rate,
    p_e_ratio=pe_ratio,
    margin_safety=Decimal(0.50),
    minimum_return_rate=Decimal(0.15),
)

print(f"Fair Value: {result['fair_value']}")
print(f"Margin Safety: {result['margin_safety']}")
print(f"Current Share Price: {quote_table['Quote Price']}")
print(f"Forward Dividend & Yield: {quote_table['Forward Dividend & Yield']}")
print(f"Ex-Dividend Date: {quote_table['Ex-Dividend Date']}")

# Fair Value: 314.5651440036796693493692873
# Margin Safety: 157.2825720018398346746846436
# Current Share Price: 171.6999969482422

# # FB
# print(value_investing.intrinsic_value_phil_town(
#     eps_ttm=13.77,
#     growth_rate=0.1660,
#     p_e_ratio=13.62,
# ))

# # AAPL
# eps_ttm = 6.01
# growth_rate = 0.1485
# p_e_ratio = 25.78

# # MSFT
# eps_ttm = 9.39
# growth_rate = 0.1740
# p_e_ratio = 32.00

# # AMZN
# eps_ttm = 64.81
# growth_rate = 0.49
# p_e_ratio = 45.48

# # BABA
# eps_ttm = 3.77
# growth_rate = 0.0035
# p_e_ratio = 20.39

# # GOOG
# eps_ttm = 112.20
# growth_rate = 0.1740
# p_e_ratio = 23.11

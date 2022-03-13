"""

Info source:
    https://www.youtube.com/watch?v=PuZY9q-aKLw
"""
from data import stocks, tickers

# Summary -> Create Csv with Yahoo Finance Data

# tickers = tickers.standard_and_poors_500()

# # csv header
# fieldnames = [
#     "ticker",
#     "open",
#     "pe_ratio_ttm",
#     "1_y_target_est",
#     "forward_dividend_and_yield"]

# # csv data
# rows = []

# for ticker in tickers:
#     data = stocks.get_quote_table(ticker=ticker)

#     if data["Forward Dividend & Yield"] == "N/A (N/A)":
#         continue

#     rows.append({
#         "ticker": ticker,
#         "open": data["Open"],
#         "pe_ratio_ttm": data["PE Ratio (TTM)"],
#         "1_y_target_est": data["1y Target Est"],
#         "forward_dividend_and_yield": data["Forward Dividend & Yield"]})

#     print(f"{ticker}: {data}")
#     print(f"Open: { data['Open'] }")
#     print(f"PE Ratio (TTM): { data['PE Ratio (TTM)'] }")
#     print(f"1y Target Est: { data['1y Target Est'] }")
#     print(f"Forward Dividend & Yield: { data['Forward Dividend & Yield'] }")
#     print(f"***")

# import csv

# with open('stocks_dividends.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(rows)

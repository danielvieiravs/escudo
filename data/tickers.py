"""
Info Source:
    https://github.com/shilewenuw/get_all_tickers/blob/master/get_all_tickers/get_tickers.py
    https://github.com/atreadw1492/yahoo_fin/blob/master/yahoo_fin/stock_info.py
"""

import pandas as pd


def standard_and_poors_500(include_company_data=False):
    """TODO: Add comment"""

    component_stocks = pd.read_html(
        "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    )[0]

    component_stocks["Symbol"] = component_stocks["Symbol"].str.replace(
        ".", "-", regex=True
    )

    if include_company_data:
        return component_stocks

    tickers = component_stocks.Symbol.tolist()

    tickers = sorted(tickers)

    return tickers


# TODO: Get other tickers
# https://dumbstockapi.com/

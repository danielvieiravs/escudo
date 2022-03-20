"""Create Csv with Value Investing Strategy
"""
from datetime import datetime
from decimal import Decimal

import csv

from data import stocks

from investment_strategies import value_investing


def value_investing_phill_town(tickers):

    fieldnames = [
        "ticker",
        "eps_ttm",
        "growth_rate",
        "pe_ratio",
        "fair_value",
        "margin_safety",
        "current_share_price",
        "dividends",
        "last_dividend",
    ]
    rows = []

    for ticker in tickers:
        try:
            print(f"*** {ticker} ***")

            quote_table = stocks.get_quote_table(ticker=ticker)
            analysis_info = stocks.get_analysis_info(ticker=ticker)

            eps_ttm = Decimal(quote_table["EPS (TTM)"])
            growth_rate = (
                Decimal(analysis_info["Growth Estimates"][ticker][4].strip("%")) / 100
            )
            pe_ratio = Decimal(quote_table["PE Ratio (TTM)"])

            result = value_investing.intrinsic_value_phil_town(
                eps_ttm=eps_ttm,
                growth_rate=growth_rate,
                p_e_ratio=pe_ratio,
                margin_safety=Decimal(0.50),
                minimum_return_rate=Decimal(0.15),
            )

            rows.append(
                {
                    "ticker": ticker,
                    "eps_ttm": eps_ttm,
                    "growth_rate": growth_rate,
                    "pe_ratio": pe_ratio,
                    "fair_value": result["fair_value"],
                    "margin_safety": result["margin_safety"],
                    "current_share_price": quote_table["Quote Price"],
                    "dividends": quote_table["Forward Dividend & Yield"],
                    "last_dividend": quote_table["Ex-Dividend Date"],
                }
            )

        except Exception as error:
            print(error)

    filename = (
        f"value_investing_phil_town"
        f"{datetime.utcnow().strftime('%Y-%m-%d-%H-%M.csv')}.csv"
    )

    with open(filename, "w", encoding="UTF8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

"""

Info Source:
    https://github.com/atreadw1492/yahoo_fin
    https://www.youtube.com/watch?v=IMCbi6cvRmY
    http://theautomatic.net/yahoo_fin-documentation/
"""
import pandas_datareader as web


def price_history(company, data_source, start_date, end_date):
    """TODO: Add comment"""
    data = web.DataReader(
        name=company,
        data_source=data_source,
        start=start_date,
        end=end_date)

    return data

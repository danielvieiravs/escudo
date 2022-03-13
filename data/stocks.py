"""

Info Source:
    https://github.com/atreadw1492/yahoo_fin
    https://www.youtube.com/watch?v=IMCbi6cvRmY
    http://theautomatic.net/yahoo_fin-documentation/
    https://roic.ai/company/IRM
"""
import requests
import pandas_datareader as web

import pandas as pd


def price_history(company, data_source, start_date, end_date):
    """TODO: Add comment"""
    data = web.DataReader(
        name=company, data_source=data_source, start=start_date, end=end_date
    )

    return data


# Yahoo Finance


def build_url(ticker, start_date=None, end_date=None, interval="1d"):

    if end_date is None:
        end_seconds = int(pd.Timestamp("now").timestamp())

    else:
        end_seconds = int(pd.Timestamp(end_date).timestamp())

    if start_date is None:
        start_seconds = 7223400

    else:
        start_seconds = int(pd.Timestamp(start_date).timestamp())

    site = "https://query1.finance.yahoo.com/v8/finance/chart/" + ticker

    params = {
        "period1": start_seconds,
        "period2": end_seconds,
        "interval": interval.lower(),
        "events": "div,splits",
    }

    return site, params


def get_data(
    ticker,
    start_date=None,
    end_date=None,
    index_as_date=True,
    interval="1d",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
    },
):
    """Downloads historical stock price data into a pandas data frame.  Interval
        must be "1d", "1wk", "1mo", or "1m" for daily, weekly, monthly, or minute data.
        Intraday minute data is limited to 7 days.

    Args:
        ticker (str)
        start_date (str)
        end_date (str)
        index_as_date (bool)
        interval (str)
    """

    if interval not in ("1d", "1wk", "1mo", "1m"):
        raise AssertionError("interval must be of of '1d', '1wk', '1mo', or '1m'")

    # build and connect to URL
    site, params = build_url(ticker, start_date, end_date, interval)
    resp = requests.get(site, params=params, headers=headers)

    if not resp.ok:
        raise AssertionError(resp.json())

    # get JSON response
    data = resp.json()

    # get open / high / low / close data
    frame = pd.DataFrame(data["chart"]["result"][0]["indicators"]["quote"][0])

    # get the date info
    temp_time = data["chart"]["result"][0]["timestamp"]

    if interval != "1m":

        # add in adjclose
        frame["adjclose"] = data["chart"]["result"][0]["indicators"]["adjclose"][0][
            "adjclose"
        ]
        frame.index = pd.to_datetime(temp_time, unit="s")
        frame.index = frame.index.map(lambda dt: dt.floor("d"))
        frame = frame[["open", "high", "low", "close", "adjclose", "volume"]]

    else:

        frame.index = pd.to_datetime(temp_time, unit="s")
        frame = frame[["open", "high", "low", "close", "volume"]]

    frame["ticker"] = ticker.upper()

    if not index_as_date:
        frame = frame.reset_index()
        frame.rename(columns={"index": "date"}, inplace=True)

    return frame


def get_live_price(ticker):
    """Gets the live price of input ticker

    Args:
       ticker (str)
    """

    df = get_data(ticker, end_date=pd.Timestamp.today() + pd.DateOffset(10))

    return df.close[-1]


def force_float(elt):

    try:
        return float(elt)
    except ValueError:
        return elt


def get_quote_table(ticker, dict_result=True, headers={"User-agent": "Mozilla/5.0"}):
    """Scrapes data elements found on Yahoo Finance's quote page of input ticker

    Args:
        ticker (str)
        dict_result (bool)
    """
    site = "https://finance.yahoo.com/quote/" + ticker + "?p=" + ticker

    tables = pd.read_html(requests.get(site, headers=headers).text)

    data = tables[0].append(tables[1])

    data.columns = ["attribute", "value"]

    quote_price = pd.DataFrame(["Quote Price", get_live_price(ticker)]).transpose()
    quote_price.columns = data.columns.copy()

    data = data.append(quote_price)

    data = data.sort_values("attribute")

    data = data.drop_duplicates().reset_index(drop=True)

    data["value"] = data.value.map(force_float)

    if dict_result:
        result = {key: val for key, val in zip(data.attribute, data.value)}
        return result

    return data


# roic.ai

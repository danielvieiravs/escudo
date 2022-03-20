"""Main
"""
from utils import generate_csv
from data import tickers


tickers = tickers.standard_and_poors_500()

generate_csv.value_investing_phill_town(tickers=tickers)

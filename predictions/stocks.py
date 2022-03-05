"""

Info source:
    https://www.youtube.com/watch?v=PuZY9q-aKLw
"""

from data import stocks
from datetime import datetime

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

companies = [
    'GOOG',  # Alphabet / Google
    'MSFT',  # Microsoft
    'AMZN',  # Amazon
    'FB',  # Meta
    'AAPL',  # Apple
    'ABNB',  # Airbnb
    'RYAAY',  # Ryanair
    'PTON'  # Peloton
]

data = stocks.price_history(
    company='FB',
    data_source='yahoo',
    start_date=datetime(2012, 1, 1),
    end_date=datetime(2020, 1, 1))

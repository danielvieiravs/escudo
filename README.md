# Escudo
Arma de defesa que consiste em uma peça larga, ger. de metal, presa à mão ou ao
braço, que protege o corpo do guerreiro contra armas.

![Tree](images/tree.jpeg)


# Examples Price History:

- Meta / Facebook
```shell
python
from datetime import datetime
from data import stocks
data = stocks.price_history(company='FB', data_source='yahoo', start_date=datetime(2012, 1, 1), end_date=datetime(2023, 1, 1))
```

# Examples Get Tickers:

- S&P 500
```shell
python
from data import tickers
data = tickers.standard_and_poors_500(include_company_data=False)
```
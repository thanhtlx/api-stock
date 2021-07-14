# API STOCK
## Api Useful To Get Historical Stock Price Values

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Installation

API STOCK requires [Python 3](https://www.python.org/)  to run.
Install 
```
pip install apiStock
```
#### Featured Methods
1. getStockHistory(code, start_date, end_date)
   - code stock in Vietnam Stock Market.
   - start_date should be entered in the ‘YYYY-MM-DD’ format and is the first day that data will be pulled for.
   - end_date should be entered in the ‘YYYY-MM-DD’ format and is the last day that data will be pulled for.
#### Use
```python
from apiStock import getStockHistory
vin_prices = getStockHistory('VIN', '2019-08-19', '2020-08-19')
```

## License

MIT

**Free Library, Hell Yeah!**
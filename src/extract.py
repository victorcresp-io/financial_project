import os

import yfinance as yf
import pandas as pd

commodities = [
    'BTC-USD',
    'ETH-USD'
]

def search_commodities(simbol, period = '5d', interval = '1d'):
    ticker = yf.Ticker(simbol)
    data = ticker.history(period = period, interval = interval)
    data['simbol'] = simbol
    return data

def search_every_commodities(commodities):
    every_data = []
    for simbol in commodities:
        data = search_commodities(simbol)
        every_data.append(data)
    return pd.concat(every_data)

if __name__ == "__main__":
    result = search_every_commodities(commodities)
    print(f'The type of result is: {type(result)}')
    print(result.info())
    print(result.head())
    print(result.columns)
    print(result['simbol'].unique())
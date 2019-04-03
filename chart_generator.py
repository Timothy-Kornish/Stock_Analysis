from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import os
import pydoc

symbols = ['MSFT', 'IBM', 'NVDA', 'GOOGL']
API_KEY = 'TVWEXLQTCHKV4QK2'
#matplotlib.rcParams['figure.figsize'] = (20.0,10.0)

TS = TimeSeries(key = API_KEY, output_format = 'pandas')
TI = TechIndicators(key = API_KEY, output_format = 'pandas')

nvda_data, metadata = TS.get_intraday(symbol = symbols[2], interval = '1min', outputsize = 'full')
nvda_macd, nvda_metadata = TI.get_macd(symbol = symbols[2], interval='daily', series_type='close')
nvda_rsi, nvda_rsi_metadata = TI.get_rsi(symbol = symbols[2], interval='daily', series_type='close')

"""
print(nvda_data.head())
print(nvda_data.columns)
index = list(nvda_data.index)
print(nvda_data.index)
print(index)
"""

print(nvda_data.describe())
print(nvda_data.head())
print(nvda_macd.head())
print(nvda_rsi.head())

nvda_macd['date'] = nvda_macd.index
nvda_rsi['date'] = nvda_rsi.index

print(nvda_macd.head())
print(nvda_rsi.head())
#nvda_data['4. close'].plot()
#plt.title('Intraday Time Series for the NVDA stock (1 min intervals)')
#plt.grid()
#plt.show()
#print()

plt.plot(nvda_macd['date'], nvda_macd['MACD'])
plt.show()
#plt.plot(nvda_rsi['date'], nvda_rsi['RSI'])
#plt.plot()
#nvda_macd['MACD'].plot()
#nvda_rsi['RSI'].plot()
#plt.show()

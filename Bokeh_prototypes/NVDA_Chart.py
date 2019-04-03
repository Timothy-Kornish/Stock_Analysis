from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
import pandas as pd
import numpy as np
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
import os
import pydoc

symbol = 'NVDA'
API_KEY = 'TVWEXLQTCHKV4QK2'

def datetime(x):
    return np.array(x, dtype=np.datetime64)

def set_date_column(df):
    df['date'] = df.index
    df.reset_index(drop = True, inplace = True)
    return df


TS = TimeSeries(key = API_KEY, output_format = 'pandas')
TI = TechIndicators(key = API_KEY, output_format = 'pandas')

nvda_intraday_data, metadata = TS.get_intraday(symbol = symbol, interval = '1min', outputsize = 'full')
nvda_macd, nvda_metadata = TI.get_macd(symbol = symbol, interval='daily', series_type='close')
nvda_rsi, nvda_rsi_metadata = TI.get_rsi(symbol = symbol, interval='daily', series_type='close')

#nvda_intraday_data['date'] = nvda_intraday_data.index
#nvda_macd['date'] = nvda_macd.index
#nvda_rsi['date'] = nvda_rsi.index
#nvda_intraday_data.reset_index(drop = True, inplace = True)

nvda_intraday_data = set_date_column(nvda_intraday_data)
nvda_macd = set_date_column(nvda_macd)
nvda_rsi = set_date_column(nvda_rsi)

nvda_intraday_data = nvda_intraday_data.to_dict(orient = 'list')
nvda_macd = nvda_macd.to_dict(orient = 'list')
nvda_rsi = nvda_rsi.to_dict(orient = 'list')


p1 = figure(x_axis_type="datetime", title="Stock Closing Prices")
p1.grid.grid_line_alpha=0.3
p1.xaxis.axis_label = 'Date'
p1.yaxis.axis_label = 'Price'
location = nvda_intraday_data['date'].index('2019-04-02 09:31:00')
p1.line(datetime(nvda_intraday_data['date'][location:]), nvda_intraday_data['4. close'][location:], color='#A6CEE3', legend='NVDA')

p2 = figure(x_axis_type="datetime", title="MACD")
macd_timeframe = nvda_macd['date'].index('2018-10-02')
hist, edges = np.histogram(nvda_macd['MACD_Hist'][macd_timeframe:], density = True, bins=180)
p2.quad(top = hist, bottom = 0, left = edges[:-1], right = edges[1:], fill_color = 'navy', line_color = 'white', alpha = 0.5)
p2.grid.grid_line_alpha=0.3
p2.xaxis.axis_label = 'Date'
p2.yaxis.axis_label = 'Price'
p2.line(datetime(nvda_macd['date'][macd_timeframe:]), nvda_macd['MACD'][macd_timeframe:], color='#A6CEE3', legend='NVDA')

p3 = figure(x_axis_type="datetime", title="RSI")
p3.grid.grid_line_alpha=0.3
p3.xaxis.axis_label = 'Date'
p3.yaxis.axis_label = 'Price'
rsi_timeframe = nvda_rsi['date'].index('2018-10-02')
p3.line(datetime(nvda_rsi['date'][rsi_timeframe:]), nvda_rsi['RSI'][rsi_timeframe:], color='#A6CEE3', legend='NVDA')

output_file("NVDA_stocks.html", title="stocks.py example")

show(gridplot([[p1], [p2], [p3]], plot_width=800, plot_height=400))
"""
"""

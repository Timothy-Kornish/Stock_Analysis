from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
import pandas as pd
import numpy as np
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from bokeh.models.glyphs import Patch
from bokeh.models import ColumnDataSource
import os
import pydoc
from datetime import datetime, timedelta

symbol = 'MSFT'
API_KEY = 'TVWEXLQTCHKV4QK2'

def get_intraday_start():
    now = datetime.now()
    return now.strftime('%Y-%m-%d') + ' 09:31:00'

def get_6_months_ago():
    return (datetime.now() - timedelta(days = 182)).strftime('%Y-%m-%d')

def get_1_year_ago():
    month = datetime.now().month
    day = datetime.now().day
    if day > 0 and day < 10:
        day = '0' + str(day)
    if month > 0 and month < 10:
        month = '0' + str(month)
    year = datetime.now().year - 1
    return str(year) + '-' + str(month) + '-' + str(day)

intraday_start = get_intraday_start()
six_months_ago = get_6_months_ago()
year_ago = get_1_year_ago()

def datetime(x):
    return np.array(x, dtype=np.datetime64)

def set_date_column(df):
    df['date'] = df.index
    df.reset_index(drop = True, inplace = True)
    return df


TS = TimeSeries(key = API_KEY, output_format = 'pandas')
TI = TechIndicators(key = API_KEY, output_format = 'pandas')

nvda_intraday_data, metadata = TS.get_intraday(symbol = symbol, interval = '1min', outputsize = 'full')
nvda_day_data, nvda_day_metadata = TS.get_daily(symbol = symbol, outputsize = 'full')
nvda_macd, nvda_metadata = TI.get_macd(symbol = symbol, interval='daily', series_type='close')
nvda_rsi, nvda_rsi_metadata = TI.get_rsi(symbol = symbol, interval='daily', series_type='close')

#intraday_ema, intraday_ema_metadata = TI.get_ema(symbol = symbol, interval = '1min', time_period = 30, series_type = 'close')

nvda_intraday_data = set_date_column(nvda_intraday_data)
nvda_day_data = set_date_column(nvda_day_data)
nvda_macd = set_date_column(nvda_macd)
nvda_rsi = set_date_column(nvda_rsi)
#intraday_ema = set_date_column(intraday_ema)
nvda_macd.loc[:,'zero'] = 0

nvda_intraday_data = nvda_intraday_data.to_dict(orient = 'list')
nvda_day_data = nvda_day_data.to_dict(orient = 'list')
nvda_macd = nvda_macd.to_dict(orient = 'list')
nvda_rsi = nvda_rsi.to_dict(orient = 'list')
#intraday_ema = intraday_ema.to_dict(orient = 'list')

p1 = figure(x_axis_type="datetime", title="Stock Closing Prices - Today")
p1.grid.grid_line_alpha=0.3
p1.xaxis.axis_label = 'Date'
p1.yaxis.axis_label = 'Price'
location = nvda_intraday_data['date'].index(intraday_start)
#p1.line(datetime(intraday_ema['date'][location:]), intraday_ema['EMA'][location:], color='#464E43', legend=symbol)
p1.line(datetime(nvda_intraday_data['date'][location:]), nvda_intraday_data['4. close'][location:], color='#A6CEE3', legend=symbol)
p1.legend.location = 'bottom_right'

p1_2 = figure(x_axis_type="datetime", title="Stock Closing Prices - Week")
p1_2.grid.grid_line_alpha=0.3
p1_2.xaxis.axis_label = 'Date'
p1_2.yaxis.axis_label = 'Price'
#p1_2.line(datetime(intraday_ema['date']), intraday_ema['EMA'], color='#464E43', legend=symbol)
p1_2.line(datetime(nvda_intraday_data['date']), nvda_intraday_data['4. close'], color='#A6CEE3', legend=symbol)
p1_2.legend.location = 'bottom_right'

day_ema, day_ema_metadata = TI.get_ema(symbol = symbol, interval = 'daily', time_period = 20, series_type = 'close')
day_ema = set_date_column(day_ema)
day_ema = day_ema.to_dict(orient = 'list')

p1_3 = figure(x_axis_type="datetime", title="Stock Closing Prices - 6 Months")
p1_3.grid.grid_line_alpha=0.3
p1_3.xaxis.axis_label = 'Date'
p1_3.yaxis.axis_label = 'Price'
location = nvda_day_data['date'].index(six_months_ago)
p1_3.line(datetime(day_ema['date'][location:]), day_ema['EMA'][location:], color='#464E43', legend = symbol + ': EMA')
p1_3.line(datetime(nvda_day_data['date'][location:]), nvda_day_data['4. close'][location:], color='#A6CEE3', legend=symbol)
p1_3.legend.location = 'bottom_right'

p1_4 = figure(x_axis_type="datetime", title="Stock Closing Prices - Year")
p1_4.grid.grid_line_alpha=0.3
p1_4.xaxis.axis_label = 'Date'
p1_4.yaxis.axis_label = 'Price'
location = nvda_day_data['date'].index(year_ago)
p1_4.line(datetime(day_ema['date'][location:]), day_ema['EMA'][location:], color='#464E43', legend = symbol + ': EMA')
p1_4.line(datetime(nvda_day_data['date'][location:]), nvda_day_data['4. close'][location:], color='#A6CEE3', legend=symbol)
p1_4.legend.location = 'bottom_right'


p2 = figure(x_axis_type="datetime", title="MACD - 6 Months")
macd_timeframe = nvda_macd['date'].index(six_months_ago)

p2.grid.grid_line_alpha=0.3
p2.xaxis.axis_label = 'Date'
p2.yaxis.axis_label = 'Price'

p2.line(datetime(nvda_macd['date'][macd_timeframe:]), nvda_macd['MACD'][macd_timeframe:], color = '#1955C4', legend = symbol + ': MACD - 6 Months')
p2.line(datetime(nvda_macd['date'][macd_timeframe:]), nvda_macd['zero'][macd_timeframe:], color = '#000000', legend = symbol + ': MACD - Zero')
p2.line(datetime(nvda_macd['date'][macd_timeframe:]), nvda_macd['MACD_Hist'][macd_timeframe:], color = '#42CC14', legend = symbol + ': MACD - Hist')
p2.line(datetime(nvda_macd['date'][macd_timeframe:]), nvda_macd['MACD_Signal'][macd_timeframe:], color = '#8411C6', legend = symbol +': MACD - Signal')
p2.legend.location = 'bottom_right'

p2_2 = figure(x_axis_type="datetime", title="MACD - 12 Months")
macd_timeframe = nvda_macd['date'].index(year_ago)

p2_2.grid.grid_line_alpha=0.3
p2_2.xaxis.axis_label = 'Date'
p2_2.yaxis.axis_label = 'Price'

p2_2.line(datetime(nvda_macd['date'][macd_timeframe:]), nvda_macd['MACD'][macd_timeframe:], color = '#1955C4', legend = symbol + ': MACD - 12 Months')
p2_2.line(datetime(nvda_macd['date'][macd_timeframe:]), nvda_macd['zero'][macd_timeframe:], color = '#000000', legend = symbol + ': MACD - Zero')
p2_2.line(datetime(nvda_macd['date'][macd_timeframe:]), nvda_macd['MACD_Hist'][macd_timeframe:], color = '#42CC14', legend = symbol + ': MACD - Hist')
p2_2.line(datetime(nvda_macd['date'][macd_timeframe:]), nvda_macd['MACD_Signal'][macd_timeframe:], color = '#8411C6', legend = symbol +': MACD - Signal')
p2_2.legend.location = 'bottom_right'

p3 = figure(x_axis_type="datetime", title="RSI - 6 Months")
p3.grid.grid_line_alpha=0.3
p3.xaxis.axis_label = 'Date'
p3.yaxis.axis_label = 'Price'
rsi_timeframe = nvda_rsi['date'].index(six_months_ago)
p3.line(datetime(nvda_rsi['date'][rsi_timeframe:]), nvda_rsi['RSI'][rsi_timeframe:], color = '#A6CEE3', legend = symbol)
p3.legend.location = 'bottom_right'

p3_2 = figure(x_axis_type="datetime", title="RSI - 12 Months")
p3_2.grid.grid_line_alpha=0.3
p3_2.xaxis.axis_label = 'Date'
p3_2.yaxis.axis_label = 'Price'
rsi_timeframe = nvda_rsi['date'].index(year_ago)
p3_2.line(datetime(nvda_rsi['date'][rsi_timeframe:]), nvda_rsi['RSI'][rsi_timeframe:], color = '#A6CEE3', legend = symbol)
p3_2.legend.location = 'bottom_right'

output_file(symbol + "_stocks.html", title = symbol + " Charts")

show(gridplot([[p1, p1_2], [p1_3, p1_4], [p2, p2_2], [p3, p3_2]], plot_width=800, plot_height=400))
"""
"""

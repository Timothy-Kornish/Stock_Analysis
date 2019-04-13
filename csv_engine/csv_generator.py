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
from datetime import datetime, timedelta, date

symbol = 'AMD'
API_KEY = 'TVWEXLQTCHKV4QK2'
def output_file_to_csv(df, output_file_name):
    prefix = 'C:\\Users\\tlkor\\Stock_Market\\Stock_Analysis\\csv_engine\\CSVs\\'
    df.to_csv(prefix + output_file_name, index = True)

def get_date():
    return datetime.now().strftime('%Y-%m-%d')


TS = TimeSeries(key = API_KEY, output_format = 'pandas')
TI = TechIndicators(key = API_KEY, output_format = 'pandas')
"""

symbol_intraday_data, metadata = TS.get_intraday(symbol = symbol, interval = '1min', outputsize = 'full')
symbol_day_data, nvda_day_metadata = TS.get_daily(symbol = symbol, outputsize = 'full')

macd, nvda_metadata = TI.get_macd(symbol = symbol, interval='daily', series_type='close')
rsi, nvda_rsi_metadata = TI.get_rsi(symbol = symbol, interval='daily', series_type='close')
stoch, stoch_metadata = TI.get_stoch(symbol = symbol, interval = 'daily', slowdmatype = 1)


output_file_to_csv(symbol_intraday_data, symbol + '_intraday_' + get_date() + '.csv')
output_file_to_csv(symbol_day_data, symbol + '_day_' + get_date() + '.csv')
output_file_to_csv(macd, symbol + '_macd_' + get_date() + '.csv')
output_file_to_csv(rsi, symbol + '_rsi_' + get_date() + '.csv')
output_file_to_csv(stoch, symbol + '_stoch_' + get_date() + '.csv')
"""

adx_day, axd_day_metadata = TI.get_adx(symbol = symbol, interval = 'daily', time_period = 20)
dmi_minus, dmi_minus_metadata = TI.get_minus_di(symbol = symbol, interval = 'daily', time_period = 20)
dmi_plus, dmi_plus_metadata = TI.get_plus_di(symbol = symbol, interval = 'daily', time_period = 20)
bbands, bbands_metadata = TI.get_bbands(symbol = symbol, interval = 'daily', time_period = 20)
ema, day_ema_metadata = TI.get_ema(symbol = symbol, interval = 'daily', time_period = 20, series_type = 'close')
output_file_to_csv(ema, symbol + '_ema_' + get_date() + '.csv')
output_file_to_csv(adx_day, symbol + '_adx_day_' + get_date() + '.csv')
output_file_to_csv(dmi_minus, symbol + '_dmi_minus_' + get_date() + '.csv')
output_file_to_csv(dmi_plus, symbol + '_dmi_plus_' + get_date() + '.csv')
output_file_to_csv(bbands, symbol + '_bbands_' + get_date() + '.csv')

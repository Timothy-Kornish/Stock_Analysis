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

symbol = 'GOOGL'
API_KEY = 'TVWEXLQTCHKV4QK2'
TOOLS = "pan,wheel_zoom,box_zoom,reset,save,hover"

def get_intraday_start():
    now = datetime.now()
    return now.strftime('%Y-%m-%d') + ' 09:31:00'

def get_6_months_ago():
    return (datetime.now() - timedelta(days = 185)).strftime('%Y-%m-%d')

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

def get_date():
    return datetime.now().strftime('%Y-%m-%d')
today = get_date()

def datetime(x):
    return np.array(x, dtype=np.datetime64)

def set_array(x):
    return np.array(x, dtype=np.int64)

def set_date_column(df):
    df['date'] = df.index
    df.reset_index(drop = True, inplace = True)
    return df

def convert_date_str_to_int(date_val1, date_val2):
    date_val_list = date_val1.split('-')
    year = int(date_val_list[0])
    month = int(date_val_list[1])
    day = int(date_val_list[2])
    date_val_list2 = date_val2.split('-')
    year2 = int(date_val_list2[0])
    month2 = int(date_val_list2[1])
    day2 = int(date_val_list2[2])
    day_of_year = date(year, month, day)
    day_of_year2 = date(year2, month2, day2)
    delta = day_of_year - day_of_year2
    delta = delta.days
    return delta


def get_width(source):
    mindate = min(source['date'])
    maxdate = max(source['date'])
    days = convert_date_str_to_int(mindate, maxdate)
    width = 0.7 * (days)*24*60*60*1000 / len(source['date'])
    return abs(width)

TS = TimeSeries(key = API_KEY, output_format = 'pandas')
TI = TechIndicators(key = API_KEY, output_format = 'pandas')
"""
nvda_intraday_data, metadata = TS.get_intraday(symbol = symbol, interval = '1min', outputsize = 'full')
nvda_day_data, nvda_day_metadata = TS.get_daily(symbol = symbol, outputsize = 'full')
nvda_macd, nvda_metadata = TI.get_macd(symbol = symbol, interval='daily', series_type='close')
nvda_rsi, nvda_rsi_metadata = TI.get_rsi(symbol = symbol, interval='daily', series_type='close')

day_ema, day_ema_metadata = TI.get_ema(symbol = symbol, interval = 'daily', time_period = 20, series_type = 'close')
day_ema = set_date_column(day_ema)
day_ema = day_ema.to_dict(orient = 'list')

stoch, stoch_metadata = TI.get_stoch(symbol = symbol, interval = 'daily', slowdmatype = 1)
#print(stoch.head())
adx_day, axd_day_metadata = TI.get_adx(symbol = symbol, interval = 'daily', time_period = 20)
#print(adx_day.head())
dmi_minus, dmi_minus_metadata = TI.get_minus_di(symbol = symbol, interval = 'daily', time_period = 20)
#print(dmi_minus.head())
dmi_plus, dmi_plus_metadata = TI.get_plus_di(symbol = symbol, interval = 'daily', time_period = 20)
#print(dmi_plus.head())
bbands, bbands_metadata = TI.get_bbands(symbol = symbol, interval = 'daily', time_period = 20)
#print(bbands.head())
"""

nvda_intraday_data = pd.read_csv('C:\\Users\\tlkor\\Stock_Market\\Stock_Analysis\\csv_engine\\CSVs\\' + symbol + '_intraday_' + today +'.csv')
nvda_day_data = pd.read_csv('C:\\Users\\tlkor\\Stock_Market\\Stock_Analysis\\csv_engine\\CSVs\\' + symbol + '_day_' + today +'.csv')

nvda_macd = pd.read_csv('C:\\Users\\tlkor\\Stock_Market\\Stock_Analysis\\csv_engine\\CSVs\\' + symbol + '_macd_' + today +'.csv')
nvda_rsi = pd.read_csv('C:\\Users\\tlkor\\Stock_Market\\Stock_Analysis\\csv_engine\\CSVs\\' + symbol + '_rsi_' + today +'.csv')
stoch = pd.read_csv('C:\\Users\\tlkor\\Stock_Market\\Stock_Analysis\\csv_engine\\CSVs\\' + symbol + '_stoch_' + today +'.csv')
adx_day = pd.read_csv('C:\\Users\\tlkor\\Stock_Market\\Stock_Analysis\\csv_engine\\CSVs\\' + symbol + '_adx_day_' + today +'.csv')
dmi_minus = pd.read_csv('C:\\Users\\tlkor\\Stock_Market\\Stock_Analysis\\csv_engine\\CSVs\\' + symbol + '_dmi_minus_' + today +'.csv')
dmi_plus = pd.read_csv('C:\\Users\\tlkor\\Stock_Market\\Stock_Analysis\\csv_engine\\CSVs\\' + symbol + '_dmi_plus_' + today +'.csv')
bbands = pd.read_csv('C:\\Users\\tlkor\\Stock_Market\\Stock_Analysis\\csv_engine\\CSVs\\' + symbol + '_bbands_' + today +'.csv')
day_ema = pd.read_csv('C:\\Users\\tlkor\\Stock_Market\\Stock_Analysis\\csv_engine\\CSVs\\' + symbol + '_ema_' + today +'.csv')
#intraday_ema, intraday_ema_metadata = TI.get_ema(symbol = symbol, interval = '1min', time_period = 30, series_type = 'close')

print(day_ema.head())
"""
nvda_intraday_data = set_date_column(nvda_intraday_data)
nvda_day_data = set_date_column(nvda_day_data)
nvda_macd = set_date_column(nvda_macd)
nvda_rsi = set_date_column(nvda_rsi)
stoch = set_date_column(stoch)
adx_day = set_date_column(adx_day)
dmi_minus = set_date_column(dmi_minus)
dmi_plus = set_date_column(dmi_plus)
bbands = set_date_column(bbands)
"""
nvda_day_data_6_month = nvda_day_data
nvda_day_data_1_year = nvda_day_data
nvda_day_data_6_month = nvda_day_data[-130:]
nvda_day_data_1_year = nvda_day_data[-260:]


#intraday_ema = set_date_column(intraday_ema)
nvda_macd.loc[:,'zero'] = 0

nvda_intraday_data = nvda_intraday_data.to_dict(orient = 'list')
nvda_day_data = nvda_day_data.to_dict(orient = 'list')
#nvda_day_data_6_month = nvda_day_data_6_month.to_dict(orient = 'list')
#nvda_day_data_1_year = nvda_day_data_1_year.to_dict(orient = 'list')
nvda_macd = nvda_macd.to_dict(orient = 'list')
nvda_rsi = nvda_rsi.to_dict(orient = 'list')

stoch = stoch.to_dict(orient = 'list')
adx_day = adx_day.to_dict(orient = 'list')
dmi_minus = dmi_minus.to_dict(orient = 'list')
dmi_plus = dmi_plus.to_dict(orient = 'list')
bbands = bbands.to_dict(orient = 'list')
#intraday_ema = intraday_ema.to_dict(orient = 'list')

p1 = figure(x_axis_type="datetime", tools = TOOLS, title="Stock Closing Prices - Today")
p1.grid.grid_line_alpha=0.3
p1.xaxis.axis_label = 'Date'
p1.yaxis.axis_label = 'Price'
#p1.line(datetime(intraday_ema['date'][location:]), intraday_ema['EMA'][location:], color='#464E43', legend=symbol)
p1.line(datetime(nvda_intraday_data['date']), nvda_intraday_data['4. close'], color='#A6CEE3', legend=symbol)
p1.legend.location = 'bottom_right'

p1_2 = figure(x_axis_type="datetime", tools = TOOLS, title="Stock Closing Prices - Week")
p1_2.grid.grid_line_alpha=0.3
p1_2.xaxis.axis_label = 'Date'
p1_2.yaxis.axis_label = 'Price'
#p1_2.line(datetime(intraday_ema['date']), intraday_ema['EMA'], color='#464E43', legend=symbol)
p1_2.line(datetime(nvda_intraday_data['date']), nvda_intraday_data['4. close'], color='#A6CEE3', legend=symbol)
p1_2.legend.location = 'bottom_right'

p1_3 = figure(x_axis_type="datetime", tools = TOOLS, title="Stock Closing Prices - 6 Months")
p1_3.grid.grid_line_alpha=0.3
p1_3.xaxis.axis_label = 'Date'
p1_3.yaxis.axis_label = 'Price'
location = -130 #nvda_day_data['date'].index(six_months_ago)
p1_3.line(datetime(list(day_ema['date'][location:])), day_ema['EMA'][location:], color='#464E43', legend = symbol + ': EMA')
p1_3.line(datetime(nvda_day_data['date'][location:]), nvda_day_data['4. close'][location:], color='#A6CEE3', legend=symbol)
p1_3.legend.location = 'bottom_right'

p1_4 = figure(x_axis_type="datetime", tools = TOOLS, title="Stock Closing Prices - Year")
p1_4.grid.grid_line_alpha=0.3
p1_4.xaxis.axis_label = 'Date'
p1_4.yaxis.axis_label = 'Price'
location = -260 #nvda_day_data['date'].index(year_ago)
p1_4.line(datetime(list(day_ema['date'][location:])), day_ema['EMA'][location:], color='#464E43', legend = symbol + ': EMA')
p1_4.line(datetime(nvda_day_data['date'][location:]), nvda_day_data['4. close'][location:], color='#A6CEE3', legend=symbol)
p1_4.legend.location = 'bottom_right'

p1_5 = figure(x_axis_type="datetime", tools = TOOLS, title="Stock Closing Prices - 6 Months")

w = 24*130*60*60*1000
p1_5.grid.grid_line_alpha=0.3
p1_5.xaxis.axis_label = 'Date'
p1_5.yaxis.axis_label = 'Price'
location = -130 #nvda_day_data['date'].index(six_months_ago)
six_month_inc = nvda_day_data_6_month['4. close'] > nvda_day_data_6_month['1. open']
six_month_dec = nvda_day_data_6_month['4. close'] < nvda_day_data_6_month['1. open']
p1_5.line(datetime(bbands['date'][location:]), bbands['Real Upper Band'][location:], color = '#fcb23c', legend = symbol + ': BBand upper')
p1_5.line(datetime(bbands['date'][location:]), bbands['Real Middle Band'][location:], color = '#8c20e5', legend = symbol + ': BBand middle')
p1_5.line(datetime(bbands['date'][location:]), bbands['Real Lower Band'][location:], color = '#fcb23c', legend = symbol + ': BBand lower')
p1_5.segment(x0 = datetime(list(nvda_day_data_6_month['date'])), y0 = set_array(nvda_day_data_6_month['2. high']), x1 = datetime(list(nvda_day_data_6_month['date'])), y1 = set_array(nvda_day_data_6_month['3. low']), color="black")
p1_5.vbar(x = datetime(list(nvda_day_data_6_month['date'][six_month_inc])), width = get_width(nvda_day_data_6_month), top = list(nvda_day_data_6_month['1. open'][six_month_inc]), bottom = list(nvda_day_data_6_month['4. close'][six_month_inc]), fill_color="#07B229", line_color="black", legend = symbol + ': inc')
p1_5.vbar(x = datetime(list(nvda_day_data_6_month['date'][six_month_dec])), width = get_width(nvda_day_data_6_month), top = list(nvda_day_data_6_month['4. close'][six_month_dec]), bottom = list(nvda_day_data_6_month['1. open'][six_month_dec]), fill_color="#F2583E", line_color="black", legend = symbol + ': dec')
p1_5.legend.location = 'bottom_right'

p1_6 = figure(x_axis_type="datetime", tools = TOOLS, title="Stock Closing Prices - Year")
p1_6.grid.grid_line_alpha=0.3
p1_6.xaxis.axis_label = 'Date'
p1_6.yaxis.axis_label = 'Price'
location = -260 #nvda_day_data['date'].index(year_ago)
one_year_inc = nvda_day_data_1_year['4. close'] > nvda_day_data_1_year['1. open']
one_year_dec = nvda_day_data_1_year['4. close'] < nvda_day_data_1_year['1. open']
p1_6.line(datetime(bbands['date'][location:]), bbands['Real Upper Band'][location:], color = '#fcb23c', legend = symbol + ': BBand upper')
p1_6.line(datetime(bbands['date'][location:]), bbands['Real Middle Band'][location:], color = '#8c20e5', legend = symbol + ': BBand middle')
p1_6.line(datetime(bbands['date'][location:]), bbands['Real Lower Band'][location:], color = '#fcb23c', legend = symbol + ': BBand lower')
p1_6.segment(x0 = datetime(list(nvda_day_data_1_year['date'])), y0 = nvda_day_data_1_year['2. high'], x1 = datetime(list(nvda_day_data_1_year['date'])), y1 = nvda_day_data_1_year['3. low'], color="black")
p1_6.vbar(x = datetime(list(nvda_day_data_1_year['date'][one_year_inc])), width = get_width(nvda_day_data_1_year), top = nvda_day_data_1_year['1. open'][one_year_inc], bottom = nvda_day_data_1_year['4. close'][one_year_inc], fill_color="#07B229", line_color="black", legend = symbol + ': inc')
p1_6.vbar(x = datetime(list(nvda_day_data_1_year['date'][one_year_dec])), width = get_width(nvda_day_data_1_year), top = nvda_day_data_1_year['4. close'][one_year_dec], bottom = nvda_day_data_1_year['1. open'][one_year_dec],  fill_color="#F2583E", line_color="black", legend = symbol + ': dec')
p1_6.legend.location = 'bottom_right'


p2 = figure(x_axis_type="datetime", tools = TOOLS, title="MACD - 6 Months")
macd_timeframe = -130# nvda_macd['date'].index(six_months_ago)

p2.grid.grid_line_alpha=0.3
p2.xaxis.axis_label = 'Date'
p2.yaxis.axis_label = 'Price'

p2.line(datetime(nvda_macd['date'][macd_timeframe:]), nvda_macd['MACD'][macd_timeframe:], color = '#1955C4', legend = symbol + ': MACD - 6 Months')
p2.line(datetime(nvda_macd['date'][macd_timeframe:]), nvda_macd['zero'][macd_timeframe:], color = '#000000', legend = symbol + ': MACD - Zero')
p2.line(datetime(nvda_macd['date'][macd_timeframe:]), nvda_macd['MACD_Hist'][macd_timeframe:], color = '#42CC14', legend = symbol + ': MACD - Hist')
p2.line(datetime(nvda_macd['date'][macd_timeframe:]), nvda_macd['MACD_Signal'][macd_timeframe:], color = '#8411C6', legend = symbol +': MACD - Signal')
p2.legend.location = 'bottom_right'

p2_2 = figure(x_axis_type="datetime", tools = TOOLS, title="MACD - 12 Months")
macd_timeframe = -260 #nvda_macd['date'].index(year_ago)

p2_2.grid.grid_line_alpha=0.3
p2_2.xaxis.axis_label = 'Date'
p2_2.yaxis.axis_label = 'Price'

p2_2.line(datetime(nvda_macd['date'][macd_timeframe:]), nvda_macd['MACD'][macd_timeframe:], color = '#1955C4', legend = symbol + ': MACD - 12 Months')
p2_2.line(datetime(nvda_macd['date'][macd_timeframe:]), nvda_macd['zero'][macd_timeframe:], color = '#000000', legend = symbol + ': MACD - Zero')
p2_2.line(datetime(nvda_macd['date'][macd_timeframe:]), nvda_macd['MACD_Hist'][macd_timeframe:], color = '#42CC14', legend = symbol + ': MACD - Hist')
p2_2.line(datetime(nvda_macd['date'][macd_timeframe:]), nvda_macd['MACD_Signal'][macd_timeframe:], color = '#8411C6', legend = symbol +': MACD - Signal')
p2_2.legend.location = 'bottom_right'

p3 = figure(x_axis_type="datetime", tools = TOOLS, title="RSI - 6 Months")
p3.grid.grid_line_alpha=0.3
p3.xaxis.axis_label = 'Date'
p3.yaxis.axis_label = 'Price'
rsi_timeframe = -130 #nvda_rsi['date'].index(six_months_ago)
p3.line(datetime(nvda_rsi['date'][rsi_timeframe:]), nvda_rsi['RSI'][rsi_timeframe:], color = '#A6CEE3', legend = symbol)
p3.legend.location = 'bottom_right'

p3_2 = figure(x_axis_type="datetime", tools = TOOLS, title="RSI - 12 Months")
p3_2.grid.grid_line_alpha=0.3
p3_2.xaxis.axis_label = 'Date'
p3_2.yaxis.axis_label = 'Price'
rsi_timeframe = -260 #nvda_rsi['date'].index(year_ago)
p3_2.line(datetime(nvda_rsi['date'][rsi_timeframe:]), nvda_rsi['RSI'][rsi_timeframe:], color = '#A6CEE3', legend = symbol)
p3_2.legend.location = 'bottom_right'

p4_1 = figure(x_axis_type="datetime", tools = TOOLS, title="ADX - 6 Months")
p4_1.grid.grid_line_alpha=0.3
p4_1.xaxis.axis_label = 'Date'
p4_1.yaxis.axis_label = 'Price'
location = -130
p4_1.line(datetime(adx_day['date'][location:]), adx_day['ADX'][location:], color = '#A6CEE3', legend = symbol + ': ADX')
p4_1.line(datetime(dmi_minus['date'][location:]), dmi_minus['MINUS_DI'][location:], color = '#0cad21', legend = symbol  + ': DMI+')
p4_1.line(datetime(dmi_plus['date'][location:]), dmi_plus['PLUS_DI'][location:], color = '#a50914', legend = symbol + ': DMI-')
p4_1.legend.location = 'bottom_right'

p4_2 = figure(x_axis_type="datetime", tools = TOOLS, title="ADX - 12 Months")
p4_2.grid.grid_line_alpha=0.3
p4_2.xaxis.axis_label = 'Date'
p4_2.yaxis.axis_label = 'Price'
location = -260
p4_2.line(datetime(adx_day['date'][location:]), adx_day['ADX'][location:], color = '#A6CEE3', legend = symbol + ': ADX')
p4_2.line(datetime(dmi_minus['date'][location:]), dmi_minus['MINUS_DI'][location:], color = '#0cad21', legend = symbol + ': DMI+')
p4_2.line(datetime(dmi_plus['date'][location:]), dmi_plus['PLUS_DI'][location:], color = '#a50914', legend = symbol + ': DMI-')
p4_2.legend.location = 'bottom_right'

p5_1 = figure(x_axis_type="datetime", tools = TOOLS, title="STOCH - 6 Months")
p5_1.grid.grid_line_alpha=0.3
p5_1.xaxis.axis_label = 'Date'
p5_1.yaxis.axis_label = 'Price'
location = -130
p5_1.line(datetime(stoch['date'][location:]), stoch['SlowD'][location:], color = '#A6CEE3', legend = symbol + ': STOCH slow-D')
p5_1.line(datetime(stoch['date'][location:]), stoch['SlowK'][location:], color = '#a50914', legend = symbol + ': STOCH slow-K')
p5_1.legend.location = 'bottom_right'

p5_2 = figure(x_axis_type="datetime", tools = TOOLS, title="STOCH - 12 Months")
p5_2.grid.grid_line_alpha=0.3
p5_2.xaxis.axis_label = 'Date'
p5_2.yaxis.axis_label = 'Price'
location = -260
p5_2.line(datetime(stoch['date'][location:]), stoch['SlowD'][location:], color = '#A6CEE3', legend = symbol + ': STOCH slow-D')
p5_2.line(datetime(stoch['date'][location:]), stoch['SlowK'][location:], color = '#a50914', legend = symbol + ': STOCH slow-K')
p5_2.legend.location = 'bottom_right'




output_file(symbol + "_stocks.html", title = symbol + " Charts")

show(gridplot([[p1, p1_2], [p1_3, p1_4], [p1_5, p1_6], [p2, p2_2], [p3, p3_2], [p4_1, p4_2], [p5_1, p5_2]], plot_width=800, plot_height=400))
"""
"""

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

API_KEY = 'TVWEXLQTCHKV4QK2'

class Charts:

    intraday_start = get_intraday_start()
    six_months_ago = get_6_months_ago()
    year_ago = get_1_year_ago()

    def get_intraday_start(self):
        now = datetime.now()
        return now.strftime('%Y-%m-%d') + ' 09:31:00'

    def get_6_months_ago(self):
        return (datetime.now() - timedelta(days = 182)).strftime('%Y-%m-%d')

    def get_1_year_ago(self):
        month = datetime.now().month
        day = datetime.now().day
        if day > 0 and day < 10:
            day = '0' + str(day)
        if month > 0 and month < 10:
            month = '0' + str(month)
        year = datetime.now().year - 1
        return str(year) + '-' + str(month) + '-' + str(day)

    def datetime(x):
        return np.array(x, dtype=np.datetime64)

    def set_date_column(df):
        df['date'] = df.index
        df.reset_index(drop = True, inplace = True)
        return df

    def create_intraday_plot(self, symbol, df, intraday_data, intraday_ema):
        plot = figure(x_axis_type="datetime", title="Stock Closing Prices - Today")
        plot.grid.grid_line_alpha=0.3
        plot.xaxis.axis_label = 'Date'
        plot.yaxis.axis_label = 'Price'
        location = intraday_data['date'].index(intraday_start)
        plot.line(datetime(intraday_ema['date'][location:]), intraday_ema['EMA'][location:], color='#464E43', legend=symbol)
        plot.line(datetime(intraday_data['date'][location:]), intraday_data['4. close'][location:], color='#A6CEE3', legend=symbol)
        plot.legend.location = 'bottom_left'
        return plot

    def create_week(self, symbol):
        plot = figure(x_axis_type="datetime", title="Stock Closing Prices - Week")
        plot.grid.grid_line_alpha=0.3
        plot.xaxis.axis_label = 'Date'
        plot.yaxis.axis_label = 'Price'
        plot.line(datetime(intraday_ema['date']), intraday_ema['EMA'], color='#464E43', legend=symbol)
        plot.line(datetime(nvda_intraday_data['date']), nvda_intraday_data['4. close'], color='#A6CEE3', legend=symbol)
        plot.legend.location = 'bottom_left'
        return plot

    def create_6_month(self, symbol):
        plot = figure(x_axis_type="datetime", title="Stock Closing Prices - 6 Months")
        plot.grid.grid_line_alpha=0.3
        plot.xaxis.axis_label = 'Date'
        plot.yaxis.axis_label = 'Price'
        location = nvda_day_data['date'].index(six_months_ago)
        plot.line(datetime(day_ema['date'][location:]), day_ema['EMA'][location:], color='#464E43', legend = symbol + ': EMA')
        plot.line(datetime(nvda_day_data['date'][location:]), nvda_day_data['4. close'][location:], color='#A6CEE3', legend=symbol)
        plot.legend.location = 'bottom_right'
        return plot

    def create_year(self, symbol):
        plot = figure(x_axis_type="datetime", title="Stock Closing Prices - Year")
        plot.grid.grid_line_alpha=0.3
        plot.xaxis.axis_label = 'Date'
        plot.yaxis.axis_label = 'Price'
        location = nvda_day_data['date'].index(year_ago)
        plot.line(datetime(day_ema['date'][location:]), day_ema['EMA'][location:], color='#464E43', legend = symbol + ': EMA')
        plot.line(datetime(nvda_day_data['date'][location:]), nvda_day_data['4. close'][location:], color='#A6CEE3', legend=symbol)
        plot.legend.location = 'bottom_right'
        return plot

    def create_MACD(self, symbol):
        plot = figure(x_axis_type="datetime", title="MACD - 12 Months")
        macd_timeframe = nvda_macd['date'].index(year_ago)

        plot.grid.grid_line_alpha=0.3
        plot.xaxis.axis_label = 'Date'
        plot.yaxis.axis_label = 'Price'

        plot.line(datetime(nvda_macd['date'][macd_timeframe:]), nvda_macd['MACD'][macd_timeframe:], color = '#1955C4', legend = symbol + ': MACD - 12 Months')
        plot.line(datetime(nvda_macd['date'][macd_timeframe:]), nvda_macd['zero'][macd_timeframe:], color = '#000000', legend = symbol + ': MACD - Zero')
        plot.line(datetime(nvda_macd['date'][macd_timeframe:]), nvda_macd['MACD_Hist'][macd_timeframe:], color = '#42CC14', legend = symbol + ': MACD - Hist')
        plot.line(datetime(nvda_macd['date'][macd_timeframe:]), nvda_macd['MACD_Signal'][macd_timeframe:], color = '#8411C6', legend = symbol +': MACD - Signal')
        plot.legend.location = 'bottom_right'
        return plot

    def create_RSI(self, symbol):
        plot = figure(x_axis_type="datetime", title="RSI - 6 Months")
        plot.grid.grid_line_alpha=0.3
        plot.xaxis.axis_label = 'Date'
        plot.yaxis.axis_label = 'Price'
        rsi_timeframe = nvda_rsi['date'].index(six_months_ago)
        plot.line(datetime(nvda_rsi['date'][rsi_timeframe:]), nvda_rsi['RSI'][rsi_timeframe:], color = '#A6CEE3', legend = symbol)
        plot.legend.location = 'bottom_right'
        return plot

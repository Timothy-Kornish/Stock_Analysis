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
matplotlib.rcParams['figure.figsize'] = (20.0,10.0)

print(dir(TimeSeries))
print('\n------------------------\n')
print(dir(TechIndicators))
print('\n------------------------\n')
print(dir(SectorPerformances))
print('\n------------------------\n')



"""
TimeSeries

"""
timeSeries = ''
get_batch_stock_quotes = pydoc.plain(pydoc.render_doc(TimeSeries.get_batch_stock_quotes, "Help on %s"))
get_daily              = pydoc.plain(pydoc.render_doc(TimeSeries.get_daily, "Help on %s"))
get_daily_adjusted     = pydoc.plain(pydoc.render_doc(TimeSeries.get_daily_adjusted, "Help on %s"))
get_intraday           = pydoc.plain(pydoc.render_doc(TimeSeries.get_intraday, "Help on %s"))
get_monthly            = pydoc.plain(pydoc.render_doc(TimeSeries.get_monthly, "Help on %s"))
get_monthly_adjusted   = pydoc.plain(pydoc.render_doc(TimeSeries.get_monthly_adjusted, "Help on %s"))
get_weekly             = pydoc.plain(pydoc.render_doc(TimeSeries.get_weekly, "Help on %s"))
get_weekly_adjusted    = pydoc.plain(pydoc.render_doc(TimeSeries.get_weekly_adjusted, "Help on %s"))
map_to_matype          = pydoc.plain(pydoc.render_doc(TimeSeries.map_to_matype, "Help on %s"))
set_proxy              = pydoc.plain(pydoc.render_doc(TimeSeries.set_proxy, "Help on %s"))

timeSeries = get_batch_stock_quotes + '\n----------------------------------------------------------------------\n\n' + get_daily + '\n----------------------------------------------------------------------\n\n' + get_daily_adjusted + '\n----------------------------------------------------------------------\n\n' + get_intraday + '\n----------------------------------------------------------------------\n\n'
timeSeries = timeSeries + get_monthly + '\n----------------------------------------------------------------------\n\n' + get_monthly_adjusted + '\n----------------------------------------------------------------------\n\n' + get_weekly + '\n----------------------------------------------------------------------\n\n' + get_weekly_adjusted + '\n----------------------------------------------------------------------\n\n'
timeSeries = timeSeries + map_to_matype + '\n----------------------------------------------------------------------\n\n' + set_proxy

with open("Time_Series.txt", "w") as time_file:
   time_file.write(timeSeries)

"""
TechIndicators

"""
get_ad           = pydoc.plain(pydoc.render_doc(TechIndicators.get_ad, "Help on %s"))
get_adosc        = pydoc.plain(pydoc.render_doc(TechIndicators.get_adosc, "Help on %s"))
get_adx          = pydoc.plain(pydoc.render_doc(TechIndicators.get_adx, "Help on %s"))
get_adxr         = pydoc.plain(pydoc.render_doc(TechIndicators.get_adxr, "Help on %s"))
get_apo          = pydoc.plain(pydoc.render_doc(TechIndicators.get_apo, "Help on %s"))
get_aroon        = pydoc.plain(pydoc.render_doc(TechIndicators.get_aroon, "Help on %s"))
get_aroonosc     = pydoc.plain(pydoc.render_doc(TechIndicators.get_aroonosc, "Help on %s"))
get_atr          = pydoc.plain(pydoc.render_doc(TechIndicators.get_atr, "Help on %s"))
get_bbands       = pydoc.plain(pydoc.render_doc(TechIndicators.get_bbands, "Help on %s"))
get_bop          = pydoc.plain(pydoc.render_doc(TechIndicators.get_bop, "Help on %s"))
get_cci          = pydoc.plain(pydoc.render_doc(TechIndicators.get_cci, "Help on %s"))
get_cmo          = pydoc.plain(pydoc.render_doc(TechIndicators.get_cmo, "Help on %s"))
get_dema         = pydoc.plain(pydoc.render_doc(TechIndicators.get_dema, "Help on %s"))
get_dx           = pydoc.plain(pydoc.render_doc(TechIndicators.get_dx, "Help on %s"))
get_ema          = pydoc.plain(pydoc.render_doc(TechIndicators.get_ema, "Help on %s"))
get_ht_dcperiod  = pydoc.plain(pydoc.render_doc(TechIndicators.get_ht_dcperiod, "Help on %s"))
get_ht_dcphase   = pydoc.plain(pydoc.render_doc(TechIndicators.get_ht_dcphase, "Help on %s"))
get_ht_phasor    = pydoc.plain(pydoc.render_doc(TechIndicators.get_ht_phasor, "Help on %s"))
get_ht_sine      = pydoc.plain(pydoc.render_doc(TechIndicators.get_ht_sine, "Help on %s"))
get_ht_trendline = pydoc.plain(pydoc.render_doc(TechIndicators.get_ht_trendline, "Help on %s"))
get_ht_trendmode = pydoc.plain(pydoc.render_doc(TechIndicators.get_ht_trendmode, "Help on %s"))
get_kama         = pydoc.plain(pydoc.render_doc(TechIndicators.get_kama, "Help on %s"))
get_macd         = pydoc.plain(pydoc.render_doc(TechIndicators.get_macd, "Help on %s"))
get_macdext      = pydoc.plain(pydoc.render_doc(TechIndicators.get_macdext, "Help on %s"))
get_mama         = pydoc.plain(pydoc.render_doc(TechIndicators.get_mama, "Help on %s"))
get_mfi          = pydoc.plain(pydoc.render_doc(TechIndicators.get_mfi, "Help on %s"))
get_midpoint     = pydoc.plain(pydoc.render_doc(TechIndicators.get_midpoint, "Help on %s"))
get_midprice     = pydoc.plain(pydoc.render_doc(TechIndicators.get_midprice, "Help on %s"))
get_minus_di     = pydoc.plain(pydoc.render_doc(TechIndicators.get_minus_di, "Help on %s"))
get_minus_dm     = pydoc.plain(pydoc.render_doc(TechIndicators.get_minus_dm, "Help on %s"))
get_mom          = pydoc.plain(pydoc.render_doc(TechIndicators.get_mom, "Help on %s"))
get_natr         = pydoc.plain(pydoc.render_doc(TechIndicators.get_natr, "Help on %s"))
get_obv          = pydoc.plain(pydoc.render_doc(TechIndicators.get_obv, "Help on %s"))
get_plus_di      = pydoc.plain(pydoc.render_doc(TechIndicators.get_plus_di, "Help on %s"))
get_plus_dm      = pydoc.plain(pydoc.render_doc(TechIndicators.get_plus_dm, "Help on %s"))
get_ppo          = pydoc.plain(pydoc.render_doc(TechIndicators.get_ppo, "Help on %s"))
get_roc          = pydoc.plain(pydoc.render_doc(TechIndicators.get_roc, "Help on %s"))
get_rocr         = pydoc.plain(pydoc.render_doc(TechIndicators.get_rocr, "Help on %s"))
get_rsi          = pydoc.plain(pydoc.render_doc(TechIndicators.get_rsi, "Help on %s"))
get_sar          = pydoc.plain(pydoc.render_doc(TechIndicators.get_sar, "Help on %s"))
get_sma          = pydoc.plain(pydoc.render_doc(TechIndicators.get_sma, "Help on %s"))
get_stoch        = pydoc.plain(pydoc.render_doc(TechIndicators.get_stoch, "Help on %s"))
get_stochf       = pydoc.plain(pydoc.render_doc(TechIndicators.get_stochf, "Help on %s"))
get_stochrsi     = pydoc.plain(pydoc.render_doc(TechIndicators.get_stochrsi, "Help on %s"))
get_t3           = pydoc.plain(pydoc.render_doc(TechIndicators.get_t3, "Help on %s"))
get_tema         = pydoc.plain(pydoc.render_doc(TechIndicators.get_tema, "Help on %s"))
get_trange       = pydoc.plain(pydoc.render_doc(TechIndicators.get_trange, "Help on %s"))
get_trima        = pydoc.plain(pydoc.render_doc(TechIndicators.get_trima, "Help on %s"))
get_trix         = pydoc.plain(pydoc.render_doc(TechIndicators.get_trix, "Help on %s"))
get_ultsoc       = pydoc.plain(pydoc.render_doc(TechIndicators.get_ultsoc, "Help on %s"))
get_willr        = pydoc.plain(pydoc.render_doc(TechIndicators.get_willr, "Help on %s"))
get_wma          = pydoc.plain(pydoc.render_doc(TechIndicators.get_wma, "Help on %s"))
map_to_matype    = pydoc.plain(pydoc.render_doc(TechIndicators.map_to_matype, "Help on %s"))
set_proxy        = pydoc.plain(pydoc.render_doc(TechIndicators.set_proxy, "Help on %s"))

indicators = ''
functions = [get_ad, get_adosc, get_adx, get_adxr, get_apo, get_aroon, get_aroonosc, get_atr, get_bbands, get_bop, get_cci, get_cmo, get_dema, get_dx, get_ema, get_ht_dcperiod, get_ht_dcphase, get_ht_phasor, get_ht_sine, get_ht_trendline, get_ht_trendmode, get_kama, get_macd, get_macdext, get_mama, get_mfi, get_midpoint, get_midprice, get_minus_di, get_minus_dm, get_mom, get_natr, get_obv, get_plus_di, get_plus_dm, get_ppo, get_roc, get_rocr, get_rsi, get_sar, get_sma, get_stoch, get_stochf, get_stochrsi, get_t3, get_tema, get_trange, get_trima, get_trix, get_ultsoc, get_willr, get_wma, map_to_matype, set_proxy]

for func in functions:
    indicators = indicators + func + '\n----------------------------------------------------------------------\n\n'

with open("Tech_Indicators.txt", "w") as tech_file:
   tech_file.write(indicators)

"""
SectorPerformances

"""
get_sector          = pydoc.plain(pydoc.render_doc(SectorPerformances.get_sector, "Help on %s"))
map_to_matype       = pydoc.plain(pydoc.render_doc(SectorPerformances.map_to_matype, "Help on %s"))
percentage_to_float = pydoc.plain(pydoc.render_doc(SectorPerformances.percentage_to_float, "Help on %s"))
set_proxy           = pydoc.plain(pydoc.render_doc(SectorPerformances.set_proxy, "Help on %s"))
sector = get_sector + '\n----------------------------------------------------------------------\n\n' + map_to_matype + '\n----------------------------------------------------------------------\n\n' + percentage_to_float + '\n----------------------------------------------------------------------\n\n' + set_proxy
with open("Sector_Performance.txt", "w") as tech_file:
   tech_file.write(sector)

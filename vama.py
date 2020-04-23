# volatility adjusted moving average

#commontimeframe.py
import pandas as pd
voldf = pd.read_csv('vcrix.csv',  usecols = [2, 3], parse_dates=['date'])
voldf['date'] = voldf['date'].dt.date
voldf = voldf.set_index('date')
import datetime
tA1 = voldf.reset_index().loc[0,'date']
tA2 = voldf.reset_index().loc[len(voldf)-1,'date']
prices = pd.read_csv('XBTUSD_past1000_days.csv')
prices = pd.read_csv('XBTUSD_past1000_days.csv', usecols = [0, 4], parse_dates=['timestamp'])
prices['date'] = prices['timestamp'].dt.date
prices = prices.set_index('date')
prices = prices.drop(['timestamp'], axis = 1)
prices = prices.iloc[::-1]
tB1 = prices.reset_index().loc[0,'date']
tB2 = prices.reset_index().loc[len(prices)-1,'date']
tC1 = 0; tC2 = 0; #initialise common time window
if tA1<tB1:
    tC1 = tB1
else:
    tC1 = tA1

if tA2<tB2:
    tC2 = tA2
else:
    tC2 = tB2

voldf = voldf[tC1:tC2]
prices = prices[tC1:tC2]
###################

vama = prices.ewm(span=vcrix*40/1000).mean() #???



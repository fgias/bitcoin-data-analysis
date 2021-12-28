# Find common time window.

import pandas as pd
import datetime


# Import vcrix data.
voldf = pd.read_csv('data/vcrix.csv',  usecols=[2, 3], parse_dates=['date'])
voldf['date'] = voldf['date'].dt.date
voldf = voldf.set_index('date')

tA1 = voldf.reset_index().loc[0, 'date']
tA2 = voldf.reset_index().loc[len(voldf) - 1, 'date']

# Same for XBTUSD price.
prices = pd.read_csv('data/XBTUSD_past1000_days.csv')
# If you want to use closing price only.
prices = pd.read_csv('data/XBTUSD_past1000_days.csv', usecols=[0, 4],
                     parse_dates=['timestamp'])
prices['date'] = prices['timestamp'].dt.date
prices = prices.set_index('date')
prices = prices.drop(['timestamp'], axis=1)
prices = prices.iloc[::-1]

tB1 = prices.reset_index().loc[0, 'date']
tB2 = prices.reset_index().loc[len(prices) - 1, 'date']

# Choose common overlap.
# Initialise common time window.
tC1 = 0
tC2 = 0

if tA1 < tB1:
    tC1 = tB1
else:
    tC1 = tA1

if tA2 < tB2:
    tC2 = tA2
else:
    tC2 = tB2

# Plot in same range.
voldf = voldf[tC1:tC2]
prices = prices[tC1:tC2]

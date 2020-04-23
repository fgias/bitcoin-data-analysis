# vcrix index

import pandas as pd
voldf = pd.read_csv('vcrix.csv',  usecols = [2, 3], parse_dates=['date'])
voldf = voldf.set_index('date')
import datetime

# voldf.loc[datetime.date(2014,11,28)]  # to comment whole section in sublime, select,  cmd+/
# voldf.loc[datetime.date(2020,3,7)]

prices = pd.read_csv('XBTUSD_past1000_days.csv')
# if you want to use closing price only
prices = pd.read_csv('XBTUSD_past1000_days.csv', usecols = [0, 4], parse_dates=['timestamp'])
prices['ts'] = prices['timestamp'].dt.date
prices = prices.set_index('ts')
prices = prices.drop(['timestamp'], axis = 1)

prices = prices.iloc[::-1]
voldf = voldf[datetime.date(2017,6,19):]
prices = prices[:datetime.date(2020,3,7)]

# define formatter
def Num_Format(x, pos): 
    # The two arguments are the number and tick position
    string = '{:,.0f}'.format(x)
    return string

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

formatter = FuncFormatter(Num_Format)

fig, ax1 = plt.subplots()

ax1.plot(prices, 'k', linewidth = .8)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

ax2.plot(voldf, linewidth = .8)


# fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

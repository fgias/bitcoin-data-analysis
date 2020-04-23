# vcrix index

import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


voldf = pd.read_csv('vcrix.csv',  usecols = [2, 3], parse_dates=['date'])
voldf['date'] = voldf['date'].dt.date
voldf = voldf.set_index('date')

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

formatter = FuncFormatter(Num_Format)

fig, axs = plt.subplots(2)
axs[0].grid(axis='both', linestyle='--', linewidth=.1)
axs[1].grid(axis='both', linestyle='--', linewidth=.1)
axs[0].plot(voldf)
axs[0].set_title('VCRIX')
axs[0].yaxis.set_major_formatter(formatter)
axs[1].plot(prices)
axs[1].set_title('XBTUSD price')
axs[1].yaxis.set_major_formatter(formatter)
plt.show()

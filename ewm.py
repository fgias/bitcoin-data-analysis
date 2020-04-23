# exponentially weighted moving average

import pandas as pd 
# pd.options.display.float_format = '{:,.2f}'.format
prices = pd.read_csv('XBTUSD_past1000_days.csv')
# if you want to use closing price only
prices = pd.read_csv('XBTUSD_past1000_days.csv', usecols = [0, 4], parse_dates=['timestamp'])
prices['ts'] = prices['timestamp'].dt.date
prices = prices.set_index('ts')
prices = prices.drop(['timestamp'], axis = 1)
import matplotlib.pyplot as plt # pyplot provides a MATLAB-like way of plotting.
#prices.plot()
#plt.ion()
#plt.title('XBTUSD')
#plt.xlabel('date'); plt.ylabel('price in USD');
#plt.show()

prices = prices.iloc[::-1]
ema20 = prices.ewm(span=20).mean()
ema80 = prices.ewm(span=80).mean()

def Num_Format(x, pos): 
    # The two arguments are the number and tick position
    string = '{:,.0f}'.format(x)
    return string

from matplotlib.ticker import FuncFormatter

formatter = FuncFormatter(Num_Format)

fig, axs = plt.subplots(1)

axs.plot(prices, 'k', linewidth=.3, label = 'XBTUSD')
axs.plot(ema20, 'b', linewidth=.7, label = 'EMA20d')
axs.plot(ema80, 'g', linewidth=.7, label = 'EMA80d')

#plt.plot(prices, 'k', linewidth=.3)
#plt.plot(ema20, 'b', linewidth=.7)
#plt.plot(ema80, 'g', linewidth=.7)
#plt.legend(['XBTUSD', 'EMA20d', 'EMA80d'])
axs.set_title('XBTUSD Price and EMAs')
axs.grid(axis='both', linestyle='--', linewidth=.1)
axs.yaxis.set_major_formatter(formatter)
axs.set(ylabel='USD')
axs.legend()

plt.show()

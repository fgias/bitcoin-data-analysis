# exponentially weighted moving average

import pandas as pd 
# pd.options.display.float_format = '{:,.2f}'.format
prices = pd.read_csv('data/XBTUSD_past1000_days.csv')
# if you want to use closing price only
prices = pd.read_csv('data/XBTUSD_past1000_days.csv', usecols = [0, 4], parse_dates=['timestamp'])
prices['ts'] = prices['timestamp'].dt.date
prices = prices.set_index('ts')
prices = prices.drop(['timestamp'], axis = 1)
import matplotlib.pyplot as plt # pyplot provides a MATLAB-like way of plotting.
#prices.plot()
#plt.ion()
#plt.title('XBTUSD')
#plt.xlabel('date'); plt.ylabel('price in USD');
#plt.show()
import datetime

prices = prices.iloc[::-1]
ema20 = prices.ewm(span=20).mean()
ema80 = prices.ewm(span=80).mean()

#############
emadiff = ema20 - ema80
#############

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

#############

i_range = list(range(1, len(emadiff)))
zeroes=[]
for i in i_range:
    if (emadiff.reset_index().loc[i, 'close'] < 0 and emadiff.reset_index().loc[i-1, 'close'] > 0) or (emadiff.reset_index().loc[i, 'close'] > 0 and emadiff.reset_index().loc[i-1, 'close'] < 0): 
        zeroes.append(i)

dates=[]       
for i in zeroes:
    dates.append(emadiff.reset_index().loc[i, 'ts'])

for j in range(len(dates)):
    print(dates[j])

############

for i in zeroes:
    axs.plot(emadiff.reset_index().loc[i, 'ts'], ema20.reset_index().loc[i, 'close'], 'kx')

axs.annotate('Long', xy=(emadiff.reset_index().loc[zeroes[7], 'ts'], ema20.reset_index().loc[zeroes[7], 'close']), xytext=(datetime.date(2019,1,1), 10000), arrowprops=dict(facecolor='green', shrink=0.05),)
axs.annotate('Short', xy=(emadiff.reset_index().loc[zeroes[2], 'ts'], ema20.reset_index().loc[zeroes[2], 'close']), xytext=(datetime.date(2018,8,25), 15000), arrowprops=dict(facecolor='red', shrink=0.05),)

plt.show()


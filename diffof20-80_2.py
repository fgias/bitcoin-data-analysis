# Gradient of EMA 20-80 #2

import pandas as pd 
import matplotlib.pyplot as plt # pyplot provides a MATLAB-like way of plotting.
from matplotlib.ticker import FuncFormatter

# Exponentially weighted moving average.
prices = pd.read_csv('XBTUSD_past1000_days.csv')
# if you want to use closing price only
prices = pd.read_csv('XBTUSD_past1000_days.csv', usecols = [0, 4], parse_dates=['timestamp'])
prices['ts'] = prices['timestamp'].dt.date
prices = prices.set_index('ts')
prices = prices.drop(['timestamp'], axis = 1)
# import matplotlib
#prices.plot()
#plt.ion()
#plt.title('XBTUSD')
#plt.xlabel('date'); plt.ylabel('price in USD');
#plt.show()

prices = prices.iloc[::-1]
ema20 = prices.ewm(span=20).mean()
ema80 = prices.ewm(span=80).mean()
diff = ema20-ema80

grad = diff.diff()
smoothgrad = grad.ewm(span=10).mean()

# define formatter
def Num_Format(x, pos): 
    # The two arguments are the number and tick position.
    string = '{:,.0f}'.format(x)
    return string


formatter = FuncFormatter(Num_Format)

fig, axs = plt.subplots(3)
axs[0].grid(axis='both', linestyle='--', linewidth=.1)
axs[1].grid(axis='both', linestyle='--', linewidth=.1)
axs[2].grid(axis='both', linestyle='--', linewidth=.1)

axs[0].plot(diff)
axs[0].set_title('EMA20d-EMA80d')
axs[0].yaxis.set_major_formatter(formatter)
axs[1].plot(grad)
axs[1].set_title('grad')
axs[1].yaxis.set_major_formatter(formatter)

axs[2].plot(smoothgrad)
axs[2].set_title('smooth grad')
axs[2].yaxis.set_major_formatter(formatter)


plt.show()

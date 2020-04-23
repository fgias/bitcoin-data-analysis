import pandas as pd 
pd.options.display.float_format = '{:,2f}'.format
prices = pd.read_csv('XBTUSD_past1000_days.csv')
# if you want to use closing price only
prices = pd.read_csv('XBTUSD_past1000_days.csv', usecols = [0, 4], parse_dates=['timestamp'])
prices['ts'] = prices['timestamp'].dt.date
prices = prices.set_index('ts')
prices = prices.drop(['timestamp'], axis = 1)
import matplotlib.pyplot as plt # pyplot provides a MATLAB-like way of plotting.
prices.plot()
plt.ion()
plt.title('XBTUSD')
plt.xlabel('date'); plt.ylabel('price in USD');
#plt.show()

stds = []
# list.append(elmnt)
# reverse order, rolling window in past
prices = prices.iloc[::-1]
stds.append(prices.rolling(150).std()) # 1 year volatility,# list.append(elmnt)
std_df = pd.concat(stds, axis = 1)
std_df = std_df.fillna(0)

fig, axs = plt.subplots(2)
axs[0].plot(std_df)
axs[0].set_title('Past 150d Price Stdev')
axs[1].plot(prices)
axs[1].set_title('XBTUSD Price')

plt.show()

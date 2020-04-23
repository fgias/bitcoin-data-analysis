# Find common time window.

import pandas as pd
import datetime


def find_common_window(df1, df2):
    # You can use pass here if you want the function to do nothing.
    t1_start = df1.index[0]
    t1_end = df1.index[-1]
    t2_start = df2.index[0]
    t2_end = df2.index[-1]
    # Choose common overlap.
    # Initialise common time window.
    tcom_start = 0
    tcom_end = 0
    # The tab here is not working, I get indentation error. Only 4 spaces are
    # working.
    if t1_start < t2_start:
        tcom_start = t2_start
    else:
        tcom_start = t1_start
    
    if t1_end < t2_end:
        tcom_end = t1_end
    else:
        tcom_end = t2_end
    
    return tcom_start, tcom_end

# Import vcrix data.
vol_df = pd.read_csv('vcrix.csv',  usecols=[2, 3], parse_dates=['date'])
vol_df['date'] = vol_df['date'].dt.date
vol_df = vol_df.set_index('date')

# Same for XBTUSD price.
price_df = pd.read_csv('XBTUSD_past1000_days.csv')
# If you want to use closing price only.
price_df = pd.read_csv('XBTUSD_past1000_days.csv', usecols=[0, 4],
                     parse_dates=['timestamp'])
price_df['date'] = price_df['timestamp'].dt.date
price_df = price_df.set_index('date')
price_df = price_df.drop(['timestamp'], axis=1)
price_df = price_df.iloc[::-1]

t1, t2 = find_common_window(vol_df, price_df)

# Plot in same range.
vol_df = vol_df[t1:t2]
price_df = price_df[t1:t2]

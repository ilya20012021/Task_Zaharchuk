import pandas as pd
from datetime import datetime
import numpy as np
df = pd.read_csv('traffic_security.csv',names=['timestamp','src','dst','port','bytes'])
df['timestamp'] = pd.to_datetime(df['timestamp'],unit='ms')
df['hour'] = pd.DatetimeIndex(df['timestamp']).hour
df_res = df.query('hour < 8 | hour > 17')
df_res = df_res.groupby(['src']).sum('bytes')
top_five = df_res.sort_values(by='bytes',ascending=False).head(5)
print(top_five['bytes']) 
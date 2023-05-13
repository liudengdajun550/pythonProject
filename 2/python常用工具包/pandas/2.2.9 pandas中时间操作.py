import pandas as pd

import datetime
#numpy中对于时间的操作
dt= datetime.datetime(year=1023,month=12,day=23,hour=20,minute=12)
print(dt)
#pandas中时间操作
ts = pd.Timestamp('2023-07-13')
print(ts)
print(ts.month)
print(ts.day)
print(ts+pd.Timedelta('5 days'))#直接增加几天
print(pd.to_datetime('2023-11-23'))
print(pd.to_datetime('2023/11/23'))
s = pd.Series(['2023-11-23','2023-11-23','2023-11-23'])
print(s)
print(pd.to_datetime(s))
print(s.dt.hour)





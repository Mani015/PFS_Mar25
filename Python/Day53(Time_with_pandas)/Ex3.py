# 3.Generate a date range using pandas

# 1. Create a date range by specifying the start and end dates with the default daily frequent.

from datetime import datetime
import pandas as pd

start_dt = datetime.strptime("2025-08-08","%Y-%m-%d")
end_dt = datetime.strptime("2025-08-15","%Y-%m-%d")
# D = "D" -> difference between each date. D means one day

date_list = pd.date_range(start_dt,end_dt,freq='D')

# print(date_list)
# DatetimeIndex(['2025-08-08', '2025-08-09', '2025-08-10', '2025-08-11',
#                '2025-08-12', '2025-08-13', '2025-08-14', '2025-08-15'],
#               dtype='datetime64[ns]', freq='D')

# If you want dates in string formate then convert it into string
print(date_list.strftime("%y-%m-%d"))


# Index(['25-08-08', '25-08-09', '25-08-10', '25-08-11', '25-08-12', '25-08-13',
#        '25-08-14', '25-08-15'],
#       dtype='object')


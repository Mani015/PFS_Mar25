# 2. Create a list of the next 10 days starting from the current date
# Here  we will use list comprehension

import datetime

num_of_dates = 10
start_dt = datetime.datetime.now()
# print(start_dt)

next_10_days = [start_dt.date() + datetime.timedelta(days=i) for i in range(num_of_dates)]
# print(next_10_days)
# [datetime.date(2025, 8, 8), datetime.date(2025, 8, 9), datetime.date(2025, 8, 10), datetime.date(2025, 8, 11), datetime.date(2025, 8, 12), datetime.date(2025, 8, 13), datetime.date(2025, 8, 14), datetime.date(2025, 8, 15), datetime.date(2025, 8, 16), datetime.date(2025, 8, 17)]


# 2. Create a list of the past 10 days starting from the current date
# Here  we will use list comprehension
print()
num_of_dates = 10
current_dt = datetime.datetime.now()

past_10_days = [current_dt.date() - datetime.timedelta(days = k) for k in range(num_of_dates)]
print(past_10_days)

# [datetime.date(2025, 8, 8), datetime.date(2025, 8, 7), datetime.date(2025, 8, 6), datetime.date(2025, 8, 5), datetime.date(2025, 8, 4), datetime.date(2025, 8, 3), datetime.date(2025, 8, 2), datetime.date(2025, 8, 1), datetime.date(2025, 7, 31), datetime.date(2025, 7, 30)]

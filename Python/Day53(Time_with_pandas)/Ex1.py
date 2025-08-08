# 1.Create a list of dates with in a range of data

# We specify two dates and creates a list with all the dates in between them.

from datetime import date, timedelta

start_dt = date(2025,8,8)
end_dt = date(2025,8,15)
current_date = start_dt
delta = timedelta(days=1)

dates_list = []

while start_dt < end_dt:
    dates_list.append(start_dt.isoformat())
    start_dt += delta

print(f"difference between start_date : {current_date} and  end_date : {end_dt}")
print(f"between days : {dates_list}")
# difference between start_date : 2025-08-08 and  end_date : 2025-08-15
# between days : ['2025-08-08', '2025-08-09', '2025-08-10', '2025-08-11', '2025-08-12', '2025-08-13', '2025-08-14']

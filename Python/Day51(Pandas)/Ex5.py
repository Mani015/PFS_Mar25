import pandas as pd

# Two-dimensional, size-mutable, potentially heterogeneous tabular data.
# DataFrame([data, index, columns, dtype, copy])

Stu_info = {
    'Names' : ['Dorababu','nani','saikumar','venu','shabber','firoz','mahammad','pawan','dathri'],
    'Ages'  : [21,22,23,24,25,26,27,28,29],
    'Country' : ['India','swizerland','USA','london','japan','pakistan','UAE','rassia','australia'],
    'salary' : [1000,2000,3000,4000,5000,6000,7000,8000,9000]
}


df1 = pd.DataFrame(Stu_info)
# print(df1)
#       Names  Ages     Country  salary
# 0  Dorababu    21       India    1000
# 1      nani    22  swizerland    2000
# 2  saikumar    23         USA    3000
# 3      venu    24      london    4000
# 4   shabber    25       japan    5000
# 5     firoz    26    pakistan    6000
# 6  mahammad    27         UAE    7000
# 7     pawan    28      rassia    8000
# 8    dathri    29   australia    9000

# print('dimesions : ',df1.ndim)
# dimesions :  2

# See all colums
# print(df1.columns)
# Index(['Names', 'Ages', 'Country', 'salary'], dtype='object')

# See all values
# print(df1.values)
# [['Dorababu' 21 'India' 1000]
#  ['nani' 22 'swizerland' 2000]
#  ['saikumar' 23 'USA' 3000]
#  ['venu' 24 'london' 4000]
#  ['shabber' 25 'japan' 5000]
#  ['firoz' 26 'pakistan' 6000]
#  ['mahammad' 27 'UAE' 7000]
#  ['pawan' 28 'rassia' 8000]
#  ['dathri' 29 'australia' 9000]]


# print(df1.index)
# RangeIndex(start=0, stop=9, step=1)

# head returns first 5 rows
# print(df1.head(2))
#       Names  Ages     Country  salary
# 0  Dorababu    21       India    1000
# 1      nani    22  swizerland    2000
# 2  saikumar    23         USA    3000
# 3      venu    24      london    4000
# 4   shabber    25       japan    5000


# last 5 rows
print(df1.tail())

#       Names  Ages    Country  salary
# 4   shabber    25      japan    5000
# 5     firoz    26   pakistan    6000
# 6  mahammad    27        UAE    7000
# 7     pawan    28     rassia    8000
# 8    dathri    29  australia    9000




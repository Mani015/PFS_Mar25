
# Pandas : Pandas is a fast,powerful, flexible and easily to use opensource data analysis
# and manipulation tools, builts on top of the python programming language.

# There are two types
# 1.Series
# 2.DataFrames

# Seires is a 1-Dimensional array defined in pandas that can be used to store any data type
# 1). A series is a very similar to numpy array (i fact it is built on top of the Numpy array object)
# 2).What is difference the  Numpy arrays from a series.

import numpy as np

n1 = np.array([11,22,33,44,55])
# print(n1[0])

# is the series can have axis labels [meaning it can be indexed by a label insted of just number  location]
# it doesn't need to hold numeric

# Numpy to Series

import pandas as pd
# print(help(pd.Series))
# Series(data=None, index=None, dtype: 'Dtype | None' = None, name=None, copy: 'bool | None' = None, fastpath: 'bool' = False) -> 'None'


s1 = pd.Series(data=n1)

print(s1)
# 0    11
# 1    22
# 2    33
# 3    44
# 4    55
# dtype: int32

# print(type(s1))
# <class 'pandas.core.series.Series'>

print()
print('Changed indexing numbers :')

Names = ['Dorababu','narasimha','dathri','sai','venu']

s2 = pd.Series(data=n1,index=Names)
print(s2)
# Changed indexing numbers :
# Dorababu     11
# narasimha    22
# dathri       33
# sai          44
# venu         55

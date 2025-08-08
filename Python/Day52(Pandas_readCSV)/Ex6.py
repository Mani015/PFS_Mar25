
d1 = {
    'A' : [1,2,3],
    'B' : [4,5,6],
    'C' : [7,8,9]
}

import pandas as pd

df1 = pd.DataFrame(d1)
print(df1)
print()

# apply() : Apply function on Multiple series using in Dataframe
def Sum_series(data1,data2):

    return  data1 + data2


sum1 = df1.apply(lambda row : Sum_series(row['A'],row['B']),axis=1)
print(sum1)

#    A  B  C
# 0  1  4  7
# 1  2  5  8
# 2  3  6  9
#
# 0    5
# 1    7
# 2    9



import pandas as pd
import numpy as np
Emp_dict = {
    'Names' : ['charan','madhuri','yogeswar','pasand','suresh','sonia','bhanu','charan'],
    'Ages' : [20,21,19,22,24,21,20,20],
    'Marks' : [np.nan,34000,45000,20000,50000,60000,np.nan,25000],
    'Location' : ['chennai','Bengaluru','pune','kadapa','nellore',np.nan,'tirupathi','vijayawada']
}

emp_df = pd.DataFrame(Emp_dict)

# Drop column where at least one value is missing:
# There is a case when we cannot process the dataset with missing value.
# If we need to drop such columns that condtions NA,
# sy : dataframe.dropna(axis= " columns")
# print(emp_df.dropna(axis='columns'))

#       Names  Ages
# 0    charan    20
# 1   madhuri    21
# 2  yogeswar    19
# 3    pasand    22
# 4    suresh    24
# 5     sonia    21
# 6     bhanu    20
# 7    charan    20


# Drop column where the all values are missing

stu = {
    'Name' : ['bablu','Joy','Rema','Ron','Melody'],
    'Ages' : [np.nan,np.nan,np.nan,np.nan,np.nan]
}
d1 = pd.DataFrame(stu)
# print(d1)
# We can drop an empty column from Dataframe using Dataframe.dropna()
# we need to use how parameters as follows.

# -> If how = "all" it drops the column where all the values are NA.
# -> By default, how  = "any", it removes the column where one or more values are NA.

# Ex : "Ages" column where all values are NaN.

# sy : Dataframe.dropna(axis = 'column', how = "all")

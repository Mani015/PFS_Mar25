import pandas as pd

# Merge two DataFrames based on condition.


stu_info = {
    'Name' : ['Bilal','jasmin','bharath','kalyan','jyothsna','jayanthi'],
    'Ages' : [10,12,13,14,15,16],
    "Marks" : [99,100,101,100,98,97],
    'Location' : ['Dubai','Canada','India','French','Germany','Netherlands']
}


grade_marks = {
    'Marks' : [99,100,101,100,98,97]
    ,'Grade' : ['A1','A1','A1','A1','A1','A1']
}


# Create dataframe1 :


df1 = pd.DataFrame(stu_info)
df2 = pd.DataFrame(grade_marks)

# print(df1)
# print()
# print(df2)


New_df = pd.merge(df1,df2,on='Marks')
print(New_df)

#        Name  Ages  Marks     Location Grade
# 0     Bilal    10     99        Dubai    A1
# 1    jasmin    12    100       Canada    A1
# 2    jasmin    12    100       Canada    A1
# 3    kalyan    14    100       French    A1
# 4    kalyan    14    100       French    A1
# 5   bharath    13    101        India    A1
# 6  jyothsna    15     98      Germany    A1
# 7  jayanthi    16     97  Netherlands    A1




import pandas as pd

Stu_info = {
    'Names' : ['Dorababu','nani','saikumar','venu','shabber','firoz','mahammad','pawan','dathri'],
    'Ages'  : [21,22,23,24,25,26,27,28,29],
    'Country' : ['India','swizerland','USA','london','japan','pakistan','UAE','rassia','australia'],
    'salary' : [1000,2000,3000,4000,5000,6000,7000,8000,9000]
}

df2 = pd.DataFrame(Stu_info)



# df2.loc[rows,colums]
# print(df2.loc[1:5])
#      Names  Ages     Country  salary
# 1      nani    22  swizerland    2000
# 2  saikumar    23         USA    3000
# 3      venu    24      london    4000
# 4   shabber    25       japan    5000
# 5     firoz    26    pakistan    6000



# print(df2.loc[1:5,['Names','Ages']])
#       Names  Ages
# 1      nani    22
# 2  saikumar    23
# 3      venu    24
# 4   shabber    25
# 5     firoz    26

# iloc : interger location

# print(df2[])


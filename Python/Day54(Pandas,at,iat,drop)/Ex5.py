
# Drop duplicate value but keep first
# When we have the dataframe with many duplicate rows that want to remove we use Dataframe.drop_duplicate()

# Drop duplicate rows

import pandas as pd
Emp_dict = {
    'Names' : ['charan','madhuri','yogeswar','pasand','suresh','sonia','bhanu','charan'],
    'Ages' : [20,21,19,22,24,21,20,20],
    'Salary' : [10000,34000,45000,20000,50000,60000,39000,25000],
    'Location' : ['chennai','Bengaluru','pune','kadapa','nellore','kurnool','tirupathi','vijayawada']
}

emp_df = pd.DataFrame(Emp_dict)
print(emp_df)
# Before drop the Dataframe
#       Names  Ages  Salary    Location
# 0    charan    20   10000     chennai
# 1   madhuri    21   34000   Bengaluru
# 2  yogeswar    19   45000        pune
# 3    pasand    22   20000      kadapa
# 4    suresh    24   50000     nellore
# 5     sonia    21   60000     kurnool
# 6     bhanu    20   39000   tirupathi
# 7    charan    20   25000  vijayawada

print()

# print(help(pd.DataFrame.drop_duplicates))

emp_df.drop_duplicates(subset=['Names','Ages'],inplace=True)
print(emp_df)
#      Names  Ages  Salary   Location
# 0    charan    20   10000    chennai
# 1   madhuri    21   34000  Bengaluru
# 2  yogeswar    19   45000       pune
# 3    pasand    22   20000     kadapa
# 4    suresh    24   50000    nellore
# 5     sonia    21   60000    kurnool
# 6     bhanu    20   39000  tirupathi


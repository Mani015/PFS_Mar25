

import pandas as pd
Emp_dict = {
    'Names' : ['Simhadri','madhuri','yogeswar','pasand','suresh','sonia','bhanu','charan'],
    'Ages' : [20,21,19,22,24,21,20,23],
    'Salary' : [10000,34000,45000,20000,50000,60000,39000,25000],
    'Location' : ['chennai','Bengaluru','pune','kadapa','nellore','kurnool','tirupathi','vijayawada']
}

# convert python dict to DataFrame

emp_df = pd.DataFrame(Emp_dict)
# print(emp_df)

#       Names  Ages  Salary    Location
# 0  Simhadri    20   10000     chennai
# 1   madhuri    21   34000   Bengaluru
# 2  yogeswar    19   45000        pune
# 3    pasand    22   20000      kadapa
# 4    suresh    24   50000     nellore
# 5     sonia    21   60000     kurnool
# 6     bhanu    20   39000   tirupathi
# 7    charan    23   25000  vijayawada



# at :
# select value using row and column  using Dataframe.at
# we need to access a speicfic value of the dataframe using its column label and row index.
# We can use the DataFrame.at property pass the row index and column label of the value access parameters

# syntax : dataframe.at[row, index]
v1 = emp_df.at[2,'Salary']
# print(v1) # 45000

# Change the value of a specific column

emp_df.at[5,'Location'] = "Hyderabad"

print(emp_df)

#       Names  Ages  Salary    Location
# 0  Simhadri    20   10000     chennai
# 1   madhuri    21   34000   Bengaluru
# 2  yogeswar    19   45000        pune
# 3    pasand    22   20000      kadapa
# 4    suresh    24   50000     nellore
# 5     sonia    21   60000   Hyderabad
# 6     bhanu    20   39000   tirupathi
# 7    charan    23   25000  vijayawada

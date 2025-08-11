
import pandas as pd
Emp_dict = {
    'Names' : ['Simhadri','madhuri','yogeswar','pasand','suresh','sonia','bhanu','charan'],
    'Ages' : [20,21,19,22,24,21,20,23],
    'Salary' : [10000,34000,45000,20000,50000,60000,39000,25000],
    'Location' : ['chennai','Bengaluru','pune','kadapa','nellore','kurnool','tirupathi','vijayawada']
}


emp_df = pd.DataFrame(Emp_dict)

# Drop columns & rows
# We can use the pandas function we can remove  the column or rows for Dataframe.drop(labels = None,axis= 1)

# emp_df.drop(columns=['Location'],inplace=True)
print()
# print(emp_df)
#       Names  Ages  Salary
# 0  Simhadri    20   10000
# 1   madhuri    21   34000
# 2  yogeswar    19   45000
# 3    pasand    22   20000
# 4    suresh    24   50000
# 5     sonia    21   60000
# 6     bhanu    20   39000
# 7    charan    23   25000


# Drop 2 columns at a time
emp_df.drop(columns=['Ages','Names'],inplace=True)
print(emp_df)

#   Salary    Location
# 0   10000     chennai
# 1   34000   Bengaluru
# 2   45000        pune
# 3   20000      kadapa
# 4   50000     nellore
# 5   60000     kurnool
# 6   39000   tirupathi
# 7   25000  vijayawada



# iat : Select value row and column position using DF.iat
# we want to access a specific element from a very large dataframe, but we don't know its column label or row index.'
# we can still access such an element using column and row positions for that, we can use Dataframe.iat property of python pandas.
# unlike Dataframe.at

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

value = emp_df.iat[1,2]
# print(value)
# 34000


value2 = emp_df.iat[6,3]
# print(value2)
# tirupathi



# SET SPECIFIC VALUE IN PANDADATAFRAMES
# when we want to update the value of the paritcular element from dataframe based on its coliumn and row positions. we can use Dataframe.iat

emp_df.iat[4,2] = 55000
print(emp_df)

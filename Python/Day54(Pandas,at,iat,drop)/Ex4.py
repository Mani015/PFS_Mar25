
import pandas as pd
Emp_dict = {
    'Names' : ['Simhadri','madhuri','yogeswar','pasand','suresh','sonia','bhanu','charan'],
    'Ages' : [20,21,19,22,24,21,20,23],
    'Salary' : [10000,34000,45000,20000,50000,60000,39000,25000],
    'Location' : ['chennai','Bengaluru','pune','kadapa','nellore','kurnool','tirupathi','vijayawada']
}


#using drop with  axis = 1 or axis = "columns"
emp_df = pd.DataFrame(Emp_dict)
# emp_df.drop(['Ages','Location'],axis="columns",inplace=True)
# print(emp_df)




# emp_df = pd.DataFrame(Emp_dict)
# emp_df.drop(['Ages','Location'],axis=1,inplace=True)
# print(emp_df)


# Drop range of columns using iloc :
# There could be a case when we need to delete the fourth column from the database or Dataframe need to delete a range of columns
# we can use Dataframe.iloc to select single or multiple columns from the DataFrame.

# We can use DataFrame.iloc in the column parameter to specifiy the index position of the column which need to drop

# sy : dataframe.drop(columns = dataframe.iloc[rows, columns])


# emp_df.drop(columns=emp_df.iloc[:,0:1],inplace=True)
# print(emp_df)
#    Ages  Salary    Location
# 0    20   10000     chennai
# 1    21   34000   Bengaluru
# 2    19   45000        pune
# 3    22   20000      kadapa
# 4    24   50000     nellore
# 5    21   60000     kurnool
# 6    20   39000   tirupathi
# 7    23   25000  vijayawada



# emp_df.drop(columns=emp_df.iloc[:,0:2],inplace=True)
# print(emp_df)



# Drop first N columns : If we need to delete the First 'N' columns  from a dataframe, we can use Dataframe.iloc
# and the python range()
emp_df.drop(columns=emp_df.iloc[:,range(3)],inplace=True)
print(emp_df)

#      Location
# 0     chennai
# 1   Bengaluru
# 2        pune
# 3      kadapa
# 4     nellore
# 5     kurnool
# 6   tirupathi
# 7  vijayawada


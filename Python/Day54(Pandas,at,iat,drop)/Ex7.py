
# --> Drop column with the number of NA :  We need to use the parameter thresh = no_of_nonNA_values of
# Dataframe.drop() to specifiy the number of values, else drop column
import pandas as pd
import numpy as np

stu = {
    'Name' : ['bablu','Joy','Rema','Ron','Melody'],
    'Ages' : [np.nan,np.nan,np.nan,np.nan,np.nan]
}
d1 = pd.DataFrame(stu)


d1.dropna(axis=1,thresh=1,inplace=True)
# print(d1)
#      Name
# 0   bablu
# 1     Joy
# 2    Rema
# 3     Ron
# 4  Melody


# --> Drop NA from defined rows : suppose we are intersted in droping the column only if it contains null
# values in some particular rows. we can use subset = [row1,row2]

# sy : dataframe.dropna(axis=1,subset = [0,2])
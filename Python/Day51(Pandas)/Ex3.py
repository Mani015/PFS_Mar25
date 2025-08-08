# Attributes :

import pandas as pd
stu_info = {
    'Name' : 'Pawankalayan',
    'Age' : 20,
    'location' : 'Bangalore',
    'Phone' : 9843532322
}

s3 = pd.Series(stu_info)

# print(s3.values)
# ['Pawankalayan' 20 'Bangalore' 9843532322]

# for i in s3.values:
#     print(i)

# Pawankalayan
# 20
# Bangalore
# 9843532322

# print(s3.ndim) # 1

# print(s3.info)
# <bound method Series.info of Name        Pawankalayan
# Age                   20
# location       Bangalore
# Phone         9843532322
# dtype: object>


print(s3.dtype)
# object

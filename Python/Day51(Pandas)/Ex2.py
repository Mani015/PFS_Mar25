
# A dictionary to Series
import pandas as pd
stu_info = {
    'Name' : 'Pawankalayan',
    'Age' : 20,
    'location' : 'Bangalore',
    'Phone' : 9843532322
}


s2 = pd.Series(data=stu_info)
# print(s2)
# Name        Pawankalayan
# Age                   20
# location       Bangalore
# Phone         9843532322

print(s2['Name'])
print(s2['Age'])
# Pawankalayan
# 20


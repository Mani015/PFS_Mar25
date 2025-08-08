
# Rename column names

# Columns : ['Product ID' 'Product' 'Category' 'Size' 'Cost per Box']

import pandas as pd

df_pro = pd.read_csv('products.csv')
# print(df_pro)

# df_pro.rename(
#     columns= {'Product ID' : 'pro_ID'}
# )
#
# print(df_pro.columns.values)
# ['Product ID' 'Product' 'Category' 'Size' 'Cost per Box']




df_pro.rename(
    columns= {'Product ID' : 'pro_ID'},
    inplace=True
)

print(df_pro.columns.values)
# ['pro_ID' 'Product' 'Category' 'Size' 'Cost per Box']

# https://pandas.pydata.org/docs/reference/frame.html

# Read CSV files

import pandas as pd

df1 = pd.read_csv('products.csv')
# print(df1)

# Extract column

# print(df1.columns)
# Index(['Product ID', 'Product', 'Category', 'Size', 'Cost per Box'], dtype='object')
print(f'Columns : {df1.columns.values}')
# Columns : ['Product ID' 'Product' 'Category' 'Size' 'Cost per Box']



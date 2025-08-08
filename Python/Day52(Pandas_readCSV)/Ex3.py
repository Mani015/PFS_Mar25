
# Rename Multiple column names

import pandas as pd

df2 = pd.read_csv('products.csv')
# ['Product ID' 'Product' 'Category' 'Size' 'Cost per Box']
print(df2.columns)
quit()

df2.rename(
    columns= {
        'Product' : 'Item',
        'Category' : 'Purpose',
        'Size' : 'Shape'

    },
    inplace=True
)

print(df2)

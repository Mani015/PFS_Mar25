# Apply some conditions

# Sales Person,Geo,Product,Date,Amount,Boxes

# Excute Amount > 5000
import pandas as pd

sales_df = pd.read_csv('sales-data-new.csv')
# print(sales_df)

# Apply single condition
# x = pd.DataFrame(sales_df['Amount'] > 5000)
# print(x.head(10))


# Apply multiple condition
# Excute Boxes greater 500 ans Amount > 5000

y = pd.DataFrame([(sales_df['Boxes'] != 500) | (sales_df['Amount'] > 5000)])
print(y)








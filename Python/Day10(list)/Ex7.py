# insert : insert a new value at the specified index 
# syntax : list.insert(index, value)

names = ['suresh','vamsi','chaithanya','balu','venkat']
print(names)

names.insert(1,'bablu')

print(names)
# ['suresh', 'bablu', 'vamsi', 'chaithanya', 'balu', 'venkat']


names.insert(-1,'charan')
print(names)
# ['suresh', 'bablu', 'vamsi', 'chaithanya', 'balu', 'charan', 'venkat']


print()
# replacing values

mobiles = ['vivo','realme','mi','samsung','nothing','iphone']

mobiles[2] = 'xiaomi'
print(mobiles)
# ['vivo', 'realme', 'xiaomi', 'samsung', 'nothing', 'iphone']



# The count() method returns the number of times a specified value appears in the string.
s1 = "The revenant"
# syn : string.count(value)

print('e repeats : ', s1.count('e'))
# e repeats :  3

# Count a specified character after the 3 index 

# syt : str.count(value,start,stop)

print('e repeats : ', s1.count('e',4))
# e repeats :  2

print('packaged drinking water'.count('a',5,10))
# 0

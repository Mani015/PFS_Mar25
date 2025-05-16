
# The filter() Function
# Similar to map(), filter() takes a function object and an iterable and creates a new list.
#
# As the name suggests, filter() forms a new list that contains only elements that satisfy a certain condition, i.e. the function we passed returns True.
#
# The syntax is:
#
# filter(function, iterable(s))



num = [2,3,4,5,6,7,9,5,2,4,6,8,12,45,36,78,90,22,24,26]

def Finding(num):

    return num % 2 == 0


even = list(filter(Finding,num))
# print(even)
# [2, 4, 6, 2, 4, 6, 8, 12, 36, 78, 90, 22, 24, 26]


print(tuple(filter(lambda x : x%2 == 0 , num)))
# (2, 4, 6, 2, 4, 6, 8, 12, 36, 78, 90, 22, 24, 26)




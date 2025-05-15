
# The map(), filter() and reduce() functions bring a bit of functional programming to Python.
#  All three of these are convenience functions that can be replaced with List Comprehensions or loops,
# but provide a more elegant and short-hand approach to some problems.
#
# The map() Function
# The map() function iterates through all items in the given iterable and executes the function we passed as an argument on each of them.
#
# The syntax is:
#
# map(function, iterable(s))



num1 = [2,3,4,5,6,7,8,9,10]


def Onebyone(x):

    return x ** 2

v1 = map(Onebyone,num1)
# print(v1)
# <map object at 0x0000015B5A663BB0>
# print(list(v1))
# [4, 9, 16, 25, 36, 49, 64, 81, 100]



# write down single line

print(tuple(map(lambda x : x ** 2,range(1,11))))

Names= ['Senorita','Darla','ron','chion','philip']




# map with filter

x = [4,6,3,87,9,6,2,-10,3,-5,-20,12,-56,-23,11,22,56,89]

# Do a square to all numbers ,
# next, excute which are divisible by 5


def Square(num):

    return num ** 2

# double = list(map(Square,x))
# print(double)
# [16, 36, 9, 7569, 81, 36, 4, 100, 9, 25, 400, 144, 3136, 529, 121, 484, 3136, 7921]


def divisible_by_5(var) :

    return var % 5 == 0

# divisible_5 = tuple(filter(divisible_by_5,double))
# print(divisible_5)


divisible_5 = tuple(filter(divisible_by_5,list(map(Square,x))))
# print(divisible_5)

# print(list(map(lambda x : x ** 2, x)))


print(list(filter(lambda y : y % 5 == 0, list(map(lambda x : x ** 2, x)))))
# [100, 25, 400]




from functools import reduce

print(reduce(lambda x,y : x / y, range(1,11)))

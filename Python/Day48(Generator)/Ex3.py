
def Calling():

    yield 10
    yield 20
    yield 30
    yield 40
    yield 50


ob1 = Calling()
# print(next(ob1))
# print(next(ob1))
# print(next(ob1))
# print(next(ob1))
# print(next(ob1))
# print(next(ob1)) StopIteration


# print(type((i for i in range(1,11))))

# print((i for i in range(1,11)))
# <generator object <genexpr> at 0x0000017F743887B0>

v1 = (i for i in range(1,11))
print(next(v1)) # 1
print(next(v1)) # 2


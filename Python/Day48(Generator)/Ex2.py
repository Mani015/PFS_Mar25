
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
# 10
# 20
# 30

print(ob1.__next__())
print(ob1.__next__())
print(ob1.__next__())
print(ob1.__next__())
print(ob1.__next__())
# 10
# 20
# 30
# 40
# 50
print(ob1.__next__())
# StopIteration
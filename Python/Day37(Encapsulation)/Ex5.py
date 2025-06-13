

# Name Mangling :
# At least two leading underscore before the variable name like  (__variable)
# At most one trailing underscore After the Variable name like (variable_)
#                         __variable_
# If the object has a method named __dir__(), this method will be called and must return the list of attributes.
# syntax : obj._classname__variablename_



class A:

    name = "surehs"
    age_ = 12
    __Salary = 23456
    ____location_ = "Bangalore"
    ___Country____ = "India"
    ________________phonenum = 9848012034

    def _Method1(self):
        pass

    def __Method2_(self):
        pass


ob1 = A()
# print(ob1.__Salary) AttributeError: 'A' object has no attribute '__Salary'
# print(dir(ob1))

print(ob1._A__Salary)
# 23456



# for mangling in dir(ob1):
#     print(mangling)



# _A__Method2_
# _A__Salary
# _A________________phonenum
# _A____location_
# _Method1
# ___Country____
# __class__
# __delattr__
# __dict__
# __dir__
# __doc__
# __eq__
# __format__
# __ge__
# __getattribute__
# __gt__
# __hash__
# __init__
# __init_subclass__
# __le__
# __lt__
# __module__
# __ne__
# __new__
# __reduce__
# __reduce_ex__
# __repr__
# __setattr__
# __sizeof__
# __str__
# __subclasshook__
# __weakref__
# age_
# name
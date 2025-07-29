
# Create Python Generator
# In Python, similar to defining a normal function, we can define a generator function using the def keyword,
# but instead of the return statement we use the yield statement.

# def generator_name(arg):
#     # statements
#     yield something


# When the generator function is called, it does not execute the function body immediately. Instead,
# it returns a generator object that can be iterated over to produce the values.



def my_function():

    return "Hello function"

# my_function()
# ob1 = my_function
# print(type(ob1))
# <class 'function'>



def Sequence():

    yield 10

# ob2 = Sequence()
# print(type(ob2))
# <class 'generator'>



def Calling():

    yield 10
    yield 20
    yield 30
    yield 40
    yield 50

# print(Calling()) #<generator object Calling at 0x000002DB807D8E40>

Num = Calling()

for i in Num:
    print(i)

# 10
# 20
# 30
# 40
# 50



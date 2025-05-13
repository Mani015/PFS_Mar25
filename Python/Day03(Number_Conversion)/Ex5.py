
# 2. Explicit casting: The explicit type conversion is performed by the user using built-in functions.

# int(): convert any type variable to the integer type.
# float(): convert any type variable to the float type.
# complex(): convert any type variable to the complex type.
# bool(): convert any type variable to the bool type.
# str(): convert any type variable to the string type.


x  : str = '12'
# convert str to int
# syntax : int(object)

y = int(x)
# print(y)
# print(type(y))
# 12
# <class 'int'>

# float to int
f1 : float = 2.45

f2 = int(f1)
print(f2)
print(type(f2))
# 2
# <class 'int'>

"""
Int type conversion
Casting float value to an integer
Casting Boolean value to an integer
Casting a string to an integer

Float type conversion
Casting integer to float
Casting Boolean to float
Casting string to float

Complex type conversion
Casting integer type to complex type
Casting float type to complex type
Casting Boolean type to complex type

Bool type conversion
Casting integer to Boolean type
Casting float to Boolean type
Casting string to Boolean type
Casting complex type to Boolean type

String type conversion
Casting int to str type
Casting float type to str type
Casting complex type to str  type
Casting bool type to str type
"""

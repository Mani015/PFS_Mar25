
# In Python, we can convert one type of variable to another type.
# This conversion is called type casting or type conversion.

# In casting, we convert variables declared in specific data types to the different data types.

# Python performs the following two types of casting.
# 1.Implict conversion
# 2.Explict conversion


# 1. Python avoids data loss by converting lower data types to higher data types.
#  For example, an integer 7, is converted to a float when added with another float, 2.2

v1  : int = 4
v2  : float = 3.4

result = v1 + v2
print(result)

print(type(result))
# 7.4
# <class 'float'>



v3 : float = 12.3
v4 : complex  = 2 + 4j

output = v3 + v4
print(output)
# print(type(output))
# (14.3+4j)
# <class 'complex'>



print()
com = output
# Extact only real value 
# sy : obj.real
# the real part of a complex number
# print(com.real)14.3

# the imaginary part of a complex number

print(com.imag)
# 4.0



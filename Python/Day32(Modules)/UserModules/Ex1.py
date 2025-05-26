
# In Python, modules refer to the Python file, which contains Python code like Python statements, classes, functions, variables, etc.
#  A file with Python code is defined with extension.py
#
#
#
# In Python, large code is divided into small modules. The benefit of modules is, it provides a way to share reusable functions.
# 1.providing flexibility to organize the code in a logic way
# 2.Enables reusability of code
# 3.Helps in debugging code easily
#
# Types of modules
# In Python, there are two types of modules.
#
# Built-in Modules
# User-defined Modules

# Built-in modules
# Built-in modules come with default Python installation. One of Python’s most significant advantages is its rich library support that contains lots of built-in modules. Hence, it provides a lot of reusable code.
#
# Some commonly used Python built-in modules are datetime, os, math, sys, random, etc.
#
#
# User-defined modules
# The modules which the user defines or create are called a user-defined module.
#  We can create our own module, which contains classes, functions, variables, etc., as per our requirements.




def Check_Palindrom(Name : str) -> bool:

    Result = 0
    if Name == Name[::-1]:

        Result = True

    else:

        Result = False

    return Result



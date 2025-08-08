# Recursion
# Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept.
# It means that a function calls itself.
# This has the benefit of meaning that you can loop through data to reach a result.

# The error RecursionError: maximum recursion depth exceeded while calling a Python object occurs in Python
# when a function calls itself too many times without stopping — this is known as infinite recursion or exceeding the recursion limit.


# reason for display upto 996---the main problem is stack overflow and the memory utiliztion
# -------------------------------------------------------------------------------------------------
#  the maximum recursion depth that Python can handle depends on the available memory
# and the size of the call stack. In some cases, the recursion limit of 1000 may be
# reached before the call stack is full, resulting in a stack overflow error.
# [the recursion would continue indefinitely, leading to a stack overflow.]
#
# In your specific case, the recursion limit of 1000 was reached before the call stack
# was completely filled, allowing Python to display up to 966 iterations. The exact
# number of iterations that can be displayed may vary depending on the factors mentioned above.
# should know the interpreter capacity
import sys

# print('Interpreter capacity : ', sys.getrecursionlimit())
# Interpreter capacity :  1000

# set recursion limit
sys.setrecursionlimit(200)
def fun1():

    print("hello")
    fun1()

fun1()
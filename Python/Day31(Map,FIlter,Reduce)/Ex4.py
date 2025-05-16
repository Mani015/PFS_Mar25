# The reduce() Function
# reduce() works differently than map() and filter(). It does not return a new list based on the function and iterable we've passed. Instead, it returns a single value.
#
# Also, in Python 3 reduce() isn't a built-in function anymore, and it can be found in the functools module.
#
# The syntax is:
#
# reduce(function, sequence[, initial])
# reduce() works by calling the function we passed for the first two items in the sequence. The result returned by the function is used in another call to function alongside with the next (third in this case), element.
#
# This process repeats until we've gone through all the elements in the sequence.

x = [4,6,3,87,9,6,2,10,3,5,20,12,56,23,11,22,56,89]







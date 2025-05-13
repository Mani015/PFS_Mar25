
# Variable-length arguments
#   1.Arbitrary positional arguments (*args)
#   2.Arbitrary keyword arguments (**kwargs)


# # Variable-length arguments:
# In Python, sometimes, there is a situation where we need to pass multiple arguments to the function.
# Such types of arguments are called arbitrary arguments or variable-length arguments.
#
# We use variable-length arguments if we don’t know the number of arguments needed for the function in advance.


def natural_num(*num1):
	print(num1)   # it returns in tuple.


# natural_num(1,2,3,4)



def Sum_of_Num(*var):

	Sum = 0

	for i in var:

		Sum = Sum + i

	return Sum

print('sum of N natural number : ',Sum_of_Num(1,2,3,4,5,6,7,8,9,10))
# sum of N natural number :  55





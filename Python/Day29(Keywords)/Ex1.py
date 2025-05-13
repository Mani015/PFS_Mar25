# Keywords 

# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# The global and nonlocal keywords used to change the scope of values with in the function


def New_tech():

	global x

	x = 10

	print('local var : ', x)



New_tech()
print(f'local variable is executed outside of function : {x}')

# local var :  10
# local variable is executed outside of function : 10



def new_Tech():

	print('Welcome to User defined functions')


# new_Tech()

# Welcome to User defined functions


# It can take arguments and returns the value.

def Profile(Name : str, Age : int):

	print(f'Name : {Name}')
	print(f'Age : {Age}')


# Profile()
# TypeError: Profile() missing 2 required positional arguments: 'Name' and 'age'

# Profile('Dathri')
# TypeError: Profile() missing 1 required positional argument: 'age'

Profile('Dathri',20)

# Name : Dathri
# Age : 20


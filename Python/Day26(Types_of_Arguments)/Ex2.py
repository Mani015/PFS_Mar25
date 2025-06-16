# Default Arguments
# In a function, arguments can have default values.
# We assign default values to the argument using the ‘=’ (assignment) operator 
# at the time of function definition.
# You can define a function with any number of default arguments.

# def add(x=10,y=20):
# 	sum=x+y 
# 	print(f'x is : {x}')
# 	print(f'y is : {y}')
# 	print(f'sum is : {sum}')
# add(30)

# x is : 30
# y is : 20
# sum is : 50

def profile(Name='Nithin',age=21,location='Bangalore'):
	print(f'Name is : {Name}')
	print(f'Age is : {age}')
	print(f'location is : {location}')
# profile()

# Name is : Nithin
# Age is : 21
# location is : Bangalore

# let's see if i pass a value while function calling
profile('Anil',20,'Chennai')

# Name is : Anil
# Age is : 20
# location is : Chennai



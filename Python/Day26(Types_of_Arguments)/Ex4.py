

def Person(Name='mahesh',age = 12, location = "pune"):
	print(f'Name is : {Name}')
	print(f'Age is : {age}')
	print(f'location is : {location}')


# Person()
# I need to change Person location 

# Person('Bangalore')
# Name is : Bangalore
# Age is : 12
# location is : pune


# Person('mahesh',12,'Bangalore')
# Name is : mahesh
# Age is : 12
# location is : Bangalore


# Replace value using keyword arguments


# Person(location = 'Bangalore')
# Name is : mahesh
# Age is : 12
# location is : Bangalore

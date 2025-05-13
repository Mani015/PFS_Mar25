# Keyword Arguments:
# Usually, at the time of the function call, values get assigned to the arguments 
# according to their position.
# So we must pass values in the same sequence defined in a function definition.

# def laptop(brandname,price,color):
# 	print(f'brandname : {brandname}')
# 	print(f'price : {price}')
# 	print(f'color : {color}')
# laptop(brandname='dell',price=58700,color='black')

# brandname : dell
# price : 58700
# color : black

# laptop(color='grey',brandname='hp',price=40000)

# brandname : hp
# price : 40000
# color : grey

def natural_num(x,y,z):
	print(f'x is : {x}')
	print(f'y is : {y}')
	print(f'z is : {z}')
x=10
y=20
z=15
natural_num(x=y,y=z,z=x)

# x is : 20
# y is : 15
# z is : 10
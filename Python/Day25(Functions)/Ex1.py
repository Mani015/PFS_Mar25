
def Calculator(x : int, y : int):

	print(f'Sum of x + y : {x + y}')
	print(f'Difference of x - y : {x - y}')
	print(f'Product of x * y : {x * y}')
	print(f'Division of x / y : {x / y}')


# Calculator(2,3)
# Sum of x + y : 5
# Difference of x - y : -1
# Product of x * y : 6
# Division of x / y : 0.6666666666666666
print()

# Calculator(5,7)
# Sum of x + y : 12
# Difference of x - y : -2
# Product of x * y : 35
# Division of x / y : 0.7142857142857143


l1 = [9,8,7,6,5]
l2 = [1,2,3,4,5]

# [10,8,9,0.1]

for i in range(len(l1)):
	Calculator(l1[i], l2[i])
	print('*********************')


# 
# Sum of x + y : 10
# Difference of x - y : 8
# Product of x * y : 9
# Division of x / y : 9.0
# *********************
# Sum of x + y : 10
# Difference of x - y : 6
# Product of x * y : 16
# Division of x / y : 4.0
# *********************
# Sum of x + y : 10
# Difference of x - y : 4
# Product of x * y : 21
# Division of x / y : 2.3333333333333335
# *********************
# Sum of x + y : 10
# Difference of x - y : 2
# Product of x * y : 24
# Division of x / y : 1.5
# *********************
# Sum of x + y : 10
# Difference of x - y : 0
# Product of x * y : 25
# Division of x / y : 1.0
# *********************



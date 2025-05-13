
def Calculator(x : int, y : int):

	print(f'Sum of x + y : {x + y}')
	print(f'Difference of x - y : {x - y}')
	print(f'Product of x * y : {x * y}')
	print(f'Division of x / y : {x / y}')



s1 = [5,10,12,30,42,58]
p1 = [3,13,18,19,25]


if len(s1) == len(p1):

	for i in range(len(s1)):

		Calculator(s1[i], p1[i])
		print('--------------------')


else:
	print(f'neither not same length')

# neither not same length


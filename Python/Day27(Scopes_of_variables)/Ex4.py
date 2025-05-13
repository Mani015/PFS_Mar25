

# Inbuilt scope : Those functions are comes from  Inbuilt like print, input, max, min, len,sum......


#global var
x1 = 10
print('global var : ', x1)

def Fun1():
	# enclosing var
	x2 = 20
	print('Enclosing var : ', x2)

	def Fun2():
		# local var
		x3 = 25
		print('Local var : ', x3)

		collect : list[int] = [x1,x2,x3]
		print(collect)
		print(f'max num :{max(collect)}')
		print(f'min num :{min(collect)}')
		print(f'sum of : {sum(collect)}')

	Fun2()

Fun1()


# global var :  10
# Enclosing var :  20
# Local var :  25
# [10, 20, 25]
# max num :25
# min num :10
# sum of : 55


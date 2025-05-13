

def Change1():
	global x
	x = 100 # enclosing variable

	print(f'enclosing var : {x}')

	def Change2():
		global y
		y = 200  # local variable

		print(f'local var : {y}')

	Change2()


Change1()

print('x is enclosing : ',x)
print('y is local : ',y)

# enclosing var : 100
# local var : 200
# x is enclosing :  100
# y is local :  200

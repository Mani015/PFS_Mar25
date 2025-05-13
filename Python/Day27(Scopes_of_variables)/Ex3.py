
# Enclosing variable : If you create enclosing variable , before that you should create nested function


# def Outer():
# 	# Enclosing scope
# 	Name = 'sudheer'
# 	print('Enclosing var : ', Name)
# 	def Inner():

# 		age = 20
# 		print('local var :', age)
# 	Inner()
# 	print('Enclosing var : ', Name)
# Outer()

# Enclosing var :  sudheer
# local var : 20
# Enclosing var :  sudheer




def Outer():
	# Enclosing scope
	Name = 'sudheer'
	print('Enclosing var1 : ', Name)
	def Inner():
		# calling enclosing var in local scope

		print('Enclosing var2 : ', Name)
		age = 20
		print('local var :', age)
	Inner()
	print('Enclosing var3 : ', Name)
Outer()

# Enclosing var1 :  sudheer
# Enclosing var2 :  sudheer
# local var : 20
# Enclosing var3 :  sudheer




# Enclosing scope :
# Enclosing scope is also same a local scope on what (Firstly it checks with in that self)


# x1 = 10

# def fun1():

# 	x1 = 20
# 	print('Enclosing var : ',x1)  # Enclosing var :  20

# 	def fun2():

# 		x1 = 30
# 		# print('Local var : ', x1)

# 	fun2()

# fun1()


# Varible declared in global scope, but calling from enclosing scope.

# Global var
x1 = 10

def fun1():

	# There no value in enclosing
	print('Enclosing var : ',x1)  # Enclosing var :  10

	def fun2():

		x1 = 30
		# print('Local var : ', x1)

	fun2()

fun1()

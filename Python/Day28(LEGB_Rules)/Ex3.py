# Global rule : Firstly it check in global scope, if value doesn't exist in global scope check into Built in scope

g1 = 10
print('global var : ', g1)

def fun1():

	g1 = 20

	def fun2():

		g1 = 30


	fun2()

fun1()

# global var :  10



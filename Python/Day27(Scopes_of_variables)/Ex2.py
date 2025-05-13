
# Global variable : A variable is global variable , which is declared outside of the function,
# we can use anywhere

num = 10
print('global var : ',num)

def Entire():

	var = 'suresh'
	print('local var : ', var)
	# call global variable
	print('global var : ', num)


Entire()
# call outside of the function
print('global var :', num)

# global var :  10
# local var :  suresh
# global var :  10
# global var : 10

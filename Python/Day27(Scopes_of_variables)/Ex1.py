# There are four types of scopes 
# 1.Local scope
# 2.Global scope
# 3.Enclosing scope
# 4.Built -in scope

# What is local variable ?
# A variable is which is declared inside of the function

def My_fun():

	# Local variable
	Name = "python"
	print('Local var : ', Name)


My_fun()
# Local var :  python

# Here, trying to call local var to outside of the function
print('Local var : ', Name)

# NameError: name 'Name' is not defined

# 1.Local scope : Local variables calls with in the function,but not call outside of the function



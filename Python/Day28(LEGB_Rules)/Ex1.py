# LEGB Rules : Local, Enclosing, Global, Built-in

# Local rule.
# Local rule First checks with in that self, if the value exist it returns.
# Name : 'str' = "dawrn"

# def Info():

# 	# local scope
# 	Name  : str = 'Pawan'
# 	print(Name)

# Info()



# if the value doesn't exist in local scope, it checks outside local scope

Name : 'str' = "drwan"

def Info():

	# I didn't declare variable in local scope
	
	print('Local var :',Name) # Local var : drwan

Info()



# Arbitrary keyword arguments (**kwargs):
# We saw how to use *args. Now let’s see how to use the **kwargs argument.
# The **kwargs allow you to pass multiple keyword arguments to a function.
# Use the **kwargs if you want to handle named arguments in a function


def Country(**india):
	print(type(india))
	print(india)

Country(Ap = 'Amaravathi',Telangana = 'hybderabad',karnataka = "Bangolore")

# <class 'dict'>
# {'Ap': 'Amaravathi', 'Telangana': 'hybderabad', 'karnataka': 'Bangolore'}



# Python decorators are a powerful tool that allow programmers to modify a function or
# class's behavior without permanently changing the original code.

# 1).assigning function to a variable
# 2). Passing Function as an Argument in Python
# 3). Function Returning Another Function in Python
# 4).Nested Functions in Python

def New_function():

    print('Welcome to decorators')


# new = New_function
# new() # Welcome to decorators


# 2). Passing Function as an Argument in Python

def First_Name():

    return "Ranjith"

def Last_Name():

    return "kumar"

def Chagetoupper(func):
    print(func().upper())

Chagetoupper(First_Name) # RANJITH
Chagetoupper(Last_Name) # KUMAR



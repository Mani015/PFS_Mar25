
# Function Returning Another Function in Python

def Outer():
    def Inner():
        return "This is nested function"
    return Inner #This is nested function

ob1 = Outer()
print(f'Inner function return :{ob1()}')
print(f'Outer function returns : {ob1.__name__}')
# Inner function return :This is nested function
# Outer function returns : Inner


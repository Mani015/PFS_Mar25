

def Decorator(func):

    def Wrapped():
        Name = func()
        return f"Hi, Good morning " + Name
    return Wrapped



def wish():
    return "Suresh"

# v1 = Decorator(wish)
# print(v1())
# Hi, Good morning Suresh


# with decorator

@Decorator
def Greets():
    return 'Simhadri'

print(Greets())

# Hi, Good morning Simhadri

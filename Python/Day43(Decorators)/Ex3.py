

def My_Decorator(func):

    def Wrapper():
        print('Before calling')
        func()
        print('After completion')
    return Wrapper



def call_by_name():
    print("Hello, My name is Darla")

# call_by_name()

# With out using decorator
deco = My_Decorator(call_by_name)
deco()
# Before calling
# Hello, My name is Darla
# After completion

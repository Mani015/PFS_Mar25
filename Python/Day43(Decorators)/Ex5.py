


def My_decorator(new):

    def Current_num(a,b):
        print(f"current function is : {new.__name__}(a,b), arguments : {a,b}")
        return new(a,b)
    return Current_num

def Addtwonum(a,b):
    print(a + b)

v1 = My_decorator(Addtwonum)
v1(4,5)
# current function is : Addtwonum(a,b), arguments : (4, 5)
# 9

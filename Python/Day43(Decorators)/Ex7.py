def dec1(num):
    def dec2(func):
        global i
        for i in range(num):
            func()
    return dec2





# iterate N numbers

def Sequence():
    print('Loop  :', i)


# without decorator
dec1(10)(Sequence)
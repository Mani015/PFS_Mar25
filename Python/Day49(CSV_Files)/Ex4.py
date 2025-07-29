
# print([i for i in range(1,101) if i % 2 == 0][:20:])



# print(f'global var : {Name}')
def fun():
    global Name
    Name = "lokesh"
    # print(f'local var : {Name}')

    # print(f'global var : {globals()["Name"]}')

fun()
# print(globals())
print(f'global var : {Name}')


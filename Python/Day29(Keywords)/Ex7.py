


x = 12
# print('global var : ', x)


def Emp():

    Name = 'reddy pasand'
    age = 12
    salary = 50000

    print(locals())


# Emp()
# {'Name': 'reddy pasand', 'age': 12, 'salary': 50000}



def out():

    x = 10
    print('enclosing : ', x)
    print(locals())
    def In():

        x = 20
        print('local var : ', x)
        print('enclosing var : ',x)

        print(locals())

    In()

out()

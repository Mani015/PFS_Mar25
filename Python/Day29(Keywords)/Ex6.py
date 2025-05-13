

Name = "pranay"
print('Global var : ', Name)
Age = 20

def Profile():

    Name = "Santhosh"
    Age = 12
    print(f'Name : {Name}, Age : {Age}')
    #Return the dictionary containing the current scope's global variables.

    print('Global var : ', globals()['Name'])
    print('Global var : ', globals().get('Age'))


Profile()


# print(help(globals))
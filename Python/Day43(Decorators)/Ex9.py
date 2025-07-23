
def Required_Login(permit):
    def wrapped(username):
        password = int(input('Enter your password :'))
        if username == 'python' and password == 1234:
            permit(username)
        else:
            print('Access Denied')
    return wrapped


@Required_Login
def Restricted_Login(username):
    print('Access Granted')
Restricted_Login(username=input('Enter your name :'))

# Enter your name :python
# Enter your password :12345
# Access Denied


# Enter your name :python
# Enter your password :1234
# Access Granted



# @ Symbol With Decorator
# Instead of assigning the function call to a variable, Python provides a much more elegant way to achieve this functionality using the @ symbol.
#
def make_pretty(func):

    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()

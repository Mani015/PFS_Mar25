



def My_Auth(func):

    def Permission(user):
        if user == 'admin':
            return func(user)
        else:
            return "Denied"
    return Permission

@My_Auth
def my_obervation(user):
    return f'{user} login successfully'


print(my_obervation('admin'))
# admin login successfully

print(my_obervation('user'))
# Denied


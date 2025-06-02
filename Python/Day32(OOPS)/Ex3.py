# Constructors in Python

# In Python, a constructor is a special type of method used to initialize the object of a Class.
# The constructor will be executed automatically when the object is created. If we create three objects,
# the constructor is called three times and initialize each object.

# The main purpose of the constructor is to declare and initialize instance variables. It can take at least one argument that is self.
#  The __init()__ method is called the constructor in Python. In other words, the name of the constructor should be __init__(self).

# A constructor is optional, and if we do not provide any constructor, then Python provides the default constructor.
# Every class in Python has a constructor, but it's not required to define it.


# def __init__(self):
#     # body of the constructor
#        Where,

# def: The keyword is used to define function.
# __init__() Method: It is a reserved method. This method gets called as soon as an object of a class is instantiated.
# self: The first argument self refers to the current object. It binds the instance to the __init__() method.
# It’s usually named self to follow the naming convention.

class Profile(object):

    def __init__(self,Name : str, Age : int, Address : str):
        # object/self . new_variable = Attribute
        self.pname = Name
        self.page = Age
        self.paddress = Address

        print(f'name : {self.pname},'
              f'age : {self.page},'
              f'Address : {self.paddress}')


Profile('suresh',10,'india')
Profile('simhadri', 11, 'USA')
Profile('Shiva', 12, 'Japan')










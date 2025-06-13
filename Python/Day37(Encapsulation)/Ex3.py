
# Protected Members
# Protected Members are those that can be accessed from within the class and its sub-classes. These protected members cannot be accessed from outside of the class.
#
# Protected Members of the class can be declared using underscore( "_" ) preceding their respective names.
#
# # Protected variables
# _age, _name
#
# # Protected methods
# _func(), _m1()
# These private members can be accessed from inside the class and also can be accessed by its child class. But if we try to access them from outside of the class then AttributeError is returned.
#
# In the below example, we have student class and self._name and self._marks as protected variables and _details() as a protected method. These protected variables and methods can be accessed from within the class and its subclass. But if we try to access them from outside then PVM throws an error.
#
class student:
    def __init__(self, name, marks):
        # protected variables
        self._name = name
        self._marks = marks

    # protected method
    def _details(self):
        print("name is", self._name)

class age(student):
    def info(self):
        self._details()
        print("age is 15")

obj = age("john", 90)
obj.info()
#
# # Output
# name is john
# age is 15
# Thus the protected members of a class can be accessed from its child class object_reference directly.
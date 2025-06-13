
# Private Members
# Private Members of a class are those that can be accessed from within the class itself and cannot be accessed from outside of the class or its subclass. Private members are declared differently when compared to public members.
#
# Private Members of the class can be declared using double underscore( "__" ) preceding their respective names.
#
# # Private variables
# __age, __name, __value
#
# # Private methods
# __func(), __m1()
# These private members can be accessed from inside the class directly. But if we try to access them from outside of the class then AttributeError is returned.
#
# In the below example, we have employee class and self.__name and self.__age as private variables and __details() as a private method. These private variables and methods can be accessed from within the class. But if we try to access them from outside then PVM throws an error.
#
class employee:
  def __init__(self, name, age):
    # private variables
    self.__name = name
    self.__age = age

  # private method
  def __details(self):
    print("age is", self.__age)

  def name(self):
    print("name :- ", self.__name)
    # accessing method from inside of class
    self.__details()

obj = employee("john", 25)
obj.name()

# Output
# name :-  john
# age is 25
#
# If we want access to these private members outside of the class then we need to use the objectreference._classname__variablename.
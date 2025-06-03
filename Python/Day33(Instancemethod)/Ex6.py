
# Let’s see how to create a factory method using the class method.
# we will create a Student class object using the class method.

from datetime import date

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls, name, birth_year):
        # calculate age
        # return new object
        return cls(name, date.today().year - birth_year)

    def show(self):
        print(self.name + "'s age is: " + str(self.age))

x1 = Student('Nithin',21)
x1.show()

# create new object using the factory method
joy = Student.calculate_age("suresh", 2004)
joy.show()

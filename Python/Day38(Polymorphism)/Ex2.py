
# Polymorphism With Inheritance
# Polymorphism is mainly used with inheritance. In inheritance, child class inherits the attributes and methods of a parent class.
# The existing class is called a base class or parent class,
# and the new class is called a subclass or child class or derived class.

# 1.Method overriding
# 2.Method over loading



# Using method overriding polymorphism allows us to defines methods in the child class that have the same name as the methods in the parent class.
# This process of re-implementing the inherited method in the child class is known as Method Overriding.

class Person(object):

    def __init__(self,Name,Age):
        self.name = Name
        self.age  = Age



class Person1(Person):

    def __init__(self,Name,Age,salary):
        self.name = Name
        self.age = Age
        self.salary = salary

# ob1  = Person1()




# The process of inheriting the properties of the parent class into a child class is called inheritance.
# The existing class is called a base class or parent class and the new class is called a subclass or child class or derived class.
#
# In Object-oriented programming, inheritance is an important aspect.
# The main purpose of inheritance is the reusability of code because we can use the existing class to create a new class instead of creating
#  it from scratch.
#
# In inheritance, the child class acquires all the data members, properties, and functions from the parent class. Also,
# a child class can also provide its specific implementation to the methods of the parent class.
#
# Types Of Inheritance
# In Python, based upon the number of child and parent classes involved, there are five types of inheritance.
#
# The type of inheritance are listed below:
#
# Single inheritance
# Multiple Inheritance
# Multilevel inheritance
# Hierarchical Inheritance
# Hybrid Inheritance
# Now let’s see each in detail with an example.
#
# Single Inheritance
# In single inheritance, a child class inherits from a single-parent class. Here is one child class and one parent class.


class Parent(object):

    def __init__(self,name,amount):

        self.name = name
        self.amount = amount

    def Property(self):
        print(f'Name {self.name}, Amount : {self.amount}')

class Child(Parent):

    def Property(self):
        print(f'Name {self.name}, Amount : {self.amount}')


# Father : Parent = Parent('Aristotle',1000)
# Father.Property()

Suresh : Child = Child('suresh',20000)
Suresh.Property()


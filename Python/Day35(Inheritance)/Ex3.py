
class Parent(object):

    def Method(self):
        print('This is parent class')

# class Child(Parent):
#     def Method(self):
#         print('I am Child class')


# ob1 : Child = Child()
# ob1.Method()
# ob1.Method()



#Multiple Inheritance
# In multiple inheritance, one child class can inherit from multiple parent classes.
# So here is one child class and multiple parent classes.


class Parent1(object):

    def Property1(self):
        print('I am Parent1 class')

class Parent2(object):

    def Property2(self):
        print('I am parent2 class')


class Child(Parent1,Parent2):

    def Property3(self):
        print('This is Child class')

kavya : Child = Child()

kavya.Property1()
kavya.Property2()
kavya.Property3()
# I am Parent1 class
# I am parent2 class
# This is Child class



# Method Resolution Order :
# Method Resolution Order(MRO) it denotes the way a programming language resolves a method or attribute.
#  Python supports classes inheriting from other classes. The class being inherited is called the Parent or Superclass,
# while the class that inherits is called the Child or Subclass.

#  In python, method resolution order defines the order in which the base classes are searched when executing a method.
# First, the method or attribute is searched within a class and then it follows the order we specified while inheriting.
# This order is also called Linearization of a class and set of rules are called MRO(Method Resolution Order).
#  While inheriting from another class, the interpreter needs a way to resolve the methods that are being called via an instance.
#  Thus we need the method resolution order.

# Multilevel inheritance
# In multilevel inheritance, a class inherits from a child class or derived class. Suppose three classes A, B, C.
#  A is the superclass, B is the child class of A, C is the child class of B. In other words, we can say a chain of classes is called multilevel inheritance.
# --------------------------------------------------------------------------------------------------------------
# Hierarchical Inheritance
# In Hierarchical inheritance, more than one child class is derived from a single parent class.
# In other words, we can say one parent class and multiple child classes.
# -----------------------------------------------------------------------------------------------------------------------------
# Hybrid Inheritance
# When inheritance is consists of multiple types or a combination of different inheritance is called hybrid inheritance.


class grand_parent(object):

    def property1(self):

        print('this is grand parent')
class parent(grand_parent):

    def property2(self):

        print('this is parent ')

class child(parent):

    def property3(self):
        print('this is child')


suresh : child = child()

suresh.property1()
suresh.property2()
suresh.property3()
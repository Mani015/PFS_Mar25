

# Encapsulation in Python
# Encapsulation is a concept of wrapping the data and methods into a single entity.
#  Every Class in Python is an example of Encapsulation. Because we wrap the methods and data under a single entity known as class.
#
# In Python, encapsulation is one of the fundamental concepts and it can also be referred to as implementing data hiding and abstraction concepts together.
#
# In the below example, we are wrapping up the value variable and method(m1) under a single class,
# this concept is known as encapsulation. Based on requirements we can change the access modifiers of these variables and methods.
#
class employee:
    def __init__(self):
        self.age = 25

    def age(self):
        print(self.age)


obj = employee()
obj.age()

# # Output
# 25
# Similar to other languages such as Java,
# we don’t have any public, private, protected keywords but the concepts related to these terms can be implemented.








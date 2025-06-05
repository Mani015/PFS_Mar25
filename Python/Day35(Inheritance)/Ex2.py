

class Parent(object):

    def Method1(self):
        print('This is parent class')



class Child(Parent):

    def Method2(self):
        print('I am Child class')


ob1 : Child = Child()
ob1.Method1()
ob1.Method2()

# This is parent class
# I am Child class




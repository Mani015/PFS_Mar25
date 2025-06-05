class Parent(object):

    def Method(self):
        print('This is parent class')



class Child(Parent):

    def Method(self):
        print('I am Child class')
        super().Method()

simhadri : Child = Child()

simhadri.Method()
class  parent(object):
    def show(self):
        print('I am the parent class')

class child1(parent):
    def show(self):
        print('This is child class 1')


class child2(parent):
    def show(self):
        print('This is child class 2')


class child3(parent):
    def show(self):
        print('This is child class 3')
        parent().show()

c1=child1()
c2=child2()
c3=child3()

c1.show()
c2.show()
c3.show()



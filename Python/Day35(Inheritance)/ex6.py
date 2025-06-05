class grand_parent(object):

    def property(self):

        print('this is grand parent')
class parent(grand_parent):

    def property(self):

        print('this is parent ')
        super().property()

class child(parent):

    def property(self):
        print('this is child')
        super().property()


suresh : child = child()
suresh.property()


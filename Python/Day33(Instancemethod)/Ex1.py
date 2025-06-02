

class Student(object):

    def __init__(self,Sname,Sage,Smarks,Saddress,Sgrade):
        self.name = Sname
        self.age  = Sage
        self.marks = Smarks
        self.address = Saddress
        self.grade = Sgrade



    def Display(self):
        print(
            f'name : {self.name},'
            f'age : {self.age}, marks : {self.marks},'
            f'address : {self.address}, grade : {self.grade}'
        )

    def Tempo(self):
        print('Instance methods are used to access & modify the instance variables')


# Variable : type_class = class_name(object)

Yogeswar  : Student = Student('yogeswar',12,100,'vizag','O-Grade')

# how to call Instance method
# sy : objectname.MethodName()

# Yogeswar.Display()
# name : yogeswar,age : 12, marks : 100,address : vizag, grade : O-Grade

# Yogeswar.Tempo()


# Student.Display()
# TypeError: Display() missing 1 required positional argument: 'self'

suresh : Student = Student('suresh',13,100,'nellore','O-Grade')
suresh.Display()


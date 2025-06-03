

# Class method: Used to access or modify the class state.
# In method implementation, if we use only class variables,
# then such type of methods we should declare as a class method.
# The class method has a cls parameter which refers to the class.




class Student(object):

    school_name = "GRK_Technology school"  # class name
    def __init__(self,Stu_name,Stu_age,Stu_marks,Stu_location):

        self.name = Stu_name
        self.age = Stu_age
        self.marks = Stu_marks
        self.location = Stu_location



    @classmethod
    def Access_cls_var(cls):
        print(f'School name : {cls.school_name}')


    def Display(self):
        print(self.name, self.age,self.marks,self.location)




Pasand : Student = Student('Reddy pasand',19,99,'Kadapa')
Pasand.Display()
Pasand.Access_cls_var()
# Reddy pasand 19 99 Kadapa
# School name : GRK_Technology school

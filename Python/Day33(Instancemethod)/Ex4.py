
# Class attributes are variables defined inside a specific class and used by all objects.
#


class Student(object):

    school_name = "GRK_Technology school"  # class name
    def __init__(self,Stu_name,Stu_age,Stu_marks,Stu_location):

        self.name = Stu_name
        self.age = Stu_age
        self.marks = Stu_marks
        self.location = Stu_location



Simhadri : Student = Student('Simhadri',10,100,'Nellore')
Madhuri : Student = Student('madhuri',12, 100, 'kurnool')
Sonia : Student = Student('Sonia',14,100,'Madanapalli')

for stu in [Simhadri,Madhuri,Sonia]:

    print(f'Name : {stu.name}')
    print(f'Age : {stu.age}')
    print(f'marks : {stu.marks}')
    print(f'location : {stu.location}')
    print(f'schoolName : {stu.school_name}')
    print('🚸🚸🚸🚸🚸🚸🚸🚸🚸🚸')
    print()



# Name : Simhadri
# Age : 10
# marks : 100
# location : Nellore
# schoolName : GRK_Technology school
# 🚸🚸🚸🚸🚸🚸🚸🚸🚸🚸
#
# Name : madhuri
# Age : 12
# marks : 100
# location : kurnool
# schoolName : GRK_Technology school
# 🚸🚸🚸🚸🚸🚸🚸🚸🚸🚸
#
# Name : Sonia
# Age : 14
# marks : 100
# location : Madanapalli
# schoolName : GRK_Technology school
# 🚸🚸🚸🚸🚸🚸🚸🚸🚸🚸


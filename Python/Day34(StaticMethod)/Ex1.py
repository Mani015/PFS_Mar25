# What is Static Methods in Python
# Define Static Method in Python
#     Example: Create Static Method Using @staticmethod Decorator
# Advantages of a Static Method
#
# Call Static Method from Another Method
#
# Static methods: A static method is a general utility method that performs a task in isolation.
# Inside this method, we don’t use instance or class variable because this static method doesn’t take any parameters like self and cls.
# Any method we create in a class will automatically be created as an instance method.
# We must explicitly tell Python that it is a static method using the @staticmethod decorator or staticmethod() function.
#
# Static methods are defined inside a class, and it is pretty similar to defining a regular function. To declare a static method, use this idiom:




class Employee(object):

    def __init__(self,Name,Cname, project_name):
        self.name = Name
        self.cname = Cname
        self.project_name = project_name

    @staticmethod
    def Requirement(Project_Name):
        if Project_Name == 'ABC project':
            requirement = ['Login_Task', 'Menu_Task', 'profile_Task']

        else:
            requirement = ['Task1']

        return requirement

    #Instance method

    def Work(self):
        requirement = self.Requirement(self.project_name)

        for Task in requirement:
            print(Task, 'completed')



Babji : Employee = Employee('Babji','CapGemini','ABC project')

# Babji.Work()
# #
# Login_Task completed
# Menu_Task completed
# profile_Task completed

suresh : Employee = Employee('Babji','CapGemini','xyz project')

suresh.Work()

# Task1 completed


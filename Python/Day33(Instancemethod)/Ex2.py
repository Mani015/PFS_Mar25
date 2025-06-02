#
# Instance variables: If the value of a variable varies from object to object, then such variables are called instance variables.
#
# Create Instance Variables
# Instance variables are declared inside a method using the self keyword.
# We use a constructor to define and initialize the instance variables. Let’s see the example to declare an instance variable in Python.
#
# When we create classes in Python, instance methods are used regularly.
# we need to create an object to execute the block of code or action defined in the instance method.
#
# Instance variables are used within the instance method.
# We use the instance method to perform a set of actions on the data/value provided by the instance variable.
#
# We can access the instance variable using the object and dot (.) operator.
#
# In Python, to work with an instance variable and method, we use the self keyword.
#  We use the self keyword as the first parameter to a method. The self refers to the current object.
#
# Instance method: Used to access or modify the object state. If we use instance variables inside a method,
# such methods are called instance methods. It must have a self parameter to refer to the current object.


class Employee(object):

    def __init__(self,Ename : str,Eage : int ,Esalary : float,Eaddress : str,Edomain : str,):

        self.name : str  = Ename
        self.age : int = Eage
        self.salary : float = Esalary
        self.address  : str = Eaddress
        self.domain : str = Edomain

    # Accessing Instance variables

    def Execute(self):
        print(
            f'Ename : {self.name},'
            f'Eage : {self.age}, Esalary : {self.salary},'
            f'Eaddress : {self.address}, domain : {self.domain}'
        )

    #Modify Instance variable

    def Change_Domain(self,New_Domain):
        self.domain = New_Domain




Sonia : Employee = Employee('Sonia',21,38000.500,'Kurnool-city','python developer')
Sonia.Execute() # Ename : Sonia,Eage : 21, Esalary : 38000.5,Eaddress : Kurnool-city, domain : python developer
print()
Sonia.Change_Domain('Java Developer')
Sonia.Execute()





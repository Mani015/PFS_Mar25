
# Class Variables: A class variable is a variable that is declared inside of class, but outside of any instance method or __init__() method.
#
#
# Class attributes are variables defined inside a specific class and used by all objects.
#  We can call attributes using the class name, attribute name, and the dot (.) operator.


class Car(object):

    no_of_seats = "4-seator"
    certified_by = 'Indian.org'

    def __init__(self,Cname,Ccolor,CPrice,Cmodel,Ctype,C_MFY):

        self.name = Cname
        self.color = Ccolor
        self.price = CPrice
        self.model = Cmodel
        self.fuel = Ctype
        self.mfy = C_MFY

    def Start(self):
        print(
            self.name,
            self.color,self.price,
            self.model,self.fuel,self.mfy
        )

    # Accessing class variables with instance method
    def Run(self):
        print(
            self.name,
            self.color, self.price,
            self.model, self.fuel, self.mfy,
            self.no_of_seats,self.certified_by
        )


    #Modify the class variable with class method

    def change_Classvar(self,update_certified):

        self.certified_by = update_certified
        print('Update successfully')


BMW : Car = Car('BMW','Black',7500000,'BMWX1','Petrol','2024-10-12')
# BMW.Start()
# print()
# BMW.Run()  # BMW Black 7500000 BMWX1 Petrol 2024-10-12 4-seator Indian.org


BMW.Run() # # BMW Black 7500000 BMWX1 Petrol 2024-10-12 4-seator Indian.org
print()
BMW.change_Classvar('Indiancars.org')
BMW.Run()
# Update successfully
# BMW Black 7500000 BMWX1 Petrol 2024-10-12 4-seator Indiancars.org



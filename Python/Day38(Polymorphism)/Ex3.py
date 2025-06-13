
#
# mehtod overloading
# Two or more methods have the same name but different numbers of parameters or
# different types of parameters, or both.
# These methods are called overloaded methods and this is called method overloading.


class Parent(object):

    def Property(self,name,age):
        print(f'Name : {name}, age : {age}')

    def Property(self,name,age,location):
        print(f'Name : {name}, age : {age}, location : {location}')

    def Property(self,name,age,location,salary):
        print(f'Name : {name}, age : {age}, location : {location},salary : {salary}')


Father : Parent = Parent()
# Father.Property('bharath',20)
# TypeError: Property() missing 2 required positional arguments: 'location' and 'salary'

# Father.Property('Bharath',20,'kadapa')
# TypeError: Property() missing 1 required positional argument: 'salary'

Father.Property('Bharath',20,'kadapa',45000)
# Name : Bharath, age : 20, location : kadapa,salary : 45000

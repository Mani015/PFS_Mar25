# To overcome methodoverloading using one module
# That module name is : multipledispatch
# Open terminal : pip install multipledispatch



from multipledispatch import dispatch
class Parent(object):

    @dispatch(str,int)
    def Property(self,name,age):
        print(f'Name : {name}, age : {age}')

    @dispatch(str, int,str)
    def Property(self,name,age,location):
        print(f'Name : {name}, age : {age}, location : {location}')

    @dispatch(str, int,str, float)
    def Property(self,name,age,location,salary):
        print(f'Name : {name}, age : {age}, location : {location},salary : {salary}')

ob1 = Parent()
ob1.Property('jayanthi',10)
# Name : jayanthi, age : 10

# ob1.Property(12,20,'chennai')
# NotImplementedError: Could not find signature for Property: <int, int, str>

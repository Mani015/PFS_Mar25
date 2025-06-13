
# Public Members
# Public members are those that are accessible from inside and outside of the class.
#  These members are wrapped into a single entity so that they can be accessed from both inside and outside of the entity.
#
# By default, In python every variable, every method is a public member.
#  We don’t have to explicitly declare them as public or change the access modifier into public.
#
# In the below example, company is a class that has members inside it.
# All these members of the class are by default public and can be accessed inside and outside using the reference variable.
#
class company:
    def __init__(self):
        self.revenue = "75 lacs"

    def members(self):
        print("The number of employees are 150")
        print("Revenue generated:- ", self.revenue)


obj = company()
obj.members()

# # Output
# The number of employees are 150
# Revenue generated:- 75 lacs
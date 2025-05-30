# calling Attributes with thier class object

class Person(object):
    Name : str = "Suresh"  # attribute1
    Age : int = 20 # attribute2
    Location : str = "India"  # attribute3
    Profession : str = "Softwate developer"  # attribute4


#
# sy : classObject_name. attribute
yogi=Person()
print(f'{yogi.Name}')
print(yogi.Age)
print(yogi.Location)
print(yogi.Profession)
print()
# Update Attribute value
yogi.Name = 'pradeep'
print(f'{yogi.Name}')
print(yogi.Age)
print(yogi.Location)
print(yogi.Profession)


print()
sonia = Person()
print(f'{sonia.Name}')
print(sonia.Age)
print(sonia.Location)
print(sonia.Profession)

# Suresh
# 20
# India
# Softwate developer
print()

# delete a attribute
# sy : del object.attribute
del sonia.Name
# print(sonia.Name)
# AttributeError: Name


sonia.salary = 100000
print(sonia.salary)




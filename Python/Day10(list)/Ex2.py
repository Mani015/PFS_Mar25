
# Create a list
Name : list[str] = ['chaithanya','pasand','bharath','simhadri','sonia','vijay']
print(Name)

# If you want add a new value to Name,using append method
# sy : list.append(value/object)
# append method will add value at the end of the list

Name.append('Suresh')

print(Name)
# ['chaithanya', 'pasand', 'bharath', 'simhadri', 'sonia', 'vijay', 'Suresh']


# List allows duplicate values
Name.append('sonia')
print(Name)
# ['chaithanya', 'pasand', 'bharath', 'simhadri', 'sonia', 'vijay', 'Suresh', 'sonia']


# Name.append('vamsi','vindo')
# print(Name)
# TypeError: list.append() takes exactly one argument (2 given)



Name.append(['vamsi','vinod'])

print(Name)
# ['chaithanya', 'pasand', 'bharath', 'simhadri', 'sonia', 'vijay', 'Suresh', 'sonia', ['vamsi', 'vinod']]

